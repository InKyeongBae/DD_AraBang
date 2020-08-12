<<<<<<< HEAD
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import views
from . import forms

class LoginView(FormView):

    template_name = "user/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("user:DDmainpage")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

def log_out(request):
    logout(request)
    return redirect(reverse("user:DDmainpage"))

class SignUpView(FormView):

    template_name = "user/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("user:DDmainpage")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
=======
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

#home 메인화면
def home(request):
    return render(request, 'home.html')


#회원가입&자동로그인
def signup(request):
    if request.method == 'POST':
        if request.POST["password1"] == request.POST["password2"]:
            username = request.POST["username"]  #이메일 @ 앞부분(로그인할 때 id로 사용)
            addr = request.POST["addr"]  #이메일 @ 뒷부분
            addr = str(username).replace("'", "").replace("(", "").replace(")", "").replace(",", "") + "@" + str(
                addr).replace("'", "").replace("(", "").replace(")", "").replace(",", "")
            email = request.POST.get('email', False)

            if request.POST.get('email', False) == addr:
                print(email)
                user = User.objects.create_user(
                    username=request.POST["username"],  # 이메일 @ 앞부분(로그인할 때 id로 사용)
                    email=request.POST.get('email', False),  # 전체 이메일
                    password=request.POST["password1"],  # 비밀번호
                )
                auth.login(request, user)
            return redirect('signup_complete')
        return render(request, 'signup.html')    #실패 시 signup으로 돌아가기
    return render(request, 'signup.html')


#-------------------------------------------------------------------------------------------------------------------
def signup_complete(request):
    return render(request, 'signup_complete.html')


#로그인
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home') #로그인 계정이 없을 때 home화면으로 이동
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'login.html')

#로그아웃
def logout(request):
    auth.logout(request)
    return redirect('home')


#마이페이지
def mypage(request):
    return render(request, 'mypage.html')
>>>>>>> yurim
