from django.urls import path
from . import views
from .views import *

import loginapp.views

urlpatterns = [
    
    path('login/', loginapp.views.login, name='login'),
    path('signup/', loginapp.views.signup, name='signup'),
    path('home/', loginapp.views.home, name='home'),
    path('reset_password/', loginapp.views.reset_password, name='reset_password' ),
        ]
