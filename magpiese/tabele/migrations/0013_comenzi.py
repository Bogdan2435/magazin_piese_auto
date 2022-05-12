# Generated by Django 4.0.4 on 2022-05-12 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tabele', '0012_masini'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comenzi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_comanda', models.DateField()),
                ('mod_livrare', models.CharField(choices=[('ridicare personala', 'ridicare personala'), ('livrare', 'livrare')], default='livrare', max_length=20)),
                ('status_comanda', models.CharField(choices=[('plasata', 'plasata'), ('pregatita pentru ridicare', 'pregatita pentru ridicare'), ('in curs de livrare', 'in curs de livrare'), ('ridicata', 'ridicata'), ('livrata', 'livrata')], default='plasata', max_length=30)),
                ('angajat_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tabele.angajati')),
                ('client_cnp', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tabele.clienti')),
                ('masina_vin', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tabele.masini')),
            ],
            options={
                'verbose_name': 'Comanda',
                'verbose_name_plural': 'Comenzi',
            },
        ),
    ]
