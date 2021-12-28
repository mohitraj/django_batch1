from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date1 = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("post-sp", kwargs={'pk':self.pk})

class Comment(models.Model):
	post = models.ForeignKey('blog1.Post', related_name="comments",on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	create_date = models.DateTimeField(default=timezone.now)
	content = models.TextField()
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True 
		self.save()
# Create your models here.
