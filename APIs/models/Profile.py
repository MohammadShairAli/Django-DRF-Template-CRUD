from django.db import models

class Profile(models.Model):
    number = models.CharField(max_length=12,null=True,blank=True)
    email = models.EmailField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.email
    