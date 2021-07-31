from django.urls import path
from . import views
from .views import *

import signup.views

urlpatterns = [
    
    path('login/', signup.views.login, name='login'),
    path('signup/', signup.views.signup, name='signup'),
    path('home/', signup.views.home, name='home'),
    path('reset_password/', signup.views.reset_password, name='reset_password' ),
    path('send_email/', signup.views.send_email, name='send_email'),
        ]
