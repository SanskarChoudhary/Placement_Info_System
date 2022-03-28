from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile

class userRegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    enrollment_no=forms.CharField(max_length=12,min_length=12)
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['first_name','last_name','username','enrollment_no','email']

class userUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['first_name','last_name','email']

class userProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['image']
