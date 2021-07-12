from django.db import models
class SpotifyToken(models.Model):
    user = models.CharField(max_length=50,unique=True)
