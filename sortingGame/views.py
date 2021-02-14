import pyrebase
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

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

def interact(request):
    return render(request, 'gui.html', {})