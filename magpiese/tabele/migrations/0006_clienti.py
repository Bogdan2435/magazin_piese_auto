# Generated by Django 4.0.4 on 2022-05-10 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabele', '0005_alter_angajati_loc_munca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clienti',
            fields=[
                ('cnp', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('nume_familie', models.CharField(max_length=255)),
                ('prenume', models.CharField(max_length=255)),
                ('nr_telefon', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
    ]
