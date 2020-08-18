
from django.conf.urls.static import static

from django.urls import path

from config import settings
from .views import *

app_name = 'review'

urlpatterns = [

    path('createaddress/',createaddress, name='createaddress'),
    path('showhouses/', showhouses, name='showhouses'),
    path('main/',map_main,name='map_main'),
    path('mapchanger/',mapchanger,name='mapchanger'),
    path('schoolupload/',school_upload,name='school_upload'),
    path('homedetail/<int:pk>/',homedetail,name='homedetail'),
    path('homeupdate/<int:pk>/',homeupdate,name='homeupdate'),
    path('homedelete/<int:pk>/',homedelete,name='homedelete'),
    path('myreview/',myreview,name='myreview'),

]