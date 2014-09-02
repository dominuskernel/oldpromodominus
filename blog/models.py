#!/usr/bin/env python
# -*- coding: utf-8 -*-

#importamos los modulos para el modelo
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
#Importamos lo necesario para el manejo de las fechas
from django.utils import timezone 
import datetime 

#Creamos la clase Entrada para el manejo de las entradas del blog
class Entrada(models.Model):
	#Introducimos lo que va a contener el blog
	titulo = models.CharField(max_length=100, verbose_name='Titulo', unique = True)
	cuerpo = models.TextField(verbose_name='Texto')
	#Guarda la fecha del momento en que publicamos la entrada
	fecha_de_la_entrada = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de su publicación')
	#Crea un selector de la categoria de la entrada
	CATEGORIAS = (
		('Viajes', 'Viajes'),
		('Libros','Libros'),
		('Cursos','Cursos'),
		('Aplicaciones','Aplicaciones'),
		('Empresas','Empresas'),
		('Eventos','Eventos'),
		('Multimedia','Multimedia'),
	)
	categoria = models.CharField(max_length=14, choices=CATEGORIAS, verbose_name='Categoria')
	
	#Esta función permite mostrar los campos de manera más humana, cogiendo el nombre de las variables o el argumento
	#verbose_name
	def __unicode__(self):
		return self.titulo
	
	def get_absolute_url(self):
		return reverse('blog.views.detalle_entrada', args=[str(self.id)])
		
#Creamos la clase Comentario en ella se permitira al usuario comentar la entrada
class Comentario(models.Model):
	#Relacionamos la tabla Comentario de la base de datos con el de Entrada
	entrada = models.ForeignKey(Entrada)
	#Guardamos el comentario
	texto = models.TextField(verbose_name='Comentario')
	#Guarda la fecha del momento en que publicamos la entrada
	fecha_de_la_publicacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de su publicación')
	#Relacionamos la tabla comentarios de la base de datos con la de usuarios
	usuario = models.ForeignKey(User)
	#Esta función permite mostrar los campos de manera más humana, cogiendo el nombre de las variables o el argumento
	#verbose_name
	def __unicode__(self):
		return self.texto

#Creamos la clase Imagen para subir imagenes relacionadas con la entrada
class Imagen(models.Model):
	#Relacionamos la tabla Imagen de la base de datos con el de Entrada
	entrada = models.ForeignKey(Entrada)
	#Guardamos la imagen
	foto = models.ImageField(upload_to='imagenes', verbose_name='Imagen')	

#Creamos la clase Enlace en el cual podremos introducir el enlace del producto de afiliacion
class Enlace(models.Model):
	#Relacionamos la tabla Enlace de la base de datos con el de Entrada
	entrada = models.ForeignKey(Entrada)
	#Guardamos un titulo del enlace
	titulo = models.CharField(max_length=60, verbose_name='Título')
	#Guardamos el enlace
	link = models.CharField(max_length=150, verbose_name='Enlace')
 
class Rotulo(models.Model):
    #Relacionamos la tabla Rotulo de la base de datos con el de Entrada
    entrada = models.ForeignKey(Entrada)
    #Guardamos la imagen
    foto = models.ImageField(upload_to='imagenes', verbose_name='Rotulo')

