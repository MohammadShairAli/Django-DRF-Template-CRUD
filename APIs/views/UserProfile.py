from rest_framework.response import Response
from rest_framework.decorators import api_view
from APIs.models import Profile
from APIs.serializers import UserProfileSerializer
import json

@api_view(['GET','POST','PUT','DELETE'])
def UserProfile(request):
    if request.method == "GET":
        id = request.GET.get("id")
        if id :
            Data = Profile.objects.get(id=id)
            serializer = UserProfileSerializer(Data)
        else:
            Data = Profile.objects.all()
            serializer = UserProfileSerializer(Data,many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = UserProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            id = data["id"]
        except:
            return Response("Missing Data")
        user = Profile.objects.get(id=id)
        serializer = UserProfileSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        try:
            data = request.GET
            id = data["id"]
        except Exception as e:
            return Response(str(e))
        user = Profile.objects.get(id=id)
        user.delete()
        return Response({"message":"User Deleted"})

    
