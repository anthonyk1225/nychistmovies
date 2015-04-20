from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse,Http404
from locations.models import Coordinate, Film

# Create your views here.
class IndexView(View):
    template = 'locations/index.html'

    def get(self,request):
        return render(request, self.template)

class CoordView(View):

    def get(self, request):
        raw_data = Coordinate.objects.all()
        coords = [(raw_coord.latitude, raw_coord.longitude, raw_coord.location_set.filter()[0].film_set.filter()[0].title if len(raw_coord.location_set.filter()) > 0 and len(raw_coord.location_set.filter()[0].film_set.filter()) > 0 else "n/a") for raw_coord in raw_data]
        return JsonResponse({"coords":coords})
