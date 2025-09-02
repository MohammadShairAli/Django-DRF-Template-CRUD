from django.urls import path
from .views import Data,Color,UserProfile, Course


urlpatterns = [
    path("Data/",Data),
    path("Color/",Color),
    # path("Profile/",UserProfile),
    path("Course/",Course),
]
