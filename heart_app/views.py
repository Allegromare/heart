from django.shortcuts import render

def homepage(request):
    return render(request, 'heart_app/homepage.html')

def about(request):
    return render(request, 'heart_app/about.html')
