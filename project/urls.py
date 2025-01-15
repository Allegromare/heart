<!-- entire content of the file ... -->
from django.contrib import admin
from django.urls import path
from heart_app import views  # Importare view per la pagina homepage

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Rendere la pagina homepage
]
