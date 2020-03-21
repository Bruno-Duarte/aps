# Generated by Django 3.0.4 on 2020-03-21 15:22

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('especialidade', models.CharField(choices=[('1', 'Cardiologia'), ('2', 'Cirurgia'), ('3', 'Clínica Geral'), ('4', 'Gastroenterologia'), ('5', 'Neurologia'), ('6', 'Odontologia'), ('7', 'Oftalmologia'), ('8', 'Ortopedia'), ('9', 'Pediatria')], max_length=1, verbose_name='Especialidade')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descricao')),
                ('icone', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Especialidade',
                'verbose_name_plural': 'Especialidades',
            },
        ),
    ]
