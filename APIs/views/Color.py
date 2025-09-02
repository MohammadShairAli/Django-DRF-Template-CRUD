from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from APIs.models import Colours
from APIs.serializers import ColorSerializer
import json

@api_view(['GET','POST','PUT','DELETE'])
def Color(request):
    if request.method == "GET":
        id = request.GET.get("id")
        if id :
            Data = Colours.objects.get(id=id)
            serializer = ColorSerializer(Data)
        else:
            Data = Colours.objects.all()
            serializer = ColorSerializer(Data,many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ColorSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
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
        user = Colours.objects.get(id=id)
        serializer = ColorSerializer(user, data=data)
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
        user = Colours.objects.get(id=id)
        user.delete()
        return Response({"message":"User Deleted"})

    
