from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import User,SentItems,Inbox,Phishing,Message
from .models import Tweets
from .models import NOtStressTweets
#######testing starts here
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
## Add these lines to turn off the warnings
import warnings
from django.db.models import Q, Count
##testing
from genetic_selection import GeneticSelectionCV
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import itertools
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.linear_model import PassiveAggressiveClassifier
import os

import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
warnings.filterwarnings("ignore")	
#cnn imports
		
######testing ends here
# Create your views here.
def home(request):
	return render(request, 'index.html')
def post_new(request):
	form = PostForm()
	return render(request, 'post_edit.html', {'form': form})
def registration(request):
	if request.method == "POST":
		print('hello123')
		form = PostForm(request.POST)
		print('hello123')
		if form.is_valid():
			print('hello1234')
			user = form.save()
			#user.refresh_from_db()	# load the profile instance created by the signal
			user.save()
			#raw_password = form.cleaned_data.get('password1')
			#user = authenticate(username=user.username, password=raw_password)
			return redirect('home')
	else:
		print('hi123')
		form = PostForm()
	return render(request, 'post_edit.html', {'form': form})
def userLoginCheck(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		request.session['username'] = username
		print(username)
		print(password)
		try:
			user_object = User.objects.get(email=username,password=password)
			request.session['userid']=user_object.id
			print(user_object)
		except:
			#user_object = None
			print('hello')
		if user_object is not None:
			print('hiiiiiiii')
			request.session['useremail'] = user_object.email
			return redirect('userHome')
			print('hiiiiiiii')
	return render(request,'userlogin.html',)	
def userHome(request):
	return render(request, 'userhome.html')	
def tweet(request):
	if request.method == 'POST':
		tweetmsg = request.POST.get('tweetmsg')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		input=[tweetmsg]
		username = request.session['username']
		userid = request.session['userid']
		fromuseremail = request.session['useremail']
		user_objectsender = User.objects.get(email=username)
		senderid1=user_objectsender.id
		senderid=User.objects.get(pk=senderid1)
		print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
		print(senderid)
		#df =pd.read_excel("E:/Stress Based on Social Interaction on social network/dataset/stress1.xlsx")
		user_object = User.objects.get(email=email)
		recieverid1=user_object.id
		recieverid=User.objects.get(pk=recieverid1)
		#cnn import
		if user_object is not None:
			import numpy as np # linear algebra
			import pandas as pd1 # data processing, CSV file I/O (e.g. pd.read_csv)
			df =pd.read_excel("C:/Users/supraja/Documents/SPAM/phishing email detectionnew1/sample2/sample1/phishing.xlsx")
			y = df.target
			X = df.text
			print(X.shape)
			print(y.shape)
			X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
			tfidf_vect = TfidfVectorizer(stop_words = 'english')
			tfidf_train = tfidf_vect.fit_transform(X_train)
			tfidf_test = tfidf_vect.transform(X_test)
			tfidf_test1= tfidf_vect.transform(input)
			tfidf_df = pd.DataFrame(tfidf_train.A, columns=tfidf_vect.get_feature_names())
			linear_clf = PassiveAggressiveClassifier()
			linear_clf.fit(tfidf_train, y_train)
			pred = linear_clf.predict(tfidf_test)
			pred1 = linear_clf.predict(tfidf_test1)
			print(pred1)
			score = metrics.accuracy_score(y_test, pred)
			print("accuracy:   %0.3f" % score)
			print(tweetmsg)
			stress=''
			if pred1==0:
				stress='Stressed Tweet'
				request.session['tweetmsg'] = tweetmsg
				tweets=Tweets()
				tweets.stresstweet= request.POST.get('tweetmsg')
				tweets.subject= request.POST.get('subject')
				tweets.touser= request.POST.get('email')
				tweets.fromuser= username
				tweets.save()
				#######################
				sentitems=SentItems()
				sentitems.senttweet=request.POST.get('tweetmsg')
				sentitems.subject=request.POST.get('subject')
				sentitems.fromuser=fromuseremail
				sentitems.touser=request.POST.get('email')
				sentitems.userid=senderid
				sentitems.save()
				#inbox
				inbox=Inbox()
				inbox.tweet=request.POST.get('tweetmsg')
				inbox.subject=request.POST.get('subject')
				inbox.fromuser=fromuseremail
				inbox.touser=request.POST.get('email')
				inbox.userid=recieverid
				inbox.save()
				#phishing email
				phishing=Phishing()
				phishing.phishingtweet=request.POST.get('tweetmsg')
				phishing.subject=request.POST.get('subject')
				phishing.fromuser=fromuseremail
				phishing.touser=request.POST.get('email')
				phishing.userid=recieverid
				phishing.save()
				
				#########################
				tweets = Tweets.objects.all()
				#.objects.last()
				d = {'e':stress}
				return render(request,'displaystress.html',{'tweets':tweets})
			elif pred1==1:
				stress='not Stressed Tweet'
				request.session['tweetmsg'] = tweetmsg
				notstresstweets=NOtStressTweets()
				notstresstweets.notstresstweet= request.POST.get('tweetmsg')
				notstresstweets.subject= request.POST.get('subject')
				notstresstweets.touser= request.POST.get('email')
				notstresstweets.fromuser= username
				notstresstweets.save()
				#######################
				sentitems=SentItems()
				sentitems.senttweet=request.POST.get('tweetmsg')
				sentitems.subject=request.POST.get('subject')
				sentitems.fromuser=fromuseremail
				sentitems.touser=request.POST.get('email')
				sentitems.userid=senderid
				sentitems.save()
				#inbox
				inbox=Inbox()
				inbox.tweet=request.POST.get('tweetmsg')
				inbox.subject=request.POST.get('subject')
				inbox.fromuser=fromuseremail
				inbox.touser=request.POST.get('email')
				inbox.userid=recieverid
				inbox.save()
				#########################
				notstresstweets = NOtStressTweets.objects.all()
				d = {'e':stress}
				return render(request,'displaynonstress.html',{'notstresstweets':notstresstweets})
			
			#print(pred2)
			#print(predictions)
			#print(predictions1)
					
			######testing ends here
	
	return render(request,'chart_page.html',)
def chart_page(request,chart_type):
	chart = Tweets.objects.values('id').annotate(dcount=Count('stresstweet'))
	return render(request,'chart_page.html',{'chart_type':chart_type,'objects':chart})
def chart_page1(request,chart_type):
	chart = NOtStressTweets.objects.values('id').annotate(dcount=Count('notstresstweet'))
	return render(request,'chart_page1.html',{'chart_type':chart_type,'objects':chart})	
def sentitems(request):
	username = request.session['username']
	user_objectsender = User.objects.get(email=username)
	senderid1=user_objectsender.id
	sentitems = SentItems.objects.filter(userid=senderid1)
	return render(request,'sentitems.html',{'sentitems':sentitems})
def inbox(request):
	username = request.session['username']
	user_objectsender = User.objects.get(email=username)
	senderid1=user_objectsender.id
	inbox = Inbox.objects.filter(userid=senderid1)
	return render(request,'inbox.html',{'inbox':inbox})
def phishingtweet(request):
	username = request.session['username']
	user_objectsender = User.objects.get(email=username)
	senderid1=user_objectsender.id
	phishing = Phishing.objects.filter(userid=senderid1)
	return render(request,'phishing.html',{'phishing':phishing})
def usermessage(request):
	return render(request,'usermessage.html')
def usermessagesave(request):
	if request.method == 'POST':
		usermessage = request.POST.get('usermessage')
		username = request.session['username']
		user_objectsender = User.objects.get(email=username)
		senderid1=user_objectsender.id
		senderid=User.objects.get(pk=senderid1)
		usermessage=Message()
		usermessage.usermessage=request.POST.get('usermessage')
		usermessage.userid=senderid
		usermessage.save()
		return redirect('userHome')
	return HttpResponse('unsuccess')
def adminmessagereply(request):
	username = request.session['username']
	user_objectsender = User.objects.get(email=username)
	senderid1=user_objectsender.id
	senderid=User.objects.get(pk=senderid1)	   
	replymsg = Message.objects.filter(userid=senderid) 
	return render(request,'adminreplymessage.html',{'replymsg':replymsg})	
def nb(request):
	import numpy as np # linear algebra
	import pandas as pd1 # data processing, CSV file I/O (e.g. pd.read_csv)
	import matplotlib.pyplot as plt
	from sklearn.model_selection import train_test_split
	from sklearn.feature_extraction.text import TfidfVectorizer
	import itertools
	from sklearn.naive_bayes import MultinomialNB
	from sklearn import metrics
	from sklearn.linear_model import PassiveAggressiveClassifier
	import os
	from sklearn import datasets, linear_model
	import seaborn as sns
	from sklearn.linear_model import LogisticRegression
	from sklearn.svm import SVC
	from sklearn.tree import DecisionTreeClassifier
	from sklearn.neighbors import KNeighborsClassifier
	from sklearn.model_selection import train_test_split
	from sklearn.metrics import confusion_matrix
	df =pd.read_excel("C:/Users/supraja/Documents/SPAM/phishing email detectionnew1/sample2/sample1/phishing.xlsx")
	y = df.target
	X = df.text
	print(X.shape)
	print(y.shape)
	X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
	tfidf_vect = TfidfVectorizer(stop_words = 'english')
	tfidf_train = tfidf_vect.fit_transform(X_train)
	tfidf_test = tfidf_vect.transform(X_test)
	tfidf_df = pd.DataFrame(tfidf_train.A, columns=tfidf_vect.get_feature_names())
	estimator = linear_model.LogisticRegression(solver="liblinear", multi_class="ovr") 
	linear_clf = GeneticSelectionCV(estimator,
									cv=5,
									verbose=1,
									scoring="accuracy",
									max_features=10,
									n_population=50,
									crossover_proba=0.5,
									mutation_proba=0.2,
									n_generations=200,
									crossover_independent_proba=0.5,
									mutation_independent_proba=0.05,
									tournament_size=3,
									n_gen_no_change=10,
									caching=True,
									n_jobs=-1)
	linear_clf.fit(tfidf_train, y_train)
	pred = linear_clf.predict(tfidf_test)
	score = metrics.accuracy_score(y_test, pred)
	print("accuracy:   %0.3f" % score)
	return render(request,'accuracy.html',{'replymsg':score})
def svc(request):
	import numpy as np # linear algebra
	import pandas as pd1 # data processing, CSV file I/O (e.g. pd.read_csv)
	import matplotlib.pyplot as plt
	from sklearn.model_selection import train_test_split
	from sklearn.feature_extraction.text import TfidfVectorizer
	import itertools
	from sklearn.naive_bayes import MultinomialNB
	from sklearn import metrics
	from sklearn.linear_model import PassiveAggressiveClassifier
	import os

	import seaborn as sns
	from sklearn.linear_model import LogisticRegression
	from sklearn.svm import SVC
	from sklearn.tree import DecisionTreeClassifier
	from sklearn.neighbors import KNeighborsClassifier
	from sklearn.model_selection import train_test_split
	from sklearn.metrics import confusion_matrix

	df =pd.read_excel("C:/Users/supraja/Documents/SPAM/phishing email detectionnew1/sample2/sample1/phishing.xlsx")
	y = df.target
	X = df.text
	print(X.shape)
	print(y.shape)
	X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
	tfidf_vect = TfidfVectorizer(stop_words = 'english')
	tfidf_train = tfidf_vect.fit_transform(X_train)
	tfidf_test = tfidf_vect.transform(X_test)
	tfidf_test1= tfidf_vect.transform(input)
	tfidf_df = pd.DataFrame(tfidf_train.A, columns=tfidf_vect.get_feature_names())
	linear_clf = SVC()
	linear_clf.fit(tfidf_train, y_train)
	pred = linear_clf.predict(tfidf_test)
	pred1 = linear_clf.predict(tfidf_test1)
	print(pred1)
	score = metrics.accuracy_score(y_test, pred)
	print("accuracy:   %0.3f" % score)	
	return render(request,'accuracy.html',{'replymsg':score})	
	
def new_job(request,id):	
	#emp = Employee.objects.filter(id=request.id)
	emp1 = Employee.objects.get(id=id)
	html = "<html><table border='2'><tr><td>"+emp1.id+"</td><td>"+emp1.name+"</td><td>"+emp1.address+"</td></table></body></html>"
	postdetailslist = {
	"postretrieveobject": emp1
				}
	print(emp1)
				#return render(request, 'retrieve.html',postdetailslist) 
				#return render(request, 'bootstrapretrieve.html',postdetailslist) 
	#return render(request, 'retrieve.html',postdetailslist) 
	return HttpResponse(html)
def	retrieveEmployee(self):
	employee_list = Employee.objects.all()
	print(employee_list)
	return HttpResponse(employee_list)
	
def retrieveSingleRecord(self):
		emprec=Employee.objects.get(id=1)
		print(emprec)
		return HttpResponse(emprec)
def updateRecord(self):
		#emprec=Employee.objects.get(id=1)
		#emprec.id = '29'
		#emprec.save()
		emprec=Employee.objects.filter(id=7).update(name="ram")
		print(emprec)
		return HttpResponse(emprec)	
def employee(self):
	employee = Employee.objects.create(id='8',name='sriram',address='hyderabad')
	#employee.save()
	return HttpResponse(employee)
def employeeFilterMethod(self):
	employee=Employee.objects.filter(address='hyderabad')
	return HttpResponse(employee)
def employeeOB(self):
	employee=Employee.objects.order_by('-id')
	return HttpResponse(employee)
def employeefiltOB(self):
	#employee=Employee.objects.order_by('-id')
	employee=Employee.objects.filter(name="sri").order_by("id")
	return HttpResponse(employee)	
def delet(self):
	delet=Employee.objects.filter(address='secunderabad').delete()
	return HttpResponse(delet)
		