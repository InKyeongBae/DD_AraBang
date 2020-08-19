from django.urls import path
from . import views
from config import views as config_views

app_name = "user"


urlpatterns = [
    path('', config_views.main_html , name='DDmainpage'), #community views의 main_html 함수 호출 
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.log_out, name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path('user_update/', views.user_update, name='user_update'),
    path('password/', views.password, name='password'),
    path('complete_email/', views.complete_email, name='complete_email'),
    path("verify/<str:key>", views.complete_verification, name="complete-verification"),
]