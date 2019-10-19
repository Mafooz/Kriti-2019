from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
	first_name=forms.CharField(widget=forms.TextInput(),max_length=200,label='First name')
	last_name=forms.CharField(widget=forms.TextInput(),max_length=200,label='Last name')
	email=forms.CharField(widget=forms.EmailInput(),max_length=200,label='Email Address')
	class Meta:
		model=User
		fields=('username','first_name','last_name','email','password1','password2')