from django.shortcuts import render
from .models import HeartReading

def homepage(request):
    readings = HeartReading.objects.all()
    return render(request, 'heart_app/homepage.html', {'readings': readings})

def about(request):
    return render(request, 'heart_app/about.html')
