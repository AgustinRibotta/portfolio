# Generated by Django 5.1 on 2024-08-09 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mrnssage',
            new_name='Menssage',
        ),
        migrations.AlterModelOptions(
            name='menssage',
            options={'verbose_name': 'Menssage', 'verbose_name_plural': 'Menssages'},
        ),
    ]
