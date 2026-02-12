from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST': # verifica se o método da requisição é POST, ou seja, se o formulário foi enviado #
        form = LoginForms(request.POST) # cria uma instância do formulário com os dados enviados pelo usuário #
        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome, 
            password=senha) # autentica o usuário com base no nome de login e senha fornecidos #
        if usuario is not None: # verifica se a autenticação foi bem-sucedida #
            auth.login(request, usuario) # faz login do usuário autenticado #
            messages.success(request, "Login bem sucedido")
            return redirect('index') # redireciona para a página inicial após o login bem-sucedido #
        else:
            messages.error(request, "Usuario não localizado! Tente novamente")
            return redirect('login') # redireciona para a página de login se a autenticação falhar #

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST': # verifica se o método da requisição é POST, ou seja, se o formulário foi enviado #
        form = CadastroForms(request.POST) # cria uma instância do formulário com os dados enviados pelo usuário #
         
        if form.is_valid():
            if form['senha_cadastro'].value() != form['senha_cadastro2'].value():
                messages.error(request, "Senhas não coincidem")
                return redirect('cadastro') # redireciona para a página de cadastro se as senhas não coincidirem #
            
            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_cadastro'].value()

            if User.objects.filter(username=nome).exists(): # verifica se já existe um usuário com o mesmo nome de cadastro #
                messages.error(request, "Usuario já cadastrado")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome, 
                email=email, 
                password=senha) # cria um novo usuário com os dados fornecidos #
            usuario.save()
            messages.success(request, "Cadastro feito com sucesso!")
            return redirect('login') # redireciona para a página de login após o cadastro bem-sucedido #

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, "logout efetuado com sucesso")
    return redirect('login')