<<<<<<< Updated upstream
from django.conf.urls.static import static
=======

>>>>>>> Stashed changes
from django.urls import path
from .views import *

app_name = 'review'

urlpatterns = [
<<<<<<< Updated upstream
    path('createaddress/',createaddress, name='createaddress'),
    path('showhouses/', showhouses, name='showhouses'),
    path('checkaddress/',checkaddress, name='checkaddress'),
=======
    path('main/',map_main,name='map_main'),
>>>>>>> Stashed changes
]