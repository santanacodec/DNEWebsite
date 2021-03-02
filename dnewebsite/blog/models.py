from django.db import models

# Create your models here.
class blog(models.Model):
    blogAuthor = models.CharField(max_length=30)
    blogContent = models.CharField(max_length=100)