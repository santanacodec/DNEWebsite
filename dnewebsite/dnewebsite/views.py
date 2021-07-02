from django.shortcuts import render
from django.http import HttpResponse
from blog.models import blog

# Create your views here.
def Indexx(request):
    return HttpResponse("It is working")
def makeBlog(request):
    return HttpResponse()
