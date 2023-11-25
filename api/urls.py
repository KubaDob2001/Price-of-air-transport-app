from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),

    path('airports/', views.getAirports, name="airports"),
    path('airports/<str:pk>/', views.getAirport, name='airport'),

    path('airplanes/', views.getAirplanes, name='airplanes'),
    path('airplanes/<str:pk>/', views.getAirplane, name='airplane'),
]
