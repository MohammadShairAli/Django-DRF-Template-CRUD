from django.db import models 
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    FirstName = models.CharField(max_length=20, null=False,blank=False)
    LastName = models.CharField(max_length=20, null=False,blank=False)
    password = models.CharField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.OneToOneField("APIs.Profile",on_delete=models.CASCADE,related_name="user",null=True,blank=True,default=None)
    colours = models.ForeignKey("APIs.Colours",on_delete=models.CASCADE,related_name="user",null=True,blank=True)
    courses = models.ManyToManyField("APIs.Courses",related_name="user",blank=True)
    
    USERNAME_FIELD = 'FirstName'

    def __str__(self):
        return f"MR. {self.FirstName} {self.LastName}"