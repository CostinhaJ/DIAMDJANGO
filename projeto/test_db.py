from votacao.models import Questao, Opcao
from django.utils import timezone
import datetime

# a)

lista = []

for q in Questao.objects.all():
    lista.append(q.questao_texto)

print(lista)

# b)

for q in Questao.objects.all():
    if(q.questao_texto.startswith("Gostas de...")):
        for o in q.opcao_set.all():
            print(o)

# c)

for q in Questao.objects.all():
    if(q.questao_texto.startswith("Gostas de...")):
        for o in q.opcao_set.all():
            if(o.votos > 2):
                print(o)

# d)

lista.clear()

for q in Questao.objects.all():
    if(q.pub_data >= timezone.now() - datetime.timedelta(days=(365*3))):
        lista.append(q.questao_texto)

print(lista)

# e)

contV = 0

for q in Questao.objects.all():
    for o in q.opcao_set.all():
        contV += o.votos

print(contV)

# f)

for q in Questao.objects.all():
    lista = sorted(list(q.opcao_set.all()), key = lambda x: x.votos, reverse=True)
    print(q.questao_texto, lista[0].opcao_texto)