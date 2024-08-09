from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

# Contact
class Menssage   (models.Model):

    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"), max_length=254)
    menssage = models.TextField(_("Menssage"))
    
    class Meta:
        verbose_name = _("Menssage")
        verbose_name_plural = _("Menssages")

    def __str__(self):
        return self.name


# Icons
class Icon(models.Model):

    name = models.CharField(_("Name"), max_length=100,)
    url = models.URLField(_("URL"), max_length=200, blank=True, null=True)
    img = models.OneToOneField('Img', verbose_name=_("Image"), on_delete=models.CASCADE, related_name='icon')

    class Meta:
        verbose_name = _("Icon")
        verbose_name_plural = _("Icons")

    def __str__(self):
        return self.name


# Media File
class Img(models.Model):

    name = models.CharField(_("Name"), max_length=50)
    img = models.ImageField(_("Image"), upload_to="../../static/img/", height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = _("Img")
        verbose_name_plural = _("Imgs")

    def __str__(self):
        return self.name


# Cards
class Card(models.Model):

    name = models.CharField(_("Name"), max_length=100,)
    url = models.URLField(_("URL"), max_length=200)
    img = models.ForeignKey('Img', verbose_name=_("Image"), on_delete=models.SET_NULL, null=True, blank=True, related_name='cards')
    icons = models.ManyToManyField('Icon', verbose_name=_("Icons"), related_name='cards')


    class Meta:
        verbose_name = _("Card")
        verbose_name_plural = _("Cards")

    def __str__(self):
        return self.name


# Presentation
class Presentation(models.Model):

    name = models.CharField(_("Name"), max_length=100,)
    description = models.TextField(_("Description"))
    icons = models.ManyToManyField('Icon', verbose_name=_("Icons"), related_name='presentations')
    cards = models.ManyToManyField('Card', verbose_name=_("Cards"), related_name='presentations')
    imgs = models.ManyToManyField('Img', verbose_name=_("Images"), related_name='presentations')


    class Meta:
        verbose_name = _("Presentation")
        verbose_name_plural = _("Presentations")

    def __str__(self):
        return self.name


