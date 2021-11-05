from django.db import models
from PIL import Image 
from django.contrib.auth.models import User 
# Create your models here.

class myProfile(models.Model) :
	user = models.OneToOneField(User, on_delete=models.CASCADE)  # Foreign key with constraint unique values
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')

	def __str__(self):
		return f"{self.user.username } Profile"
 