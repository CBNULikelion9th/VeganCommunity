from django.shortcuts import render
from django.views.generic.base import TemplateView

class MainpageView(TemplateView):
    template_name = 'main/index.html'
