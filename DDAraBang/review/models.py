from django.db import models
from django.shortcuts import render, redirect, reverse

class Place(models.Model):
    name = models.CharField(max_length=25)
    lat = models.CharField(max_length=25)
    lng = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)