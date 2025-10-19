from .models import Filme

def lista_filmes_recentes(request):
    #o sinal (-) indica que ordenada em ordem descrecente
    lista = Filme.objects.all().order_by('-data_criacao')[0:8]
    return {'lista_filmes_recentes': lista}

def lista_filmes_emalta(request):
    #o sinal (-) indica que ordenada em ordem descrecente
    lista = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {'lista_filmes_emalta': lista}

def filme_destaque(request):
    filme = Filme.objects.order_by('-visualizacoes').first()
    return {'filme_destaque': filme}