from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from apps.home.models import Card, Img

# Create your models here.
class PresentationItaliano(models.Model):

    name = models.CharField(_("Name"), max_length=100,)
    description = models.TextField(_("Description"), blank=True, null=True)
    cards = models.ManyToManyField(Card, verbose_name=_("Cards"), related_name='presentationsItaliano', blank=True )
    imgs = models.ManyToManyField(Img, verbose_name=_("Images"), related_name='presentationsItaliano', blank=True )


    class Meta:
        verbose_name = _("Presentation")
        verbose_name_plural = _("Presentations")

    def __str__(self):
        return self.name

