# Generated by Django 5.1 on 2024-09-08 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_presentation_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='img',
        ),
        migrations.AddField(
            model_name='card',
            name='img',
            field=models.ManyToManyField(blank=True, null=True, related_name='cards', to='home.img', verbose_name='Image'),
        ),
    ]
