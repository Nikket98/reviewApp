from django.urls import path
from . import views
from .views import privacy_policy

urlpatterns =[
    path('', views.home, name='reviewApp-home'),
    path('about/', views.about, name='reviewApp-about'),
    path('contact/', views.contact_view, name='reviewApp-contact'),
    path('success/', views.success_view, name='reviewApp-success'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms/', views.terms, name='terms'),
]