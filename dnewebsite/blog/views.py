from django.shortcuts import render, HttpResponse
from .models import blog
from .serializers import blogSerializer
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

def blog_list (request):
    if request.method == 'GET':
        blogs = blog.objects.all()
        serializer = blogSerializer(blogs,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = blogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class blogListCreate(generics.ListCreateAPIView):
    queryset = blog.objects.all()
    serializer_class = blogSerializer


# Create your views here.
