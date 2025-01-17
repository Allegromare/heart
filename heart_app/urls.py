from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('/about', views.about, name='about'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_reading, name='add_reading'),
]
