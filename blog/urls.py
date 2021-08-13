from django.urls import path
from .import views

urlpatterns = [
    path('map_main/', views.map_main, name='map_main'),
    path('vegan_info/', views.vegan_info, name='vegan_info'),
    path('store_save/', views.store_save, name='store_save'),    
    path('area_report/', views.area_report, name='area_report'),
    path('vegan_area_add/', views.vegan_area_add, name='vegan_area_add'),



    

]