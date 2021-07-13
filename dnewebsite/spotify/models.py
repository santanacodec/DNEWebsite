from django.db import models
class SpotifyToken(models.Model):
    user = models.CharField(max_length=50,unique=True)
    created_at = models.DateField(auto_now_add=True)
    refresh_token = models.CharField(max_length=150)
