# Generated by Django 4.2.6 on 2023-10-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentfirstsection',
            name='title',
            field=models.CharField(default=True, max_length=50, null=True, verbose_name='Title'),
        ),
    ]
