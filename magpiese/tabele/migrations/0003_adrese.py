# Generated by Django 4.0.4 on 2022-05-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabele', '0002_angajati'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adrese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tara', models.CharField(max_length=255)),
                ('judet', models.CharField(max_length=255)),
                ('localitate', models.CharField(max_length=255)),
                ('strada', models.CharField(max_length=255)),
                ('nr_strada', models.IntegerField()),
                ('nr_bloc', models.IntegerField()),
                ('scara', models.CharField(max_length=255)),
                ('etaj', models.IntegerField()),
                ('apartament', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Adresa',
                'verbose_name_plural': 'Adrese',
            },
        ),
    ]
