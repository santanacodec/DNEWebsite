from django.db import models
from blog.models import blog

# Create your models here.
class commentModel(models.Model):
    comment = models.CharField(max_length=150)
    blogId = models.IntegerField()
    commentAuthor = models.CharField(max_length=150,default='anonymous')
    commentDTF = models.DateTimeField(auto_now_add=True)