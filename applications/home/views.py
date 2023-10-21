# Dejango
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView
)
# Modesl
from .models import FirstSection, SecondSection, ThirdSection, Networck
# Forms
from .forms import ContacForm


class HomeView(TemplateView):
    # Homepage
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        
        context = super(HomeView, self).get_context_data(**kwargs)
        # Cargamois el home
        context['first'] = FirstSection.objects.first()
        # Portada
        context['second'] =  SecondSection.objects.all()
        # Arcticulos portada
        context['thir'] =  ThirdSection.objects.first()
        # Entradas  recientes
        context['networck'] =  Networck.objects.all()
        return context
    
    
class FooterView(TemplateView):
    # Homepage
    template_name = "include/footer.html"
    
    def get_context_data(self, **kwargs):
        
        context = super(HomeView, self).get_context_data(**kwargs)
        # Entradas  recientes
        context['networck'] =  Networck.objects.all()
        return context
    
    
class ContacCreateView(CreateView):
    
    form_class = ContacForm
    success_url = '.'