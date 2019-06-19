from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome', 'segmento']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return reverse('create_empresa')

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome', 'segmento']



