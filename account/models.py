from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
# Create your models here.









class AccountUser(AbstractUser):

	
	email=models.EmailField(verbose_name="Email Address",unique=True)
	like_color = models.CharField(max_length=120,blank=False,null=False,default="ui red")
	
	
	def clean_email(self):
		email=self.email.casefold()
		return email.islower()
		
	
	USERNAME_FIELD="email"
	REQUIRED_FIELDS=['first_name','last_name','username']
	