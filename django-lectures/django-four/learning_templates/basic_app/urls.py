from django.contrib import admin
from django.urls import path
from basic_app import views
from django.conf.urls import url

# For templace tagging
app_name = 'basic_app'

urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('relative',views.relative,name='relative'),
    path('other',views.other,name='other'),
    path('base',views.base,name='base'),
]
