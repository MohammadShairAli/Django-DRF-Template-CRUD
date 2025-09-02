from django.db import models 


class Courses(models.Model):
    CourseName = models.CharField(max_length=10, null=False,blank=False)


    def __str__(self):
        return self.CourseName