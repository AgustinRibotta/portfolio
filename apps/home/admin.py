from django.contrib import admin
from .models import *

list_models =[
    Icon,
    Img,
    Card,
    Presentation,
    Menssage
    ]

# Register your models here.
admin.site.register(list_models)