# Generated by Django 3.0.4 on 2020-04-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_notificacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacao',
            name='lida',
            field=models.BooleanField(default=False),
        ),
    ]