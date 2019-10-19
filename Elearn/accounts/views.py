from django.shortcuts import render,redirect
from accounts.forms import SignupForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def signup(request):
	form=SignupForm(request.POST)
	if form.is_valid():
		user=form.save(commit=False)
		user.first_name=form.cleaned_data.get('first_name')
		user.last_name=form.cleaned_data.get('last_name')
		user.save()
		auth_login(request,user)
		return redirect('home')
	else:
		form=SignupForm()
	return render(request,'signup.html',{'form':form})
def home(request):
	return render(request,'home.html')