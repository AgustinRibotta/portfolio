
# django
from django.urls import path
# Views
from . import views

app_name = 'home_app'


urlpatterns = [
    # Home page
    path(
        '',
        views.HomeView.as_view(), 
        name='Start'
    ),
    # Contact
    path(
        'register-contact', 
        views.ContacCreateView.as_view(),
        name='contact',
    ),   

]