from rest_framework import serializers
from .models import blog

class blogSerializer2(serializers.Serializer): #This is the bad way
    blogAuthor = serializers.CharField(max_length=30)
    blogContent = serializers.CharField(max_length=100)

    def create(self,validated_data):
        return blog.objects.create(validated_data)


    def update(self, instance, validated_data):
        instance.blogAuthor = validated_data.get('blogAuthor',instance.blogAuthor)
        instance.blogContent = validated_data.get('blogContent',instance.blogContent)
class blogSerializer(serializers.ModelSerializer): #better simpler way
    class Meta:
       model = blog
       fields = ['id','blogAuthor','blogContent'] 