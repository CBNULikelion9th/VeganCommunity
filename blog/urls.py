from django.urls import path
from .import views

urlpatterns = [
    path('map_main/', views.map_main, name='map_main'),
    path('vegan_info/', views.vegan_info, name='vegan_info'),
    path('store_save/', views.store_save, name='store_save'),
    path('area_report/', views.area_report, name='area_report'),
    path('vegan_area_add/', views.vegan_area_add, name='vegan_area_add'),
    path('exception/', views.exception, name='exception'),
    path('mypage/', views.mypage, name='mypage'),


    path('store_1/', views.store_1, name='store_1'),
    path('store_2/', views.store_2, name='store_2'),
    path('store_3/', views.store_3, name='store_3'),
    path('store_4/', views.store_4, name='store_4'),
    path('store_5/', views.store_5, name='store_5'),
    path('store_6/', views.store_6, name='store_6'),
    path('store_7/', views.store_7, name='store_7'),
    path('store_8/', views.store_8, name='store_8'),
    path('store_9/', views.store_9, name='store_9'),
    path('store_10/', views.store_10, name='store_10'),

    

]