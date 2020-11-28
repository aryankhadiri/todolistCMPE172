
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from login.views import login
from .views import home
urlpatterns = [
    path('userhome', home, name = "home")
]
