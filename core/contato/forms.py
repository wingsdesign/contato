# -*- Mode: Python; coding: utf-8 -*-
from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
	class Meta:
		model = Contato
		exclude = ('id', 'data', 'email_sent')