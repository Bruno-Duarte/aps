# Generated by Django 3.0.4 on 2020-04-26 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200426_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacao',
            name='mensagem',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Mensagem'),
        ),
    ]
