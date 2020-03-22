from django.db import models
from stdimage.models import StdImageField
import uuid


def get_file_path(_instance, filename):
	ext = filename.split('.')[-1]
	filename = '{}.{}'.format(uuid.uuid4(), ext)
	return filename


class Base(models.Model):
	criados = models.DateField('Criação', auto_now_add=True)
	modificado = models.DateField('Atualização', auto_now=True)
	ativo = models.BooleanField('Ativo', default=True)

	class Meta:
		abstract = True


class Especialidade(Base):
	CHOICES = (
		('Cardiologia', 'Cardiologia'),
		('Cirurgia', 'Cirurgia'),
		('Clínica Geral', 'Clínica Geral'),
		('Gastroenterologia', 'Gastroenterologia'),
		('Neurologia', 'Neurologia'),
		('Odontologia', 'Odontologia'), 
		('Oftalmologia', 'Oftalmologia'), 
		('Ortopedia', 'Ortopedia'), 
		('Pediatria', 'Pediatria'),
	)
	nome = models.CharField('Especialidade', max_length=50, choices=CHOICES)
	descricao = models.TextField('Descricao', max_length=200)
	icone = StdImageField('Icone', upload_to=get_file_path, \
		variations={'thumb': {'width': 41, 'height': 49, 'crop': True}})

	class Meta:
		verbose_name = 'Especialidade'
		verbose_name_plural = 'Especialidades'

	def __str__(self):
		return self.nome


class Pessoa(Base):
	nome = models.CharField('Nome', max_length=50)
	cpf = models.CharField('CPF', max_length=11)

	class Meta:
		abstract = True


class Medico(Pessoa):
	especialidade = models.ForeignKey('core.Especialidade', verbose_name='Especialidade', on_delete=models.CASCADE)
	formacao = models.CharField('Formacao', max_length=30)
	imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 264, 'height': 276, 'crop': True}})

	class Meta:
		verbose_name = 'Médico'
		verbose_name_plural = 'Médicos'

	def __str__(self):
		return self.nome