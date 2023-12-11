from typing import Any
from django.db import models
from apps.usuarios.models import Usuario


class Categoria(models.Model):
	nombre = models.CharField(max_length = 60)

	def __str__(self):
		return self.nombre

class Noticia(models.Model):

	titulo = models.CharField(max_length = 150, null= False)
	cuerpo = models.TextField(null = False)
	imagen = models.ImageField(upload_to = 'noticias')
	categoria_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-fecha',)
	
	def __str__(self):
		return self.titulo
	
	def delete(self, using = None, keep_parents = False):
		self.imagen.delete(self.imagen.name)
		super().delete()

class Comentario(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	texto = models.TextField(max_length = 1500)
	noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.noticia}->{self.texto}"