from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name="dash"),
    url(r'^data/', views.dataTrack.as_view(), name="data")
]
