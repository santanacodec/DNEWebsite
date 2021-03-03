from django.contrib import admin
from .models import blog

# Register your models here.
@admin.register(blog)
class blogAdminModel(admin.ModelAdmin):
    list_filter=('blogAuthor','blogContent')
    list_display =('blogAuthor','blogContent')