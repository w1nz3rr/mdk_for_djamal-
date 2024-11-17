from django.contrib import admin
from django.urls import path, include
from blog.views import *

urlPatterns = [
    path('admin/', admin.site.urls),
    path('api/users', UserAPIList.as_view()),
    path('api/users/<int:pk>', UserAPIView.as_view()),
]


