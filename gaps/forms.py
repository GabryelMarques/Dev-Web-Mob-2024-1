from django import forms
from gaps.models import Evento
#  usada para renderizar e validar formulários relacionados a eventos.
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo','data', 'hora', 'local', 'descricao', 'foto']

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

User = get_user_model()

class ClienteForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email já está em uso.")
        return email


from gaps.models import Inscricao

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = []

class PesquisaEventoForm(forms.Form):
    termo_de_pesquisa = forms.CharField(max_length=100, required=False, label='Pesquisar')
