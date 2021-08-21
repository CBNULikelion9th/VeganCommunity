from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views

import signup.views

urlpatterns = [
    
    path('login/', signup.views.login, name='login'),
    path('logout/', signup.views.logout, name='logout'),
    path('signup/', signup.views.signup, name='signup'),
    path('home/', signup.views.home, name='home'),
    path('reset_password/', signup.views.reset_password, name='reset_password' ),
    path('password_reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
        ]
