from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Questao, Opcao, Aluno
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils import timezone

def welcome(request):
    return render(request, 'votacao/welcome.html')

def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    if request.user.is_authenticated:
        context = {
            'latest_question_list': latest_question_list,
            'user': request.user,
        }
    else:
        context = {
            'latest_question_list': latest_question_list,
            'user': "anonimo",
        }
    return render(request, 'votacao/index.html', context)

def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    if request.user.is_authenticated:
        user = request.user
    else:
        user = "anonimo"
    return render(request, 'votacao/detalhe.html', {'questao': questao, 'user': user})

def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/resultados.html', {'questao': questao})

def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        # Apresenta de novo o form para votar
        return render(request, 'votacao/detalhe.html', { 'questao': questao, 'error_message': "Não escolheu uma opção", })
    else:
        if request.user.aluno.votosFeitos > ord(request.user.aluno.grupo[-1])-48+4 :
            return render(request, 'votacao/detalhe.html', { 'questao': questao, 'error_message': "Limite de votos atingido", })
        opcao_seleccionada.votos += 1
        opcao_seleccionada.save()
        request.user.aluno.votosFeitos += 1
        request.user.aluno.save()
        # Retorne sempre HttpResponseRedirect depois de tratar os dados POST de um form pois isso  impede 
        # os dados de serem tratados repetidamente se o utilizador voltar para a página web anterior.
    return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))

def criarquestao(request):
    return render(request, 'votacao/criarquestao.html')

def criarquestao2(request):
    texto = request.POST['textonovaquestao']
    Questao(questao_texto=texto, pub_data=timezone.now()).save()
    return HttpResponseRedirect(reverse('votacao:index'))

def criaropcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/criaropcao.html', {'questao': questao})

def criaropcao2(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    texto = request.POST['textonovaopcao']
    questao.opcao_set.create(opcao_texto = texto, votos = 0)
    return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))

def apagarquestao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    questao.delete()
    return HttpResponseRedirect(reverse('votacao:index'))

def apagaropcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        return render(request, 'votacao/detalhe.html', { 'questao': questao, 'error_message': "Não escolheu uma opção", })
    else:
        opcao_seleccionada.delete()
    return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))

from django.contrib.auth import authenticate, login

def loginiscte(request):
    if request.method == 'POST':
        usernameP = request.POST['username']
        passwordP = request.POST['password']
        user = authenticate(username=usernameP, password=passwordP)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('votacao:index'))
        else:
            return render(request, 'votacao/loginiscte.html', {'error_message': "Dados inválidos", })
    else:
        return render(request, 'votacao/loginiscte.html')

from django.contrib.auth.models import User

def registar(request):
    if request.method == 'POST':
        usernameP = request.POST['username']
        emailP = request.POST['email']
        passwordP = request.POST['password']
        cursoP = request.POST['curso']
        novouser = User.objects.create_user(usernameP, emailP, passwordP) 
        novouser2 = Aluno(user = novouser, curso = cursoP)
        novouser2.save()
        return HttpResponseRedirect(reverse('votacao:loginiscte'))
    else:
        return render(request, 'votacao/registar.html')
    
def pessoal(request):
    context = {
        'user': request.user,
    }
    return render(request, 'votacao/pessoal.html', context)

from django.contrib.auth import logout

def logoutiscte(request):
    logout(request)
    return HttpResponseRedirect(reverse('votacao:welcome'))