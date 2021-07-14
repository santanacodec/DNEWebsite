from django.db import models

# Create your models here.
class blog(models.Model):
    blogAuthor = models.CharField(max_length=30)
    blogContent = models.CharField(max_length=100)
    blogDTF = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    