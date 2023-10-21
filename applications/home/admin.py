from django.contrib import admin
from .models import *

MODELS = [
    FirstSection,
    ContentFirstSection,
    SecondSection,
    ContentSecondSection,
    ThirdSection,
    FilterThirSection,
    ContentThirdSection,
    Networck,
    Contact,

]


admin.site.register(MODELS)
