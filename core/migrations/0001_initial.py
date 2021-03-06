# Generated by Django 3.0.4 on 2020-04-21 15:06

import core.models
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Membro da equipe')),
                ('cpf', models.CharField(max_length=15, unique=True, verbose_name='CPF')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('imagem', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem')),
                ('formacao', models.CharField(default='', max_length=30, verbose_name='Formacao')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', core.models.UsuarioManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('texto', models.TextField(max_length=500, verbose_name='Comentario')),
            ],
            options={
                'verbose_name': 'Comentário',
                'verbose_name_plural': 'Comentários',
            },
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(choices=[('Cardiologia', 'Cardiologia'), ('Cirurgia', 'Cirurgia'), ('Clínica Geral', 'Clínica Geral'), ('Gastroenterologia', 'Gastroenterologia'), ('Neurologia', 'Neurologia'), ('Odontologia', 'Odontologia'), ('Oftalmologia', 'Oftalmologia'), ('Ortopedia', 'Ortopedia'), ('Pediatria', 'Pediatria')], max_length=50, verbose_name='Especialidade')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descricao')),
                ('icone', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Especialidade',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.CharField(choices=[('08h-09h', '08h-09h'), ('09h-10h', '09h-10h'), ('10h-11h', '10h-11h')], max_length=7, verbose_name='Horario')),
            ],
            options={
                'verbose_name': 'Horário',
                'verbose_name_plural': 'Horários',
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('data', models.DateField(verbose_name='Data da Consulta')),
                ('sintomas', models.TextField(blank=True, max_length=500, null=True, verbose_name='Sintomas')),
                ('remedios', models.TextField(blank=True, max_length=500, null=True, verbose_name='Remedios')),
                ('exames', models.TextField(blank=True, max_length=500, null=True, verbose_name='Exames')),
                ('estado', models.CharField(choices=[('Agendada', 'Agendada'), ('Cancelada', 'Cancelada'), ('Espera', 'Espera'), ('Realizada', 'Realizada'), ('Expirada', 'Expirada'), ('Análise', 'Análise')], default='Agendada', max_length=9, verbose_name='Estado')),
                ('motivo_cancelamento', models.TextField(blank=True, max_length=100, null=True, verbose_name='Motivo do Cancelamento')),
                ('hora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Horario', verbose_name='Horário')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('customusuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('comentarios', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Comentario', verbose_name='Comentario')),
                ('consultas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultas_paciente_set', to='core.Consulta', verbose_name='Consultas')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
            bases=('core.customusuario',),
            managers=[
                ('objects', core.models.PacienteManager()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('customusuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('consultas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultas_medico_set', to='core.Consulta', verbose_name='Consultas')),
                ('especialidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Especialidade', verbose_name='Especialidade')),
            ],
            options={
                'verbose_name': 'Médico',
                'verbose_name_plural': 'Médicos',
            },
            bases=('core.customusuario',),
            managers=[
                ('objects', core.models.MedicoManager()),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Medico', verbose_name='Médico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Paciente', verbose_name='Paciente'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Paciente', verbose_name='Paciente'),
        ),
    ]
