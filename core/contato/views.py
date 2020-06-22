# -*- Mode: Python; coding: utf-8 -*-
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from .models import Contato
from .forms import ContatoForm

class ContatoCreate(CreateView):
	form_class = ContatoForm
	template_name = 'contato.html'

	def get_success_url(self):
		return reverse('contato_form_success')

class ContatoCreateSuccess(TemplateView):
	template_name = 'contato_success.html'