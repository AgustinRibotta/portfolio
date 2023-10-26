from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import FirstSection, SecondSection, ThirdSection, Networck, ContentThirdSection
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .forms import ContacForm

class HomeView(TemplateView):
    # Homepage
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['first'] = FirstSection.objects.first()
        context['second'] = SecondSection.objects.all()

        # Recupera ThirdSection sin paginación
        third_sections = ThirdSection.objects.all()
        context['thir'] = third_sections

        context['networck'] = Networck.objects.all()

        # Agregar paginación
        page = self.request.GET.get('page')
        paginator = Paginator(third_sections, 8)  # 10 elementos por página
        try:
            third_sections_page = paginator.page(page)
        except PageNotAnInteger:
            third_sections_page = paginator.page(1)
        except EmptyPage:
            third_sections_page = paginator.page(paginator.num_pages)

        context['thir'] = third_sections_page

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