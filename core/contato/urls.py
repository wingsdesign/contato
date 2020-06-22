# -*- Mode: Python; coding: utf-8 -*-
from django.urls import include, path, re_path
from .views import ContatoCreate
from .views import ContatoCreateSuccess

urlpatterns = [
	path('', ContatoCreate.as_view(), name='contato_form'),
	path('sucesso/', ContatoCreateSuccess.as_view(), name='contato_form_success'),

]
