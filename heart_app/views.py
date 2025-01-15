from django.shortcuts import render
from . import settings  # Importare impostazioni del progetto

def homepage(request):
    return render(request, 'heart_app/homepage.html')
