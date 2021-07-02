from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info, name="info"),
    path('info/category1', views.category1, name="category1"),
    path('info/category2', views.category2, name="category2"),
    path('info/category3', views.category3, name="category3"),
    path('info/category4', views.category4, name="category4"),
]
