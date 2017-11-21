from django.shortcuts import render
from django.contrib.auth.models import User
from evento.models import *
from evento.serializers import *
from django.http import HttpResponse


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class EleitorViewSet(viewsets.ModelViewSet):
    queryset = Eleitor.objects.all()
    serializer_class = EleitorSerializer


class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer


class EleicaoViewSet(viewsets.ModelViewSet):
    queryset = Eleicao.objects.all()
    serializer_class = EleicaoSerializer

class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

class VotarViewSet(viewsets.ModelViewSet):
    queryset = Votar.objects.all()
    serializer_class = VotarSerializer

class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer

def Resultado(request):
    retorno = "<h1> Resultados </h1>"
    lista = Votar.objects.all()
    for age in lista:
        #retorno += '</br> Candidato: {} </br>'.format(Votar.candidato)
        retorno += '</br> Candidato: {} Votos: {} Votos em Branco :{}</br>'.format(Votar.candidato, Votar.Votou, Votar.votouemBranco)
    return HttpResponse(retorno)
