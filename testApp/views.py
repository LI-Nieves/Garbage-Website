import pyrebase
from django.shortcuts import render

from django.http import HttpResponse
from json import dumps

config = {
    "apiKey": "AIzaSyBt7pEVRkmpA8HjEqiqUaWEsgkMjLdWQeU",
    "authDomain": "garbagesite-e88ec.firebaseapp.com",
    "databaseURL": "https://garbagesite-e88ec-default-rtdb.firebaseio.com",
    "projectId": "garbagesite-e88ec",
    "storageBucket": "garbagesite-e88ec.appspot.com",
    "messagingSenderId": "405985594098",
    "appId": "1:405985594098:web:f5771d11bf8ce57eadde6b",
    "measurementId": "G-JBHDG183C8"
}

# initialize app with config
firebase = pyrebase.initialize_app(config)

# authenticate a user
#auth = firebase.auth()
#user = auth.sign_in_with_email_and_password("theman@gmail.com", "manliness")


db = firebase.database()

# Create your views here.

def bananaDrag(request):
    #subcat = db.child("users").get()
    idk = {"a":"b"}
    dataJSON = dumps(idk)
    return render(request, 'gui.html', {'data': dataJSON})





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