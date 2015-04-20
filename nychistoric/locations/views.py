from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse,Http404
from locations.models import Coordinate, Film, Location

# Create your views here.
class IndexView(View):
    template = 'locations/index.html'

    def get(self,request):
        return render(request, self.template)

class CoordView(View):

    def get(self, request):
        locations = Location.objects.all()
        group = []
        for location in locations:
            group += [(coordinate.latitude,coordinate.longitude,location.film_set.filter()[0].title) for coordinate in location.coordinate.filter()]
        return JsonResponse({"coords": group})
