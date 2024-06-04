from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('delete-task/<pk>/', views.delete, name = "delete_task"),
    path('update-task/<pk>/', views.update, name = "update_task"),
]