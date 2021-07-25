from django.db import models

class Student(models.Model):
	stuid = models.IntegerField()
	stuname = models.CharField(max_length=70)
	stmail = models.EmailField(max_length=70)
	stupass = models.CharField(max_length=70)
# Create your models here.
