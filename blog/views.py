#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blog.models import Entrada, Comentario, Imagen, Enlace, Rotulo
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
#modulos para la gestion de usuario
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
#modulos para la gestión de formularios
from django import forms
from forms import LoginForm, RegistroForm, ComentarioForm
from random import choice

# Se crea la vistas para la página de inicio, en ella se mostrará todas las
# entradas disponibles de todas las categorias
def index(request):
	entradas = Entrada.objects.all().order_by('-fecha_de_la_entrada')[:20]
	entradas_recientes = Entrada.objects.all().order_by('-fecha_de_la_entrada')[:5]
	return render_to_response('index.html',{'entradas':entradas,'entradas_recientes':entradas_recientes}, context_instance=RequestContext(request))
		

# Se crea la vista para cada entrada. En el aparecera la entrada seleccionada
# mediante un link en la pagina de inicio y se visualizara la entrada, imagenes agragadas
# sus comentarios y un formulario para introducir un nuebo usuario. 	
def detalle_entrada(request, id_entrada):
	#Esto es importante ya que en esta variable se obtendra la id de la entrada para luego pasarlo en el template.
	#Sin esto no se podra hacer link por cada entrada ya nos actuaria solo como un refresco de página
    dato = get_object_or_404(Entrada, pk=id_entrada)
    entradas_recientes = Entrada.objects.all().order_by('-fecha_de_la_entrada')[:5]
    comentarios = Comentario.objects.filter(entrada=dato)
    imagenes = Imagen.objects.filter(entrada=dato)
    enlaces = Enlace.objects.filter(entrada=dato)
    rotulos = Rotulo.objects.filter(entrada=dato)
    usuario = request.user
    if request.user.is_authenticated:
        formulario = ComentarioForm()
        if request.method == 'POST':
            formulario = ComentarioForm(request.POST)
            if formulario.is_valid():
                entrada = get_object_or_404(Entrada, id=id_entrada)
                comentario = formulario.save(commit=False)
                comentario.entrada = entrada
                comentario.usuario = usuario
                comentario.save()
                return render_to_response('entrada.html',{'entrada':dato,'entradas_recientes':entradas_recientes,'comentarios':comentarios, 'imagenes':imagenes,'enlaces':enlaces,'formulario':formulario,'rotulos':rotulos}, context_instance=RequestContext(request))
            else:
                return render_to_response('entrada.html',{'entrada':dato,'entradas_recientes':entradas_recientes,'comentarios':comentarios, 'imagenes':imagenes,'enlaces':enlaces,'formulario':formulario,'rotulos':rotulos}, context_instance=RequestContext(request))		
    return render_to_response('entrada.html',{'entrada':dato,'entradas_recientes':entradas_recientes,'comentarios':comentarios, 'imagenes':imagenes,'enlaces':enlaces,'formulario':formulario,'rotulos':rotulos}, context_instance=RequestContext(request))

# Se crea la vista para la creación de un nuevo usuario. En esta vista preguntara al usuario los datos necesarios 
#para la creación de su cuenta
def nuevo_usuario(request):
	formulario = RegistroForm(request.POST or None)
	if formulario.is_valid():
		usuario = formulario.cleaned_data['username']
		email = formulario.cleaned_data['email']
		password = formulario.cleaned_data['password']
		password_two = formulario.cleaned_data['password_two']
		captcha = formulario.cleaned_data['captcha']
		u = User.objects.create_user(username=usuario,email=email,password=password)
		u.save()
		return render_to_response('registrado.html', context_instance=RequestContext(request))
	else:
		return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))
	return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))
	
# Se crea una vista para el login de usuario.
def login(request):
	mensaje = ""
	if not request.user.is_authenticated():
		if request.method == 'POST':
			formulario = RegistroForm(request.POST)
			if formulario.is_valid:
				usuario = request.POST['username']
				clave = request.POST['password']
				acceso = authenticate(username=usuario, password=clave)
				if acceso is not None:
					if acceso.is_active:
						auth_login(request, acceso)
						return HttpResponseRedirect('/')
					else:
						mensaje="El usuario no se encuentra activo"
				else:
					mensaje="Este usuario no esta registrado o la contraseña no coincide."			
		formulario = LoginForm()
		return render_to_response('login.html',{'formulario':formulario, 'mensaje':mensaje}, context_instance=RequestContext(request))
	else:
		return render_to_response('login.html', context_instance=RequestContext(request))

#Esta vista permite al usuario cerrar su sesión
@login_required(login_url='/login')		
def logout_sesion(request):
	logout(request)
	return HttpResponseRedirect('/')

