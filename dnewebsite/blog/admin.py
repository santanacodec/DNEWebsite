from django.contrib import admin
from .models import blog

# Register your models here.
@admin.register(blog)
class blogAdminModel(admin.ModelAdmin):
    list_filter=('blogAuthor','blogContent') #This lets you filter by field
    list_display =('blogAuthor','blogContent')#This is to diplay field names in admin page