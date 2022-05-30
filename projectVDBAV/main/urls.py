from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home',),
    path('home', views.home, name='home',),
    path('signup', views.sign_up, name='signup',),
    path('add-car', views.add_car, name='add-car',),
    path('info', views.info, name='add-info',),
    path('timein', views.timein, name='add-info',),
]
