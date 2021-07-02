from django.urls import path
from . import views

urlpatterns = [
    # path('main/', views.main, name="main"),
    path('info/', views.info, name="info"),
    path('info/category', views.category, name="category"),
]
