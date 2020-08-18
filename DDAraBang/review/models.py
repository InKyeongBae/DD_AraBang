from django.db import models
from django.shortcuts import render, redirect, reverse
from user.models import User

class Place(models.Model):
    name = models.CharField(max_length=50)
    lat = models.CharField(max_length=25)
    lng = models.CharField(max_length=25)
    gu = models.CharField(max_length=25,default=1)

    def __str__(self):
        return '{}'.format(self.name)

class School(models.Model):
    name = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    gu = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)

class Test(models.Model):
    school = models.CharField(max_length=25)

    def __str__(self):
        return '{}'.format(self.school)


class ReviewForm(models.Model):
    # houseaddress = models.CharField(max_length=100, default=1)
    # lat = models.CharField(max_length=25, default=1)
    # lng = models.CharField(max_length=25, default=1)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    place = models.ForeignKey(Place,on_delete=models.CASCADE,related_name='reviews')

    image = models.ImageField(upload_to='gallery',null=True,blank=True)

    floor = models.CharField(max_length=20)

    advantage = models.TextField(help_text='자신이 생각하는 이 집의 장점을 써주세요.')
    disadvantage = models.TextField(help_text='자신이 생각하는 이 집의 단점을 써주세요.')

    water = models.CharField(max_length=20)
    waterplus = models.CharField(max_length=50,help_text='추가로 하시고 싶으신 말이 있다면 적어주세요!',blank=True,null=True)

    light = models.CharField(max_length=20)
    lightplus = models.CharField(max_length=50, help_text='추가로 하시고 싶으신 말이 있다면 적어주세요!',blank=True,null=True)

    noise = models.CharField(max_length=20)
    noiseplus = models.CharField(max_length=50, help_text='추가로 하시고 싶으신 말이 있다면 적어주세요!',blank=True,null=True)

    security = models.CharField(max_length=20)
    securityplus = models.CharField(max_length=50, help_text='추가로 하시고 싶으신 말이 있다면 적어주세요!',blank=True,null=True)

    bug = models.CharField(max_length=20)
    bugplus = models.CharField(max_length=50, help_text='추가로 하시고 싶으신 말이 있다면 적어주세요!',blank=True,null=True)

    money = models.CharField(max_length=50, help_text='ex)월세에 관리비 따로 5만원 정도 더 나오니 계약할 때 꼭 깎아달라고 하세요!',blank=True,null=True)

    recommend = models.CharField(max_length=20)

    rating = models.IntegerField(default=0)