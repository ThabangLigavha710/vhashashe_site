
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='vhashashe-home'),
    path('about', views.about, name='vhashashe-about'),
    path('services', views.services, name='vhashashe-services'),
    path('about', views.contact, name='vhashashe-contact'),
]