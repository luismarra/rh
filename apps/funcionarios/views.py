from django.contrib.auth.models import User
from django.template.defaultfilters import lower
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'sobrenome', 'funcao', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionario')


class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome', 'sobrenome','funcao',  'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.sobrenome.split(' ')[0]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=lower(username))
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)

