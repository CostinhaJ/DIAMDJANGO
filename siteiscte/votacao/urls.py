from django.urls import path
from . import views

# (. significa que importa views da mesma directoria)

app_name = 'votacao'
urlpatterns = [
    # ex: votacao/
    path("", views.index, name='index'),
    # ex: votacao/1
    path('<int:questao_id>', views.detalhe, name='detalhe'),
    # ex: votacao/3/resultados
    path('<int:questao_id>/resultados', views.resultados, name='resultados'),
    # ex: votacao/5/voto
    path('<int:questao_id>/voto', views.voto, name='voto'),
    # ex: votacao/criarquestao
    path("abrircriarquestao", views.abrircriarquestao, name='abrircriarquestao'),
    # ex: votacao/criarquestao
    path("criarquestao", views.criarquestao, name='criarquestao'),

    path("<int:questao_id>/criaropcao", views.criaropcao, name='criaropcao'),

    path("<int:questao_id>/criar", views.criar, name='criar'),
]