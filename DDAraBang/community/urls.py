from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    # 리스트들 
    path('<int:school_list>/', views.community_list, name='community_list'),
    path('<int:school_list>/<int:community_list>/', views.post_list, name='post_list'),
    path('detail/<int:post_id>/', views.post_detail, name='post_detail'),
    # 동작 
    path('<int:my_school>/<int:my_community>/write/', views.post_write, name='write'),
    path('delete/<int:delete>', views.delete, name='delete'),
    path('update/<int:update>', views.update, name='update'),
    # 
    path('my_write/', views.my_write , name='my_write'),
    path('<int:post_id>/like', views.like, name='like'),

    path('my_page/', views.my_page, name='my_page'),

]

