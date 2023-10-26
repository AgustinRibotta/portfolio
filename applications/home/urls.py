
from django.urls import path

from . import views

app_name = 'home_app'


urlpatterns = [
    path(
        '',
        views.HomeView.as_view(), 
        name='Start'
    ),
    path(
        'register-contact', 
        views.ContacCreateView.as_view(),
        name='contact',
    ),   

]