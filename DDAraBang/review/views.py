from django.shortcuts import render, redirect, reverse
import json
import requests
import geocoder
import openpyxl
import time
from .models import *

# Create your views here.

def showhouses(request):
    places = Place.objects.all()

    context = {
        'places':places,
    }

    return render(request, 'review/showhouses.html', context=context)

def createaddress(request):
  # Get
  if request.method == 'GET':
    return render(request, 'review/createaddress.html', context={})
  # Post
  elif request.method == 'POST':
    address = request.POST['address']
    context = {
        'address': address
    }
    return render(request, 'review/checkaddress.html', context=context)

def checkaddress(request):
    #Post
    if request.method == 'POST':
        address = request.POST['address']
        lat = request.POST['lat']
        lng = request.POST['lng']
        Place.objects.create(name=address, lat=lat, lng=lng)

        url = reverse('review:createaddress')
        return redirect(to=url)
