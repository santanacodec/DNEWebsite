from django.urls import path
from .views import AUTHURL


urlpatterns = [
    path('spot',AUTHURL.as_view()), #this gets added to main urls
]