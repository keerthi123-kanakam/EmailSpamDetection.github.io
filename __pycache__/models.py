from django.db import models

# Create your models here.

# Create your models here.
#models.py File



class User(models.Model):
	id = models.AutoField(primary_key=True)
	address= models.TextField()
	firstname= models.CharField(max_length=250)
	password= models.CharField(max_length=250)
	email= models.EmailField(unique=True)
	age= models.IntegerField()
	gender= models.CharField(max_length=250)
	phone= models.CharField(max_length=250)
		   
	   
class Tweets(models.Model):
	id=models.AutoField(primary_key=True)
	stresstweet= models.CharField(max_length=2250)
	subject= models.CharField(max_length=2250)
	fromuser= models.CharField(max_length=2250)
	touser= models.CharField(max_length=2250)
 
class NOtStressTweets(models.Model):
	id=models.AutoField(primary_key=True)
	notstresstweet= models.CharField(max_length=2250)
	subject= models.CharField(max_length=2250)
	fromuser= models.CharField(max_length=2250)
	touser= models.CharField(max_length=2250)
 
class SentItems(models.Model):
	id = models.AutoField(primary_key=True)
	senttweet= models.CharField(max_length=2250)
	subject= models.CharField(max_length=2250)
	fromuser= models.CharField(max_length=2250)
	touser= models.CharField(max_length=2250)
	userid = models.ForeignKey(User, on_delete=models.CASCADE)
 
class Inbox(models.Model):
	id = models.AutoField(primary_key=True)
	tweet= models.CharField(max_length=2250)
	subject= models.CharField(max_length=2250)
	fromuser= models.CharField(max_length=2250)
	touser= models.CharField(max_length=2250)
	userid = models.ForeignKey(User, on_delete=models.CASCADE)
 
class Phishing(models.Model):
	id = models.AutoField(primary_key=True)
	phishingtweet= models.CharField(max_length=2250)
	subject= models.CharField(max_length=2250)
	fromuser= models.CharField(max_length=2250)
	touser= models.CharField(max_length=2250)
	userid = models.ForeignKey(User, on_delete=models.CASCADE)	
 
class Message(models.Model):
	id = models.AutoField(primary_key=True)
	usermessage= models.CharField(max_length=2250)
	adminreply= models.CharField(max_length=2250,default='')
	userid = models.ForeignKey(User, on_delete=models.CASCADE)		  