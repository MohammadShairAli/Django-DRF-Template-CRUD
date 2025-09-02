from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from APIs.models import User
from APIs.serializers import UserSerializer
import json

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def Data(request):
    if request.method == "GET":
        id = request.GET.get("id")
        if id :
            Data = User.objects.get(id=id)
            serializer = UserSerializer(Data)
        else:
            Data = User.objects.all()
            serializer = UserSerializer(Data,many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            print(data)
            id = data["id"]
        except:
            return Response("Missing Data")
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        try:
            data = json.loads(request.body)
            id = data['id']
            print(id)
        except:
            return Response("Missing fields")
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data = data, partial=True)
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
        user = User.objects.get(id=id)
        user.delete()
        return Response({"message":"User Deleted"})




