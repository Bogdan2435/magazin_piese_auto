# Generated by Django 4.0.4 on 2022-05-11 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabele', '0008_piese_alter_clienti_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piese',
            name='data_fabricatie',
        ),
    ]
