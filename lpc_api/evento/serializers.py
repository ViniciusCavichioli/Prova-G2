from rest_framework import routers, serializers, viewsets
from evento.models import *

class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'

    def create(self, data):
        token = Token.objects.create(**data)
        return token

class EleitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eleitor
        fields = '__all__'

    def create(self, data):
        eleitor = Eleitor.objects.create(**data)
        return eleitor

class CandidatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidato
        fields = '__all__'

    def create(self, data):
        candidato = Candidato.objects.create(**data)
        return candidato

class EleicaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eleicao
        fields = '__all__'

    def create(self, data):
        eleicao = Eleicao.objects.create(**data)
        return eleicao

class VagaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaga
        fields = '__all__'

    def create(self, data):
        vaga = Vaga.objects.create(**data)
        return vaga

class VotarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Votar
        fields = '__all__'

    def create(self, data):
        votar = Votar.objects.create(**data)
        return votar

class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resultado
        fields = '__all__'

    def create(self, data):
        resultado = Resultado.objects.create(**data)
        return resultado
