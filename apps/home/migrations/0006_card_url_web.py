# Generated by Django 5.1 on 2024-09-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_card_front_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='url_web',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
    ]
