from django.shortcuts import render
from django.http import HttpResponse
import http.client

conn = http.client.HTTPSConnection("instagram47.p.rapidapi.com")

headers = { 'x-rapidapi-host': "instagram47.p.rapidapi.com" }

conn.request("GET", "/post_comments?postid=2435143128484144113", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
# Create your views here.
def Index(request):
    return HttpResponse(data.decode("utf-8"))
