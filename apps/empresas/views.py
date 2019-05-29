from django.http import request
from django.views.generic.edit import CreateView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome', 'segmento']



