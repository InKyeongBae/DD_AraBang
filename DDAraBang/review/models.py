from django.db import models
from django.shortcuts import render, redirect, reverse

class Place(models.Model):
    name = models.CharField(max_length=25)
    lat = models.CharField(max_length=25)
    lng = models.CharField(max_length=25)

    def __str__(self):
        return '{}'.format(self.name)

class School(models.Model):
    name = models.CharField(max_length=25)
    lat = models.CharField(max_length=25)
    lng = models.CharField(max_length=25)
    gu = models.CharField(max_length=25)

    def __str__(self):
        return '{}'.format(self.name)

class Test(models.Model):
    school = models.CharField(max_length=25)

    def __str__(self):
        return '{}'.format(self.school)