from django.urls import path 
from app import views

urlpatterns = [
    path('', views.home , name='home'  ), 
    path('contact', views.contact, name='contact'),
     path('blog', views.blog , name='blog'),
     path('about', views.about , name='about'),
     path('faqs', views.faqs, name='faqs'),
     path('service', views.service , name='service'), 
     path('preiume' , views.preiume , name='preiume'), 
     path('signup', views.register_view , name='signup'), 
     path('login' , views.login_view , name='login'), 
     path('logout' , views.logout_view , name='logout'), 


]
