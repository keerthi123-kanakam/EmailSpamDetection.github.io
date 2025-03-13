from django.shortcuts import render,redirect
from django.http import HttpResponse
from request1.models import User,Tweets,NOtStressTweets,Message
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
'''def viewUser(request):
	user_list = User.objects.all()
	print(user_list)
	postdetailslist = {
				"postretrieveobject": user_list
				}
	return render(request, 'viewuser.html',postdetailslist)'''
def show(request):	
	employees = User.objects.all()	
	return render(request,"viewuser.html",{'employees':employees})	
	
def showTweets(request):  
	tweets = Tweets.objects.all()  
	return render(request,"viewtweets.html",{'tweets':tweets})	
def showNotStressTweets(request):  
	notstresstweets = NOtStressTweets.objects.all()	 
	return render(request,"viewnotstresstweets.html",{'notstresstweets':notstresstweets})	
def stressGraph(request):
	return render(request,"chart_page.html")
def notStressGraph(request):
	return render(request,"chart_page1.html")	
def adminmessage(request):
	msg = Message.objects.all() 
	return render(request,'adminreply.html',{'msg':msg})   
def adminmessagehtml(request,id,userid):
	request.session['id'] = id
	request.session['userid'] = userid
	#
	return render(request,'adminrpl.html')
def adminmessagesave(request):
	if request.method == 'POST':
		adminmessage = request.POST.get('adminmessage')	   
		id = request.session['id']
		userid = request.session['userid']
		Message.objects.filter(id=id).update(adminreply=adminmessage)
		return redirect('adminHomePage')