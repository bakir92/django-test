from django import forms
from AppTwo.models import UserProfileInfo
from django.core import validators
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ("username","email","password")
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()


class UserProfileInfoForm(forms.ModelForm):
    # password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
