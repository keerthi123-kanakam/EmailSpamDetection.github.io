from django.db import models

# Create your models here.
class Student(models.Model):
	id=models.CharField(max_length=250, primary_key=True)
	name= models.CharField(max_length=250)
	address= models.TextField()
	dob=models.DateTimeField()
	
	def __str__(self):
		return self.title+'	 '+self.content	
		
		