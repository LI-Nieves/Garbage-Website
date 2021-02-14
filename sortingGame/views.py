from django.shortcuts import render

from django.http import HttpResponse
from json import dumps

# Create your views here.

def interact(request):
    return render(request, 'gui.html', {})