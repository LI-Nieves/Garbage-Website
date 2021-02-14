from django.shortcuts import render

from django.http import HttpResponse
from json import dumps

# Create your views here.

def bananaDrag(request):
    idk = {'a': 'b'}
    dataJSON = dumps(idk)
    return render(request, 'banana.html', {'data': dataJSON})

""" def opposites(request): 
    # create data dictionary 
    data = [ 
        ["Laugh", "Cry"], 
        ["Even", "Odd"], 
        ["Hot", "Cold"], 
        ["Light", "Dark"], 
        ["Opposite", "Same"], 
        ["Far", "Near"], 
        ["Give", "Take"], 
        ["Night", "Day"], 
        ["Import", "Export"], 
        ["Hard", "Easy"], 
        ["Never", "Always"], 
        ["Late", "Early"], 
        ["Less", "More"], 
        ["Male", "Female"], 
        ["Happiness", "Sadness"], 
        ["Fast", "Slow"], 
        ["Old", "Young"], 
        ["Boy", "Girl"], 
        ["Up", "Down"], 
        ["Left", "Right"], 
        ["Rich", "Poor"], 
        ["Love", "Hate"], 
        ["Inside", "Outside"], 
        ["Bad", "Good"], 
        ["Short", "Tall"], 
    ] 
    data = dumps(data) 
    return render(request, "opposites.html", {"data": data})  """