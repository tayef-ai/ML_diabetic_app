from django.contrib import admin
from django.urls import path, include
from mlapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authapp.urls')),
    path('diabetic/', mlviews, name='diabetic'),
]
