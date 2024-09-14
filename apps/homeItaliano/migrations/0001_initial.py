# Generated by Django 5.1 on 2024-09-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0006_card_url_web'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresentationItaliano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('cards', models.ManyToManyField(blank=True, related_name='presentationsItaliano', to='home.card', verbose_name='Cards')),
                ('imgs', models.ManyToManyField(blank=True, related_name='presentationsItaliano', to='home.img', verbose_name='Images')),
            ],
            options={
                'verbose_name': 'Presentation',
                'verbose_name_plural': 'Presentations',
            },
        ),
    ]