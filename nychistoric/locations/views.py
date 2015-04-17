from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class IndexView(View):
    template = 'locations/index.html'

    def get(self, request):
        return render(request,self.template)
