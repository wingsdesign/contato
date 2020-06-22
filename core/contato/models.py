# -*- Mode: Python; coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils.html import format_html
from smtplib import SMTPAuthenticationError
from django.core.mail import send_mail
from django.conf import settings

import sys

SEXO_C = (('F', 'Feminino'), ('M', 'Masculino'),)

class Contato(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=120)
	sexo = models.CharField(max_length=1, blank=True, choices=SEXO_C)
	data = models.DateTimeField(auto_now_add=True)
	email = models.EmailField()
	telefone = models.CharField(max_length=20)
	assunto = models.CharField(max_length=100)
	mensagem = models.TextField()
	email_sent = models.BooleanField(default=False)


	def __str__(self):
		return self.nome

	def send_mail(self):
		message_admin = """
		Nova Mensagem - Wings Design
		Nome: {0}
		Sexo: {1}
		Email: {2}
		Telefone: {3}
		Assunto: {4}

		Mensagem: {5}

		"""
		message_admin = message_admin.format(self.nome, self.get_sexo_display(), self.email, self.telefone, self.assunto, self.mensagem)

		message = """
Olá {0},
Obrigado por entrar em contato

Nossa equipe de atendimento responderá o mais breve possível.
		"""
		message = message.format(self.nome,)

		try:
			send_mail(
				'Novo Contato | Wings Design',
				message_admin,
				'WINGS DESIGN <contato@wingsdesign.com.br>',
				settings.ADMINS,
				fail_silently=False,
			)
			send_mail(
				'Auto Mensagem - Wings Design',
				message,
				'WINGS DESIGN <contato@wingsdesign.com.br>',
				[self.email],
				fail_silently=False,
			)
			self.email_sent = True
			self.save()
		except smtplib.SMTPAuthenticationError:
			pass
def send_confirmation_email(sender, instance, created, **wkargs):
	if not instance.email_sent:
		instance.send_mail()

models.signals.post_save.connect(
	send_confirmation_email, sender=Contato, dispatch_uid='contato.Record')
