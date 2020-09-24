from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registration/$', views.registration, name="registration"),
    url(r'^register/', views.register, name="register"),
    url(r'^login/', views.login, name="login"),
    url(r'^logout/', views.logout, name="logout"),
]