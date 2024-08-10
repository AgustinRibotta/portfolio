from django.contrib import admin
from .models import *
from django.utils.html import format_html

list_models =[
    Card,
    Menssage
    ]

# Register your models here.
admin.site.register(list_models)

@admin.register(Img)
class ImgAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" height="150" />', obj.img.url)
    
    image_tag.short_description = 'Image'

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    filter_horizontal = ('cards', 'imgs')  # Mejora la interfaz para campos ManyToMany
    search_fields = ('name', 'description')  # Permite buscar por nombre y descripción

    def short_description(self, obj):
        return format_html('<span>{}</span>', obj.description[:50])  # Muestra una vista previa de la descripción
    
    short_description.short_description = 'Description'