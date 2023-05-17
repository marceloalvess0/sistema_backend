# Generated by Django 4.2.1 on 2023-05-17 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Titulo')),
                ('collaborator', models.CharField(max_length=25, verbose_name='Colaborador')),
                ('datetime', models.DateTimeField(verbose_name='Data e Hora')),
                ('details', models.TextField(verbose_name='Detalhes')),
                ('url_meeting', models.URLField()),
            ],
        ),
    ]