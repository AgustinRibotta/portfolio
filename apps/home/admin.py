from django.contrib import admin
from .models import *
from django.utils.html import format_html

list_models =[
    Menssage
    ]

# Register your models here.
admin.site.register(list_models)

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
   filter_horizontal = ('img',)  

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
    filter_horizontal = ('cards', 'imgs')  
    search_fields = ('name', 'description') 

    def short_description(self, obj):
        return format_html('<span>{}</span>', obj.description[:50])  
    
    short_description.short_description = 'Description'

