from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_user, name='login_user' ),
    path('logout_user', views.logout_user, name='logout_user' ),
    path('signup_user', views.signup_user, name='signup_user' ),
]