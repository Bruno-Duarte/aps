# Generated by Django 3.0.4 on 2020-05-12 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200512_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='consultas',
            field=models.ManyToManyField(blank=True, related_name='consultas_medico_set', to='core.Consulta'),
        ),
    ]