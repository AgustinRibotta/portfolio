from django.shortcuts import render
from .models import Presentation

def home(request):
    presentations = Presentation.objects.all()[:8]  

    context = {
        'principal': presentations[0] if len(presentations) > 0 else None,
        'sobre_mi': presentations[1] if len(presentations) > 1 else None,
        'stack': presentations[2] if len(presentations) > 2 else None,
        'herramientas': presentations[3] if len(presentations) > 3 else None,
        'complementos': presentations[4] if len(presentations) > 4 else None,
        'proyectos': presentations[5] if len(presentations) > 5 else None,
        'colaboraciones': presentations[6] if len(presentations) > 6 else None,
        'certificaciones': presentations[7] if len(presentations) > 7 else None,
    }
    return render(request, 'home.html', context)