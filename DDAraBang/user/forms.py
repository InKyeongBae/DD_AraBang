from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from community.models import School
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.email_verified == False:
                self.add_error("email", forms.ValidationError("이메일 인증을 완료해야만 로그인이 가능합니다."))
                raise forms.ValidationError("이메일 인증을 완료해야만 로그인이 가능합니다.")
            
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
                raise forms.ValidationError("Password is wrong")
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))
            raise forms.ValidationError("User does not exist")


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "school", "email",)
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email Name"}),
            "school": forms.Select(attrs={"placeholder": "대학교"}),
        }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )

    user_model = get_user_model()
    code = 'invalid'

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def clean_email(self):

        school = self.cleaned_data.get("school")
        email = self.cleaned_data.get("email")
        email_list = school.email_list
        email_confirms = email.split('@')
        email_confirm = email_confirms[1]

        try:
            user = self.user_model.objects.get(email=email)
        except self.user_model.DoesNotExist:
            pass
        else:
            if user.is_active:
                raise ValidationError('이미 회원가입 완료된 이메일 입니다.', code=self.code)

        if email_confirm != email_list:
            raise forms.ValidationError("정확한 학교 이메일을 입력해주세요.")
        else:
            return email

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = models.User
        fields = ['username', 'first_name','last_name']
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "이메일"}),
            "first_name": forms.TextInput(attrs={"placeholder": "이름"}),
            "last_name": forms.TextInput(attrs={"placeholder": "성"}),
        }
