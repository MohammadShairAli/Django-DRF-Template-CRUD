from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from APIs.models import User
from APIs.serializers import UserSerializer
import json

# @api_view(['GET','POST','PUT','PATCH','DELETE'])
class Data(APIView):
    def get(self,request):
        id = request.GET.get("id")
        if id :
            Data = User.objects.get(id=id)
            serializer = UserSerializer(Data)
        else:
            Data = User.objects.all()
            serializer = UserSerializer(Data,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = UserSerializer(data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self,request):
        try:
            data = json.loads(request.body)
            id = data["id"]
        except:
            return Response("Missing Data")
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def patch(self,request):
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

    def delete(self,request):
        try:
            data = request.GET
            id = data["id"]
        except Exception as e:
            return Response(str(e))
        user = User.objects.get(id=id)
        user.delete()
        return Response({"message":"User Deleted"})




