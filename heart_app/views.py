from django.shortcuts import render, redirect
from .models import HeartReading

def homepage(request):
    readings = HeartReading.objects.all()
    return render(request, 'heart_app/homepage.html', {'readings': readings})

def about(request):
    return render(request, 'heart_app/about.html')

from django.contrib import messages

def add_reading(request):
    if request.method == 'POST':
        min_pressure = request.POST.get('min_pressure')
        max_pressure = request.POST.get('max_pressure')
        heart_rate = request.POST.get('heart_rate')

        if not all(x and 25 < int(x) < 250 for x in [min_pressure, max_pressure, heart_rate]):
            messages.error(request, 'I valori di pressione e battito cardiaco devono essere compresi tra 25 e 250.')
            return render(request, 'heart_app/add_reading.html')

        HeartReading.objects.create(min_pressure=min_pressure, max_pressure=max_pressure, heart_rate=heart_rate)
        messages.success(request, 'Lettura aggiunta con successo.')
        return redirect('homepage')
    return render(request, 'heart_app/add_reading.html')

def edit_reading(request, pk):
    reading = HeartReading.objects.get(pk=pk)
    if request.method == 'POST':
        reading.min_pressure = request.POST.get('min_pressure')
        reading.max_pressure = request.POST.get('max_pressure')
        reading.heart_rate = request.POST.get('heart_rate')
        reading.reading_time = request.POST.get('reading_time')

        if not all(x and 30 < int(x) < 200 for x in [reading.min_pressure, reading.max_pressure, reading.heart_rate]):
            messages.error(request, 'I valori di pressione e battito cardiaco devono essere compresi tra 30 e 200.')
            return render(request, 'heart_app/edit_reading.html', {'reading': reading})


        reading.save()
        return redirect('homepage')
    return render(request, 'heart_app/edit_reading.html', {'reading': reading})

def delete_reading(request, pk):
    reading = HeartReading.objects.get(pk=pk)
    reading.delete()
    return redirect('homepage')
