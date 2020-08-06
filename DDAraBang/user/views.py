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
            user = User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["addr"],
                password=request.POST["password1"],
            )
            auth.login(request, user)
            return redirect('signup_complete')
        return render(request, 'signup.html') #실패 시 signup으로 돌아가기
    return render(request, 'signup.html')

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
