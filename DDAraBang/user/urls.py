from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signup_complete/', views.signup_complete, name='signup_complete'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
