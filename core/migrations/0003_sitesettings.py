# Generated by Django 3.0.4 on 2020-04-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200421_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(default='Mitlton Str. 26-27 London UK', max_length=255)),
                ('telefone', models.CharField(default='+5585999999999', max_length=255)),
                ('email', models.EmailField(default='clinica@email.com', max_length=255)),
                ('support', models.EmailField(default='support@email.com', max_length=254)),
                ('account_sid', models.CharField(default='ACbcad883c9c3e9d9913a715557dddff88', max_length=255)),
                ('auth_token', models.CharField(default='abd4d45dd57dd79b86dd51df2e2a6cd7', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
