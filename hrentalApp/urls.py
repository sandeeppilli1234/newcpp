from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login),
    path('login',views.login, name= 'login'),
    path('home',views.home, name= 'home'),
    
    path('loggingin',views.loggingin,name="loggingin"),
    path('register', views.register, name = "register"),
    path('registeration', views.registeration, name = "registeration"),
    path('buy',views.buy, name= 'buy'),
    path('sell',views.sell, name= 'sell'),
    path('properties',views.properties, name= 'properties'),
    path('contact',views.contact, name= 'contact'),
    path('create_prop',views.create_prop, name= 'create_prop'),
    path('create_prop_account',views.create_prop_account, name= 'create_prop_account'),
    path('enquiry',views.enquiry, name= 'enquiry'),


]