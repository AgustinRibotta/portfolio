from django.contrib import admin
from .models import *
from django.utils.html import format_html


@admin.register(PresentationItaliano)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    filter_horizontal = ('cards', 'imgs')  
    search_fields = ('name', 'description') 

    def short_description(self, obj):
        return format_html('<span>{}</span>', obj.description[:50])  
    
    short_description.short_description = 'Description'

