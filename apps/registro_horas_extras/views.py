from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm



class HoraExtraList(ListView):
    model = RegistroHoraExtra
    fields = ['motivo', 'observacao',
              'funcionario', 'date_time_he', 'time_he1']
    paginate_by = 100

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(
            funcionario__empresa=empresa_logada)


class HoraExtraNovo(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    success_url = reverse_lazy('list_hora_extra')

    def get_form_kwargs(self):
        kwargs = super(HoraExtraNovo, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraNovoExtend(CreateView):
    model = RegistroHoraExtra
    fields = [
        'motivo',
        'observacao',
        'date_time_he',
        'time_he1']

    def get_absolute_url(self):
        return reverse_lazy('update_funcionario', args=[self.funcionario.id])

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.funcionario_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraEditList(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    success_url = reverse_lazy('list_hora_extra')

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditList, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


