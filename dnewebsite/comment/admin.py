from django.contrib import admin

# Register your models here.
from .models import commentModel

# Register your models here.
@admin.register(commentModel)
class blogAdminModel(admin.ModelAdmin):
    list_filter=('comment','blogId','commentAuthor') #This lets you filter by field
    list_display =('comment','blogId','commentAuthor')
