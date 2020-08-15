"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import settings
from . import views as config_views
from django.conf.urls.static import static
from community import views 

app_name = 'config'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', config_views.main_html , name='DDmainpage'), #community views의 main_html 함수 호출 
    path('review/',include('review.urls',namespace='review')),
    path('community/', include('community.urls',namespace='community')),
    path('user/', include('user.urls')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)