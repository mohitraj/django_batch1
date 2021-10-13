from django.db import models



class Student(models.Model):
	stuid = models.IntegerField()
	stuname = models.CharField(max_length=70)
	stmail = models.EmailField(max_length=70)
	stupass = models.CharField(max_length=70)


	def __str__(self):
		return str(self.stuid)

class Att(models.Model):
	name =  models.CharField(max_length=70)
	time = models.IntegerField()