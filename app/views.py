#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
#from .models import Album

def index(request):
    return HttpResponse("Hello world!")
    '''
    template = loader.get_template('app/index.html')
    context = {
        'none': None,
    }
    return HttpResponse(template.render(context, request))
    '''