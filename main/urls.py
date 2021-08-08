from django.urls import path
from .views import MainpageView

urlpatterns = [
    path('', MainpageView.as_view(), name='mainpage'),
]