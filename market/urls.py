from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('market/', views.market_home, name='market_home'),
    path('market/list/', views.market_list, name='market_list'),
    path('market/farmer_notice/', views.farmer_notice, name='farmer_notice'),

    path('market/<int:post_id>/', views.market_detail, name='market_detail'),
    path('market/new/', views.market_new, name='market_new'),
    path('market/create/', views.market_create, name="market_create"),
    path('market/edit/<int:post_id>/', views.market_edit, name="market_edit"),

    path('market/new_comment/<int:post_id>', views.market_comment, name='market_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

