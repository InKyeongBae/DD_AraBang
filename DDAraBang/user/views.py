from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse, render
from django.contrib.auth import authenticate, login, logout
from . import views
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import CustomUserChangeForm
from . import forms, models
from community.models import School
from user.models import User

class LoginView(FormView):

    template_name = "user/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("user:DDmainpage")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            if user.email_verified == True:
                login(self.request, user)
            # else:
            #     user.delete()
                return redirect(reverse("user:DDmainpage"))

        return super().form_valid(form)

def log_out(request):
    logout(request)
    return redirect(reverse("user:DDmainpage"))


class SignUpView(FormView):

    template_name = "user/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("user:complete_email")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        user.verify_email()
        return super().form_valid(form)

def complete_email(request):
    return render(request, 'user/complete_email.html')

def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
        # to do: add succes message
    except models.User.DoesNotExist:
        # to do: add error message
        pass
    return redirect(reverse("user:DDmainpage"))

def user_update(request):
    if request.method == "POST":
    	# updating
        user_change_form = CustomUserChangeForm(data=request.POST, instance=request.user)
        
        if user_change_form.is_valid():
            user = user_change_form.save()
            return redirect('community:my_page')
    
    else:
        # editting
        user_change_form = CustomUserChangeForm(instance=request.user)

        context = {
            'user_change_form': user_change_form,
        }
        
        return render(request, 'user/user_update.html', context)

def password(request):
    if request.method == "POST":
        password_change_form = PasswordChangeForm(request.user, request.POST)
        
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
        
    else:
        password_change_form = PasswordChangeForm(request.user)
        context = {
            'password_change_form': password_change_form
        }
        
        return render(request, 'user/password.html', context)
       