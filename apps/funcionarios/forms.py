from django.forms import ModelForm
from apps.funcionarios.models import Funcionario


class DepartamentoForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(DepartamentoForm, self).__init__(*args, **kwargs)
        self.fields['departamentos'].queryset = Funcionario.objects.filter(
            empresa=user.funcionario.empresa
        )

    class Meta:
        model = Funcionario
        fields = [
            'nome',
            'departamentos',
        ]
