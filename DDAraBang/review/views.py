from django.shortcuts import render, redirect, reverse
import json
import requests
import time

from django.views.decorators.http import require_POST

import csv, io
from django.shortcuts import render
from django.contrib import messages

from .models import *
from django.http import JsonResponse


# one parameter named request
def school_upload(request):
    # declaring template
    template = "review/school_upload.html"
    data = School.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, lat, lng, gu',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    dataset = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(dataset)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = School.objects.update_or_create(
            name=column[0],
            lat=column[1],
            lng=column[2],
            gu=column[3],
        )
    context = {}
    return render(request,template,context)







# Create your views here.

def showhouses(request):
    places = Place.objects.all()
    schools = School.objects.all()
    test = Test.objects.first()
    reviewforms = ReviewForm.objects.all()
    data = {
        'reviewforms':reviewforms,
        'places' : places,
        'schools' : schools,
        'test' : test,
    }

    return render(request, 'review/showhouses.html', data)

# def createhouse(request):
#     if request.method == 'POST':
#         address = request.POST['address']
#
#     context = {
#         'address': address,
#     }
#     return render(request, 'review/createaddress.html', context=context)

def createaddress(request):
  # Get
  if request.method == 'GET':
    return render(request, 'review/createaddress.html', context={})
  # Post
  elif request.method == 'POST':
    houseaddress = request.POST['houseaddress']
    lat = request.POST['lat']
    lng = request.POST['lng']
    image = request.FILES['image']
    floor = request.POST['floor']
    advantage = request.POST['advantage']
    disadvantage = request.POST['disadvantage']
    water = request.POST['water']
    waterplus = request.POST['waterplus']
    light = request.POST['light']
    lightplus = request.POST['lightplus']
    noise = request.POST['noise']
    noiseplus = request.POST['noiseplus']
    security = request.POST['security']
    securityplus = request.POST['securityplus']
    bug = request.POST['bug']
    bugplus = request.POST['bugplus']
    money = request.POST['money']
    recommend = request.POST['recommend']

    place, is_created = Place.objects.get_or_create(
        name=houseaddress,
        lat=lat,
        lng=lng
    )

    # TODO : place 쓰기
    ReviewForm.objects.create(place=place, image=image, floor=floor,
                              advantage=advantage, disadvantage=disadvantage, water=water,
                              waterplus=waterplus, light=light, lightplus=lightplus, noise=noise,
                              noiseplus=noiseplus,
                              security=security, securityplus=securityplus, bug=bug, bugplus=bugplus, money=money,
                              recommend=recommend)

    # try:
    #     houses = Place.objects.get(name=houseaddress)
    # except :
    #     houses = None

    # if houses:
    #     print("있는 집")
    #
    #     ReviewForm.objects.create(houseaddress=houseaddress, lat=lat, lng=lng, image=image, floor=floor,
    #                               advantage=advantage, disadvantage=disadvantage, water=water,
    #                               waterplus=waterplus, light=light, lightplus=lightplus, noise=noise,
    #                               noiseplus=noiseplus,
    #                               security=security, securityplus=securityplus, bug=bug, bugplus=bugplus, money=money,
    #                               recommend=recommend)
    # else:
    #     print('없는 새로운 집')
    #     Place.objects.create(name=houseaddress, lat=lat, lng=lng)
    #     ReviewForm.objects.create(houseaddress=houseaddress, lat=lat, lng=lng, image=image, floor=floor, advantage=advantage, disadvantage=disadvantage, water=water,
    #                           waterplus=waterplus, light=light, lightplus=lightplus, noise=noise,
    #                           noiseplus=noiseplus,
    #                           security=security, securityplus=securityplus, bug=bug, bugplus=bugplus, money=money,
    #                           recommend=recommend)

    # context = {
    #     'address': address,
    # }
    # return render(request, 'review/index.html')
    url = reverse('review:map_main')
    return redirect(to=url)

def checkaddress(request):
    #Post
    if request.method == 'POST':
        address = request.POST['address']
        lat = request.POST['lat']
        lng = request.POST['lng']
        place = Place.objects.create(name=address, lat=lat, lng=lng)

        url = reverse('review:createaddress')
        return redirect(to=url)

    elif request.method == 'GET':
        return render(request, 'review/checkaddress.html', context={})


def map_main(request) :
    schools = School.objects.all()

    context = {
        'schools': schools,
    }

    return render(request,'review/mapmain.html',context=context)

def mapchanger(request):
    schoolinput = request.POST.get("schoolinput")
    schools=School.objects.all()
    test=Test.objects.first()
    # print(test.school)
    test.school = schoolinput
    test.save()
    context = {}
    # return render(request, 'review/showhouses.html', context=context)
    return JsonResponse(context)

