from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('user_list/', views.user_list, name="user_list"),
    path('user_detail/<int:id>/', views.user_detail, name="user_detail"),
    path('user_detail/<int:id>/delete/', views.user_delete, name="user_delete"),
    path('user_new/', views.user_new, name="user_new"),
    path('user_update/<int:id>/', views.user_update, name="user_update"),
    path('vegan_store_list/', views.vegan_store_list, name="vegan_store_list"),
    path('vegan_store_detail/<int:id>/', views.vegan_store_detail, name="vegan_store_detail"),
    path('vegan_store_detail/<int:id>/delete/', views.vegan_store_delete, name="vegan_store_delete"),
    path('vegan_store_new/', views.vegan_store_new, name="vegan_store_new"),
    path('vegan_store_update/<int:id>/', views.vegan_store_update, name="vegan_store_update"),
    path('vegan_store/review/<int:id>', views.review_create, name="review_create"),
    path('food_list/', views.food_list, name="food_list"),
    path('food_detail/<int:id>/', views.food_detail, name="food_detail"),
    path('food_detail/<int:id>/delete/', views.food_delete, name="food_delete"),
    path('food_new/', views.food_new, name="food_new"),
    path('food_update/<int:id>/', views.food_update, name="food_update"),
    path('good_list/', views.good_list, name="good_list"),
    path('good_detail/<int:id>/', views.good_detail, name="good_detail"),
    path('good_detail/<int:id>/delete/', views.good_delete, name="good_delete"),
    path('good_new/', views.good_new, name="good_new"),
    path('good_update/<int:id>/', views.good_update, name="good_update"),
]