from django.db import models
# Ckaeditor
from ckeditor_uploader.fields import RichTextUploadingField


class FirstSection (models.Model):
    """ Model that will be in charge of painting the information in the first section """
    
    img = models.ImageField(
        "Cover Image", 
        upload_to="cover"
    )
    
    
    class Meta:
        
        verbose_name = 'First section'
        verbose_name_plural = 'First sections'
        
        
    def __str__(self):
        
        return str(self.id)
    
    
class ContentFirstSection(models.Model):
    """ Stores the content of the First Section """

    content = models.ForeignKey(
        FirstSection,
        on_delete= models.CASCADE,
        related_name= 'content',
    )
    title = models.CharField(
        "Title",
        max_length=50,
        blank=True,
        null=True,
        )
    text = RichTextUploadingField(
        'text',
        blank=True,
        null=True 
    )
    
    class Meta:
        
        verbose_name = 'First Section Content'
        verbose_name_plural = 'First Section Contents'
        
    def __str__(self):
        
        return str(self.title)
    
        
    
class SecondSection (models.Model):
    """ Model that will be in charge of painting the information in the Second section """
    
    title = models.CharField('Title', max_length=50)
    
    class Meta:
        
        verbose_name = 'Second section'
        verbose_name_plural = 'Second sections'
        
        
    def __str__(self):
        
        return self.title


class ContentSecondSection(models.Model):
    """ Stores the content of the Second Section """

    content = models.ForeignKey(
        SecondSection,
        on_delete= models.CASCADE,
        related_name= 'content',
    )
    title = models.CharField(
        "Title", 
        max_length=50,
        blank=True,
        null=True,
    )
    img = models.ImageField('Img', upload_to='repo', height_field=None, width_field=None, max_length=None)
    
    class Meta:
        
        verbose_name = ' Second Section Content'
        verbose_name_plural = 'Second Section Contents'
        
    def __str__(self):
        
        return str(self.id) + str(self.title)
    
class ThirdSection (models.Model):
    """ Model that will be in charge of painting the information in the Third section """
    
    title = models.CharField('Title', max_length=50)
    
    class Meta:
        
        verbose_name = 'Third section'
        verbose_name_plural = 'Third sections'
        
        
    def __str__(self):
        
        return self.title
    
    
class ContentThirdSection(models.Model):
    """ Stores the content of the Third section """

    content = models.ForeignKey(
        ThirdSection,
        on_delete= models.CASCADE,
        related_name= 'content',
    )
    img = models.ImageField('Img', upload_to='repo', height_field=None, width_field=None, max_length=None)
    title = models.CharField("Title", max_length=50)
    text = RichTextUploadingField(
        'text',
        blank=True,
        null=True 
    )
    urls = models.URLField("Url", max_length=200)
    
    class Meta:
        
        verbose_name = 'Third Section Content '
        verbose_name_plural = 'Third Section Contents'
        
    def __str__(self):
        
        return self.title
    
    

class FilterThirSection(models.Model):
    """ Stores the content of the Filter Thir section """

    filter = models.ForeignKey(
        ThirdSection,
        on_delete= models.CASCADE,
        related_name= 'filter',
    )
    title = models.CharField("Title", max_length=50)
    
    class Meta:
        
        verbose_name = 'Filter'
        verbose_name_plural = 'Filters'

    def __str__(self):
        
        return self.title
    
        
class Networck(models.Model):
    
    
    title = RichTextUploadingField(
        'Title',
        default=True,
        null=True 
    )
    urls = models.URLField(
        "Url",
        max_length=200,
        null= True,
        blank= True,
    )
    mail = models.EmailField(
        'Mail', 
        max_length=254,
        null= True,
        blank= True,
    )
    phone = models.CharField(
        max_length=12,
        null= True,
        blank= True,
    )
    cv = models.FileField(
        upload_to="uploads/",
        null= True,
        blank= True,
    )

    class Meta:
        
        verbose_name = 'Networck'
        verbose_name_plural = 'Networcks'
        

    def __str__(self):
        
        return self.title
    
    

class Contact(models.Model):
    
    full_name = models.CharField(
        'Name',
        max_length=60
    )
    email = models.CharField(max_length=200,)
    messagge = models.TextField()
    
    class Meta:

        verbose_name = 'Contact'
        verbose_name_plural = 'Message'
        
    def __str__(self):
        
        return self.full_name