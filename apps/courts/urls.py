from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^main/', views.main, name="main"),
    url(r'^court/([0-9]+)/$', views.court, name="court"),
    url(r'^court/select/', views.select, name="select"),
    url(r'^schedule/', views.schedule, name="schedule"),
    url(r'^dashboard/', views.dashboard, name="dashboard"),
    url(r'^search/', views.search, name="search"),
    url(r'^search/zcode', views.searchzip, name="searchzip")

]