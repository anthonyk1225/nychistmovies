from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse,Http404

# Create your views here.
class IndexView(View):
    template = 'locations/index.html'

    def get(self,request):
        return render(request, self.template)

