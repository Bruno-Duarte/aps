# Generated by Django 3.0.4 on 2020-05-06 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_customusuario_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusuario',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], default='Masculino', max_length=9, verbose_name='Sexo'),
        ),
    ]
