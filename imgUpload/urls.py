from django.contrib import admin
from django.urls import path
from django.urls import include,re_path
from . import views

urlpatterns = [
    path(r'^$',views.home,name='home'),
    path(r'imageprocess',views.imageprocess,name='imageprocess')
     
]