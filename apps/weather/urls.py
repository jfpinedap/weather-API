"""
Module for use of Weather urls
"""

from django.urls import path
from . import views

app_name='weather'

urlpatterns = [
    path('', views.WeatherView.as_view(), name='weather'),
]