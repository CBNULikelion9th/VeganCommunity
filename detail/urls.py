from django.urls import path
from . import views
# from . import food_info

urlpatterns = [
    path('main/', views.main, name="main"),
    path('info/', views.info, name="info"),
]
