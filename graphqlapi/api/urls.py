from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('ingredient',views.ingredient,name='ingredient'),
    path('detail',views.detail,name='detail')
]
