from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Medico, Agendamento
from forms import FormLogin, FormCadastro


def index(request):
    dados = Medico.objects.order_by('-id').filter(
        mostrar=True
    )
    return render(request, 'index.html', {'dados':dados})


def mostrar(request, idbusca):
    dados = get_object_or_404(Medico, id=idbusca)
    return render(request, 'detMedico.html', {'dados':dados})


def buscar(request):
    x = request.GET['buscar']
    if x is None or not x:
        messages.add_message(request, messages.INFO, 'Digite um valor válido')
        return render(request, 'index.html')

    dados = Medico.objects.order_by('nome').filter(
        Q(nome__icontains=x) | Q(especialidade__icontains=x)
    )
    return render(request, 'index.html', {'dados':dados})


def login(request):
    form = FormLogin(request.POST or None)
    if str(request.method) == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("cpf")
            senha = form.cleaned_data.get("senha")
            user = auth.authenticate(request, username=username, password=senha)
            if not user:
                messages.add_message(request, messages.ERROR, "Usuário ou senha inválidos")
                return render(request, "login.html", {'form': form})
            else:
                auth.login(request, user)
                return render(request, "dashboard.html")

        else:
            messages.add_message(request, messages.ERROR, "Erro ao logar", {'form': form})
    else:
        return render(request, "login.html", {'form': form})


def cadastrar(request):
    form = FormCadastro(request.POST or None)
    if str(request.method) == "POST":
        if form.is_valid():
            nome = form.cleaned_data.get("nome")
            email = form.cleaned_data.get("email")
            cpf = form.cleaned_data.get("cpf")
            telefone = form.cleaned_data.get("telefone")
            senha1 = form.cleaned_data.get("senha")
            senha2 = form.cleaned_data.get("senha2")

            if senha1 != senha2:
                messages.add_message(request, messages.WARNING, 'Senhas não compatíveis')
                return render(request, "cadastro.html", {'form': form})

            if not email or not nome or not senha1 or not senha2:
                messages.add_message(request, messages.WARNING, 'Todos os campos são obrigatórios')
                return render(request, 'cadastro.html', {'form': form})

            try:
                validate_email(email)
            except:
                messages.add_message(request, messages.WARNING, 'E-mail inválido')
                return render(request, 'cadastro.html', {'form': form})

            if User.objects.filter(email=email).exists():
               messages.add_message(request, messages.WARNING, 'E-mail já existente')
               return render(request, 'cadastro.html', {'form': form})

            user = User.objects.create_user(
                username=cpf,
                email=email,
                first_name=nome,
                password=senha1,
            )
            messages.add_message(request, messages.SUCCESS, 'Cadastrado com sucesso')
            user.save()
            return redirect('login')
        else:
            messages.add_message(request, messages.WARNING, 'Erro ao cadastrar', {'form': form})
    else:
        return render(request, 'cadastro.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required(redirect_field_name='login')
def dashboard(request):
    dados = Agendamento.objects.order_by('-id').filter(
        mostrar=True
    )
    return render(request, 'dashboard.html', {'dados': dados})
