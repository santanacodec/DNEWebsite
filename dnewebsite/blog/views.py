from django.shortcuts import render, HttpResponse
from .models import blog
from .serializers import blogSerializer
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET','POST'])
def blog_list (request):
    if request.method == 'GET':
        blogs = blog.objects.all()
        serializer = blogSerializer(blogs,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = blogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class blogListCreate(generics.ListCreateAPIView):
    queryset = blog.objects.all()
    serializer_class = blogSerializer

@api_view(['GET','PUT','DELETE'])
def blogDetails(request,pk):
    try:
        Blog = blog.objects.get(pk=pk)
    except blog.DoesNotExsist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = blogSerializer(Blog)
        return Response(serializer.data)
    elif request.method =='PUT':

        serializer = blogSerializer(Blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method =='DELETE':
        Blog.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
