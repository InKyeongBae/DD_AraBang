from django.urls import path
from . import views
from config import views as config_views

app_name = 'community'

urlpatterns = [

    path('', config_views.main_html, name='DDmainpage'),
    # 리스트들 
    path('<int:school_list>/', views.community_list, name='community_list'),
    
    # 전체 커뮤니티와 연결 
    path('all/', views.all_community_list, name='all_community_list'),
 
    # 학교 커뮤니타와 연결 
    path('<int:school_list>/<int:community_list>/', views.post_list, name='post_list'),
    path('detail/<int:post_id>/', views.post_detail, name='post_detail'),
    

    #전체 커뮤니티와 연결
    path('all/<int:all_community_list>/', views.all_post_list, name='all_post_list'),
    path('all_detail/<int:post_id>/', views.all_post_detail, name='all_post_detail'),

    # 나의 학교 페이지 동작 
    path('<int:my_school>/<int:my_community>/write/', views.post_write, name='write'),
    path('delete/<int:delete>', views.delete, name='delete'),
    path('update/<int:update>', views.update, name='update'),
    

    # 전체 페이지 동작 
    path('<int:all_my_community>/write/', views.all_post_write, name='all_write'),
    path('all_delete/<int:delete>', views.all_delete, name='all_delete'),
    path('all_update/<int:update>', views.all_update, name='all_update'),
    
    #내가 쓴 글 확인 
    path('my_write/', views.my_write , name='my_write'),

    #좋아요
    path('<int:post_id>/like', views.like, name='like'),
    path('<int:post_id>/all_like', views.all_like, name='all_like'),

    #마이페이지
    path('my_page/', views.my_page, name='my_page'),
    path('comment/', views.post_detail , name="comment"),
    path('comment_update/<int:comment_id>', views.comment_update, name='comment_update'),   
    path('comment_delete/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('post_like/', views.post_i_like, name='post_i_like'),

    path('schoolupload/',views.school_upload,name='school_upload'),
    path('user_delete/', views.user_delete, name='user_delete'),
    path('post_search/',views.post_search,name='post_search'), #관련해서 물어보실거있으면 지영에게
    path('post_search_all/',views.post_search_all, name='post_search_all'),
    path('new_comment_update/',views.new_comment_update, name='new_comment_update'), #관련해서 물어보실거있으면 지영에게
]