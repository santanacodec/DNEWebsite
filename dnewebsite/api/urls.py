from django.urls import path
from .views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/',blog_list),
    path('',Index),
]
