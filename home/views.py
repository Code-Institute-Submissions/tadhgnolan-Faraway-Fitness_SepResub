from django.shortcuts import render
from django.http import HttpResponse
from .models import Welcome

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request=request, 
                  template_name='home/index.html',
                  context={'welcomes':Welcome.objects.all})
