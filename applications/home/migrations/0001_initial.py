# Generated by Django 4.2.6 on 2023-10-22 11:56

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60, verbose_name='Name')),
                ('email', models.CharField(max_length=200)),
                ('messagge', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Message',
            },
        ),
        migrations.CreateModel(
            name='FirstSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='cover', verbose_name='Cover Image')),
            ],
            options={
                'verbose_name': 'First section',
                'verbose_name_plural': 'First sections',
            },
        ),
        migrations.CreateModel(
            name='Networck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor_uploader.fields.RichTextUploadingField(default=True, null=True, verbose_name='Title')),
                ('urls', models.URLField(blank=True, null=True, verbose_name='Url')),
                ('mail', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Mail')),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='uploads/')),
            ],
            options={
                'verbose_name': 'Networck',
                'verbose_name_plural': 'Networcks',
            },
        ),
        migrations.CreateModel(
            name='SecondSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Second section',
                'verbose_name_plural': 'Second sections',
            },
        ),
        migrations.CreateModel(
            name='ThirdSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Third section',
                'verbose_name_plural': 'Third sections',
            },
        ),
        migrations.CreateModel(
            name='FilterThirSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filter', to='home.thirdsection')),
            ],
            options={
                'verbose_name': 'Filter',
                'verbose_name_plural': 'Filters',
            },
        ),
        migrations.CreateModel(
            name='ContentThirdSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='repo', verbose_name='Img')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('text', models.CharField(max_length=250, verbose_name='Text')),
                ('urls', models.URLField(verbose_name='Url')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='home.thirdsection')),
            ],
            options={
                'verbose_name': 'Third Section Content ',
                'verbose_name_plural': 'Third Section Contents',
            },
        ),
        migrations.CreateModel(
            name='ContentSecondSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('img', models.ImageField(upload_to='repo', verbose_name='Img')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='home.secondsection')),
            ],
            options={
                'verbose_name': ' Second Section Content',
                'verbose_name_plural': 'Second Section Contents',
            },
        ),
        migrations.CreateModel(
            name='ContentFirstSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(default=True, null=True, verbose_name='text')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='home.firstsection')),
            ],
            options={
                'verbose_name': 'First Section Content',
                'verbose_name_plural': 'First Section Contents',
            },
        ),
    ]