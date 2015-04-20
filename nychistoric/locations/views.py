from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse,Http404
from locations.models import Coordinate

# Create your views here.
class IndexView(View):
    template = 'locations/index.html'

    def get(self,request):
        return render(request, self.template)

class CoordView(View):

    def get(self, request):
        raw_data = Coordinate.objects.all()
        coords = [(raw_coord.latitude, raw_coord.longitude) for raw_coord in raw_data]
        return JsonResponse({"coords":coords})

