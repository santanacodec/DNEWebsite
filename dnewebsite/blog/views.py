from django.shortcuts import render
from .models import blog
from .serializers import blogSerializer
from rest_framework import generics

class blogListCreate(generics.ListCreateAPIView):
    queryset = blog.objects.all()
    serializer_class = blogSerializer


# Create your views here.
