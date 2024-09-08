from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import os

# Create your models here.

# Contact
class Menssage (models.Model):

    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"), max_length=254)
    menssage = models.TextField(_("Menssage"))
    
    class Meta:
        verbose_name = _("Menssage")
        verbose_name_plural = _("Menssages")

    def __str__(self):
        return self.name


# Media File
def validate_file_size(file):
    file_size = file.file.size
    limit_mb = 5  # Tamaño máximo en megabytes
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError(f'El tamaño del archivo no puede exceder los {limit_mb} MB.')

def validate_file_extension(file):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.svg']
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError('El archivo debe ser una imagen con extensión: jpg, jpeg, png o svg.')

class Img(models.Model):
    
    name = models.CharField(max_length=50)
    img = models.FileField(upload_to='images/', validators=[validate_file_size, validate_file_extension])
    url = models.URLField(_("URL"), max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Img"
        verbose_name_plural = "Imgs"

    def __str__(self):
        return self.name
    

# Cards
class Card(models.Model):
    front_page = models.ForeignKey("Img", verbose_name=_("Images"), on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=100,)
    url = models.URLField(_("URL"), max_length=200)
    img = models.ManyToManyField('Img', verbose_name=_("Image"),blank=True, related_name='cards')

    class Meta:
        verbose_name = _("Card")
        verbose_name_plural = _("Cards")

    def __str__(self):
        return self.name


# Presentation
class Presentation(models.Model):

    name = models.CharField(_("Name"), max_length=100,)
    description = models.TextField(_("Description"), blank=True, null=True)
    cards = models.ManyToManyField('Card', verbose_name=_("Cards"), related_name='presentations', blank=True )
    imgs = models.ManyToManyField('Img', verbose_name=_("Images"), related_name='presentations', blank=True )


    class Meta:
        verbose_name = _("Presentation")
        verbose_name_plural = _("Presentations")

    def __str__(self):
        return self.name

