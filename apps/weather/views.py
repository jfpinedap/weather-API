"""
View of Weather
"""

# Libraries
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

class WeatherGetView(View):
    """Views of Weather"""

    def get(self, request):
        city = request.GET.get('city', None)
        country = request.GET.get('country', None)
        return JsonResponse({'city': city, 'country': country})

        