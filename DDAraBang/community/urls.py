from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [

    path('<int:pk_1>/', views.community_list, name='community_list'),
    path('<int:pk_1>/<int:pk>/', views.post_list, name='post_list'),
    path('<int:pk_1>/<int:pk>/<int:pk_3>/', views.post_detail),
    path('<int:pk_1>/<int:pk>/write/', views.post_write, name='write'),
    path('<int:pk_1>/<int:pk>/<int:pk_3>/delete/', views.delete, name='delete'),

]

