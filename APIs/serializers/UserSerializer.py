from rest_framework import serializers
from APIs.models import User, Profile
from .UserProfileSerializer import UserProfileSerializer
from .ColorSerializer import ColorSerializer
from .CoursesSerializer import CoursesSerializer

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    colours = ColorSerializer()
    courses = CoursesSerializer(many=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ["last_login","created_at"]
    


    def validate(self, data):
        # password = data.get('password')
        # if len(password) < 10:
        #     raise serializers.ValidationError("Password should'nt be longer than 10")
        
        return data
    
    def create(self, data):
        profileData = data.pop("profile")
        profile = Profile.objects.create(**profileData)
        user = User.objects.create(profile=profile,**data)
        return user
    
    def update(self, instance, data):
        courses = data.pop("courses",None)
        if courses:
            CoursesDataSerializer = CoursesSerializer(instance.courses, data = courses, partial=True)
            if CoursesDataSerializer.is_valid(raise_exception=True):
                CoursesDataSerializer.save()
        
        ColourData = data.pop("colours",None)
        if ColourData:
            colourDataSerializer = ColorSerializer(instance.colours,data = ColourData,partial=True)
            if colourDataSerializer.is_valid(raise_exception=True):
                colourDataSerializer.save()

        profileData = data.pop("profile",None)
        if profileData:
            profileDataSerializer = UserProfileSerializer(instance.profile, data=profileData, partial=True)
            if profileDataSerializer.is_valid(raise_exception=True):
                profileDataSerializer.save()

        for key,value in data.items():
            setattr(instance,key,value)
        instance.save()
        return instance
    



        

