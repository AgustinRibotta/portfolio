# Djeango
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
# Forms
from .forms import ContacForm
# Models 
from .models import FirstSection, SecondSection, ThirdSection, Networck, ContentThirdSection

class HomeView(TemplateView):
    """ View that generates the corresponding contexts for painting at home """
    
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        
        # Context of FirstSection
        context['first'] = FirstSection.objects.first()
        
        # Context of SecondSection
        context['second'] = SecondSection.objects.all()
        
        # Context of Networck
        context['networck'] = Networck.objects.all()
        
        # Context of ThirdSection
        context['thir'] = ThirdSection.objects.all()
        
        # Context of ContentThirdSection
        context['thir_content'] = ContentThirdSection.objects.select_related('content').order_by('-created')
        
        return context
    
    
class FooterView(TemplateView):
    """ View to add the links to the footer """
    
    template_name = "include/footer.html"
    
    def get_context_data(self, **kwargs):
         
        context = super(FooterView, self).get_context_data(**kwargs)
        
        # Context of Networck
        context['networck'] =  Networck.objects.all()
        return context
    
    

# Register contacto
class ContacCreateView(CreateView):
    
    form_class = ContacForm
    success_url = '.'