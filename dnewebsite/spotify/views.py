from django.http import response
from django.shortcuts import render
#from requests.models import Response
from .credentials import REDIRECT_URI, CLIENT_ID, CLIENT_SECRET
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from requests import Request, post

class AUTHURL(APIView):
    def get(self,request,format=None):
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'
        url = Request('GET','https://accounts.spotify.com/authorize',params={
            'scope':scopes,
            'response_type':'code',
            'redirect_uri':REDIRECT_URI,
            'client_id':CLIENT_ID,
            }).prepare().url
        return Response({'url':url},status = status.HTTP_200_OK)
    def spotify_callback(request,format=None):
        code = request.GET.get('code')
        error = request.GET.get('error')

        response = post('https://accounts.spotify/api/token',data={
            'grant_type':'authorization_code',
            'client_id':CLIENT_ID,
            'code':code,
            'redirect_uri':REDIRECT_URI,
            'client_secret':CLIENT_SECRET
        }).json()
        access_token = response.get('access_token')
        token_type = response.get('token_type')
        refresh_token = response.get('refresh_token')
        expires_in = response.get('expires_in')
        error = response.get('error')
