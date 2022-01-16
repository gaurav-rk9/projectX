from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def register(request):
	if request.method == "POST" :
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']

		user = User.objects.create_user(username=username,email=email,password=password)
		user.save()

		return redirect("/")

	else:
		return render(request,'register.html')

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if (user):
			auth.login(request,user)
			return redirect("/")
		else:
			messages.error(request,"invalid credentials")
			return redirect("/accounts/login/")
	else:
		return render(request,"login.html")

def logout(request):
	auth.logout(request)
	return redirect("/")