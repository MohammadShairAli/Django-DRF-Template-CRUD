from django.urls import path
from .views import Data,Color,UserProfile, Course


urlpatterns = [
    path("Data/",Data.as_view()),
    path("Color/",Color.as_view()),
    # path("Profile/",UserProfile),
    path("Course/",Course),
]
