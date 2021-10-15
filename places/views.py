from django.shortcuts import render
from .models import Place

def places(request):
    place_objects = Place.objects.all()
    return render(request, 'places.html', {'places': place_objects})
