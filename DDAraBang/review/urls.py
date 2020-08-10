
from django.conf.urls.static import static

from django.urls import path
from .views import *

app_name = 'review'

urlpatterns = [

    path('createaddress/',createaddress, name='createaddress'),
    path('showhouses/', showhouses, name='showhouses'),
    path('checkaddress/',checkaddress, name='checkaddress'),
    path('main/',map_main,name='map_main'),
    path('mapchanger/',mapchanger,name='mapchanger'),
    path('mappractice/',mappractice,name='map'),
    path('practice/',practice,name='practice'),
]