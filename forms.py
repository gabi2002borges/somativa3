from django import forms
from home.models import Agendamento


class FormLogin(forms.Form):
    cpf = forms.CharField(
      label='CPF',
      widget=forms.TextInput(
        attrs={
          'class': 'input'
        }
      )
    )
    senha = forms.CharField(
      widget=forms.PasswordInput(
        attrs={
          'class': 'input'
        }
      )
    )


class FormCadastro(forms.Form):
    nome = forms.CharField(
      label='Usuário',
      widget=forms.TextInput(
        attrs={
          'class': 'input'
        }
      )
    )
    cpf = forms.CharField(
      label='CPF',
      widget=forms.TextInput(
        attrs={
          'class': 'input'
        }
      )
    )
    email = forms.CharField(
      widget=forms.EmailInput(
        attrs={
          'class': 'input'
        }
      )
    )
    telefone = forms.CharField(
      label='Telefone',
      widget=forms.TextInput(
        attrs={
          'class': 'input'
        }
      )
    )
    senha = forms.CharField(
      widget=forms.PasswordInput(
        attrs={
          'class': 'input'
        }
      )
    )
    senha2 = forms.CharField(
      label='Confirme sua senha senha',
      widget=forms.PasswordInput(
        attrs={
          'class': 'input'
        }
      )
    )


class FormAgendamento(forms.ModelForm):

    class Meta:
        model = Agendamento
        fields = ['data', 'horario', 'medicos']
        widgets = {
            'data': forms.DateTimeInput(attrs={'class': 'input', 'type': 'date', 'name': 'data'}),
        }



