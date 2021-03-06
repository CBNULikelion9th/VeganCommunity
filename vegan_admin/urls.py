from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('user_list/', views.user_list, name="user_list"),
    path('user_detail/<int:id>/', views.user_detail, name="user_detail"),
    path('user_detail/<int:id>/delete/', views.user_delete, name="user_delete"),
    path('user_new/', views.user_new, name="user_new"),
    path('user_update/<int:id>/', views.user_update, name="user_update"),

    path('custom_store_list/', views.custom_store_list, name="custom_store_list"),
    path('custom_store_detail/<int:id>/', views.custom_store_detail, name="custom_store_detail"),
    path('custom_store_detail/<int:id>/delete/', views.custom_store_delete, name="custom_store_delete"),
    path('custom_store_new/', views.custom_store_new, name="custom_store_new"),
    path('custom_store_update/<int:id>/', views.custom_store_update, name="custom_store_update"),
    
    path('report_store_list/', views.report_store_list, name="report_store_list"),
    path('report_store_detail/<int:id>/', views.report_store_detail, name="report_store_detail"),
    path('report_store_detail/<int:id>/delete/', views.report_store_delete, name="report_store_delete"),
    path('report_store_new/', views.report_store_new, name="report_store_new"),
    path('report_store_update/<int:id>/', views.report_store_update, name="report_store_update"),

    path('add_store_list/', views.add_store_list, name="add_store_list"),
    path('add_store_detail/<int:id>/', views.add_store_detail, name="add_store_detail"),
    path('add_store_detail/<int:id>/delete/', views.add_store_delete, name="add_store_delete"),
    path('add_store_new/', views.add_store_new, name="add_store_new"),
    path('add_store_update/<int:id>/', views.add_store_update, name="add_store_update"),

    path('goods_list/', views.goods_list, name="goods_list"),
    path('goods_detail/<int:id>/', views.goods_detail, name="goods_detail"),
    path('goods_detail/<int:id>/delete/', views.goods_delete, name="goods_delete"),
    path('goods_new/', views.goods_new, name="goods_new"),
    path('goods_update/<int:id>/', views.goods_update, name="goods_update"),
    path('goods/comment/<int:id>', views.comment_create, name="comment_create"),
    path('goods/comment_list/', views.comment_list, name="comment_list"),
]