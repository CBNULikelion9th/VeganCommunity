from django.urls import path
from . import views
from .views import *

import account.views

urlpatterns = [
    
    path('login/', account.views.login, name='login'),
    path('signup/', account.views.signup, name='signup'),
    path('home/', account.views.home, name='home'),
    path('reset_password/', account.views.reset_password, name='reset_password' ),
        ]
