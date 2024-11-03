from django.urls import path, include
from . import views

app_name = "homeItaliano"

urlpatterns = [
    path('homeItaliano', views.homeItaliano, name='home_Italiano'),
    path('enviar-formulario-italiano/', views.enviar_formulario_italia, name='enviar_formulario_italia'),

] 

