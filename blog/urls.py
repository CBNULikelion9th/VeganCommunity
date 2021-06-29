from django.urls import path
from .import views

urlpatterns = [
    path('map/', views.post_map, name='post_map'),
    path('main/', views.post_main, name='post_main'),
    path('info/', views.post_info, name='post_info'),
    path('save/', views.post_save, name='post_save'),
    path('report/', views.post_report, name='post_report'),
    path('add/', views.post_add, name='post_add'),
    

]