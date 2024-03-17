from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from .models import Questao, Opcao
from django.http import Http404

def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    template = loader.get_template('votacao/index.html')
    context = { 'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))

def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html',{'questao': questao})

def resultados(questao_id):
    response = "Estes sao os resultados da questao %s."
    return HttpResponse(response % questao_id)

def voto(request, questao_id):
 questao = get_object_or_404(Questao, pk=questao_id)
 try: 
    opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])  
 except (KeyError, Opcao.DoesNotExist):
 # Apresenta de novo o form para votar
    return render(request, 'votacao/detalhe.html', { 'questao': questao, 'error_message': "Não escolheu uma opção", })
 else:
    opcao_seleccionada.votos += 1
    opcao_seleccionada.save()
    # Retorne sempre HttpResponseRedirect depois de
    # tratar os dados POST de um form
    # pois isso impede os dados de serem tratados
    # repetidamente se o utilizador
    # voltar para a página web anterior.
    return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))

def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id) 
    return render(request,'votacao/resultados.html',{'questao': questao})


def abrircriarquestao(request):
    return render(request, 'votacao/criarquestao.html')

def criarquestao(request):
    try: 
        questao_texto_nova = request.POST['novaquestao'] 
    except (KeyError, None):
        return render(request, 'votacao/criarquestao.html', {'error_message': "Tente Novamente", })
    if(len(questao_texto_nova) == 0):
        return render(request, 'votacao/criarquestao.html', { 'error_message': "Pergunta Inválida", })
    else:    
        q = Questao(questao_texto = questao_texto_nova, pub_data=timezone.now())
        q.save()
        return HttpResponseRedirect(reverse('votacao:index'))
    

def abrircriaropcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id) 
    return render(request, 'votacao/criaropcao.html',{'questao': questao})
    
def criaropcao(request, questao_id):
    x=1
    try: 
        opcao_texto_nova = request.POST['novaopcao'] 
    except (KeyError, None):
        return render(request, 'votacao/questao_id/criaropcao.html', {'error_message': "Tente Novamente", })
    if(len(opcao_texto_nova) == 0):
        return render(request, 'votacao/questao_id/criaropcao.html', { 'error_message': "Pergunta Inválida", })
    else:    
        questao = get_object_or_404(Questao, pk=questao_id) 
        o = Opcao(questao=questao, opcao_texto=opcao_texto_nova, votos=0) 
        o.save()
        return HttpResponseRedirect(reverse('votacao:index'))
