# Generated by Django 3.0.7 on 2020-10-01 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20200515_0941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customusuario',
            options={'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
        migrations.AlterField(
            model_name='customusuario',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=9, verbose_name='Sexo'),
        ),
    ]
