# Generated by Django 4.2.1 on 2023-05-28 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('doc', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateField()),
                ('hora_entrada', models.TimeField()),
                ('data_saida', models.DateField(blank=True, null=True)),
                ('hora_saida', models.TimeField(blank=True, null=True)),
                ('visitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitas.visitante')),
            ],
        ),
    ]
