#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Importamos el modulo para formaularios
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from blog.models import Comentario
from captcha.fields import ReCaptchaField

#Creamos el formulario para el login
class LoginForm(forms.Form):
	username = forms.CharField(label="Usuario", widget=forms.TextInput())
	password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False))

#Creamos el formulario para el registro
class RegistroForm(forms.Form):
	username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput())
	email = forms.EmailField(label="Email", widget=forms.TextInput)
	password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Repita la Contraseña", widget=forms.PasswordInput(render_value=False))
	captcha = ReCaptchaField(label="Codigo de verificación de usuario")
	
	#Esta función devolverá un error en caso de que el nombre de usuario exista e impedira
	#que un usuario se registre con el mismo nombre
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('El nombre de usuario ya existe')
		
	#Esta función devolverá un error al template en caso de que el email ya se encuentre registrado
	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u= User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Este email ya se ha registrado anteriormente')
	
	#Esta función devolvera un error al template en caso de que el password y password_two no coincidan	
	def clean_password_two(self):
		password = self.cleaned_data['password']
		password_two = self.cleaned_data['password_two']
		if password == password_two:
			pass
		else:
			raise forms.ValidationError('El password no coincide')
		
#Creamos la clase para que el usuario registrado pueda realizar un comentario respecto a la entrada
class ComentarioForm(ModelForm):
	class Meta:
		model = Comentario
		exclude = ("entrada","usuario")
	
		
			
	




