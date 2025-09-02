from rest_framework.response import Response
from rest_framework.decorators import api_view
from APIs.models import Courses
from APIs.serializers import CoursesSerializer
import json

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def Course(request):
    if request.method == "GET":
        id = request.GET.get("id")
        if id :
            Data = Courses.objects.get(id=id)
            serializer = CoursesSerializer(Data)
        else:
            Data = Courses.objects.all()
            serializer = CoursesSerializer(Data,many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = CoursesSerializer(data = request.data)
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
        course = Courses.objects.get(id=id)
        serializer = CoursesSerializer(course, data=data)
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
        courses = Courses.objects.get(id=id)
        courses.delete()
        return Response({"message":"Courses Deleted"})


