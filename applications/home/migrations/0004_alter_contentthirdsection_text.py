# Generated by Django 4.2.6 on 2023-10-22 14:44

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contentfirstsection_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentthirdsection',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='text'),
        ),
    ]
