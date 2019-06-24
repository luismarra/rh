from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import RegistroHoraExtra



class HoraExtraList(ListView):
    model = RegistroHoraExtra
    fields = ['motivo', 'observacao', 'funcionario', 'time_he', 'time_he1']


class HoraExtraNovo(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'observacao', 'funcionario', 'time_he', 'time_he1']

    def form_valid(self, form):
        registrohoraextra = form.save(commit=False)
        registrohoraextra.empresa = self.request.user.funcionario.empresa
        registrohoraextra.save()
        return super(HoraExtraNovo, self).form_valid(form)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'observacao', 'funcionario', 'time_he', 'time_he1']


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')

