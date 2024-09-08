# Generated by Django 5.1 on 2024-08-09 16:34

import apps.home.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.FileField(upload_to='images/', validators=[apps.home.models.validate_file_size, apps.home.models.validate_file_extension])),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Img',
                'verbose_name_plural': 'Imgs',
            },
        ),
        migrations.CreateModel(
            name='Menssage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('menssage', models.TextField(verbose_name='Menssage')),
            ],
            options={
                'verbose_name': 'Menssage',
                'verbose_name_plural': 'Menssages',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('url', models.URLField(verbose_name='URL')),
                ('img', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cards', to='home.img', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('cards', models.ManyToManyField(blank=True, related_name='presentations', to='home.card', verbose_name='Cards')),
                ('imgs', models.ManyToManyField(blank=True, related_name='presentations', to='home.img', verbose_name='Images')),
            ],
            options={
                'verbose_name': 'Presentation',
                'verbose_name_plural': 'Presentations',
            },
        ),
    ]