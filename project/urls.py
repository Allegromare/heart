from django.contrib import admin
from django.urls import path
from django.urls import include
# from heart_app import views  # Importare view per la pagina homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('heart_app.urls')),  # Includere le URL dell'app
]

