from django.urls import path, re_path
from . import views

urlpatterns = [

    path(r'', views.index, name='index'),

    path(r'about/', views.about, name='about'),

    path(r'training/', views.training, name='training'),

    path(r'faq/', views.faq, name='faq'),

    path(r'registration/', views.register, name='register'),

    path(r'contact/', views.cont, name='contact'),

]
