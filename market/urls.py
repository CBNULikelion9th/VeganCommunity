from django.urls import path
from. import views

urlpatterns = [
    path('market/', views.market_home, name='market_home'),
    path('market/list/', views.market_list, name='market_list'),
    path('market/farmer_notice/', views.farmer_notice, name='farmer_notice'),

    path('market/<int:post_id>/', views.market_detail, name='market_detail'),
    path('market/new/', views.market_new, name='maket_new'),
    path('market/new_comment/<int:post_id>', views.market_comment, name='market_comment'),
] 

