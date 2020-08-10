from django.shortcuts import render, redirect, reverse
import json
import requests
import time

from django.views.decorators.http import require_POST

from .models import *
from django.http import JsonResponse


# Create your views here.

def showhouses(request):
    places = Place.objects.all()
    schools = School.objects.all()
    test = Test.objects.first()
    data = {
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

    return render(request,'review/practice.html',context=context)

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


def mappractice(request) :
    return render(request,'review/main.html',context={})

def practice(request) :
    return render(request,'review/practice.html',context={})