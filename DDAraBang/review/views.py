from django.shortcuts import render, redirect, reverse
import json
import requests
import time
from .models import *
from django.http import JsonResponse

# Create your views here.

def showhouses(request):
    places = Place.objects.all()
    schools = School.objects.all()
    test = Test.objects.first()

    context = {
        'places' : places,
        'schools' : schools,
        'test' : test,
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

def map_main(request) :
    schools = School.objects.all()

    context = {
        'schools': schools,
    }

    return render(request,'review/index.html',context=context)

def mapchanger(request):
    schoolinput = request.POST.get("schoolinput")
    schools=School.objects.all()
    test=Test.objects.first()
    print(test.school)
    test.school = schoolinput
    test.save()
    context = {}
    # return render(request, 'review/showhouses.html', context=context)
    return JsonResponse(context)