from django.shortcuts import render
#from requests.models import Response
from .credentials import REDIRECT_URI, CLIENT_ID, CLIENT_SECRET
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from requests import Request, post

class AUTHURL(APIView):
    def get(self,request,format="none"):
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'
        url = Request('GET','https://accounts.spotify.com/authorize',params={
            'scope':scopes,
            'response_type':'code',
            'redirect_uri':REDIRECT_URI,
            'client_id':CLIENT_ID,
            }).prepare().url
        return Response({'url':url},status = status.HTTP_200_OK)
