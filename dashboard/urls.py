from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'dashboard/', views.dashboard, name="dashboard"),
    url(r'^datasteps/(?P<username>\w+)', views.dataStepsTrack.as_view(), name="data"),
    url(r'^dataweight/(?P<username>\w+)', views.dataWeightTrack.as_view(), name="data"),
]
