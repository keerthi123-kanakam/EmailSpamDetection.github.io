from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def adminHome(request):
	return render(request, 'adminlogin.html')
def adminLogin(request):	
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username == "admin" and password == "admin":
			return redirect('adminHomePage')
	return render(request,'adminlogin.html')
def adminHomePage(request):
	return render(request, 'adminhomepage.html')	