from django.db import models
from django.utils import timezone


class Token(models.Model):
    codigo = models.IntegerField('Codigo')

    def __str__(self):
        return '{}'.format(self.codigo)

class Eleitor(models.Model):
    nome = models.CharField('nome', max_length=200)
    CPF = models.CharField('CPF', max_length = 11)
    token = models.ForeignKey(Token, related_name='Token', null=True, blank=False)


    def __str__(self):
        return '{}'.format(self.nome)

class Candidato(models.Model):
    nome = models.CharField('nome', max_length = 150)
    partido = models.CharField('partido', max_length = 150)

    def __str__(self):
        return '{}'.format(self.nome)


class Eleicao(models.Model):
    codigoEleicao = models.IntegerField('CodigoEleição')
    eleitor = models.ForeignKey(Eleitor, related_name='eleitorEleicao', null=True, blank=False)
    local = models.CharField('local', max_length = 100)
    dataEHoraDeInicio = models.DateTimeField('dataEHoraDeInicio', default=timezone.now)
    dataEHoraDeTermino = models.DateTimeField('dataEHoraDeTermino', default=timezone.now)

    def __str__(self):
        return '{}'.format(self.codigoEleicao)


class Vaga(models.Model):
    cargo = models.CharField('cargo', max_length=150)
    quantidadeVaga = models.IntegerField('quantidadeVaga')
    candidato = models.ForeignKey(Candidato, related_name='candidatoVaga', null=True, blank=False)

    def __str__(self):
        return '{}'.format(self.cargo)

class Votar(models.Model):
    TIPO_CHOICES = (
        ('sim', 'Sim'),
        ('nao', 'Não'),
    )
    eleitor = models.ForeignKey(Eleitor, related_name='eleitor', null=True, blank=False)
    candidato = models.ForeignKey(Candidato, related_name='candidato', null=True, blank=False)
    Votou = models.CharField(max_length=7, choices=TIPO_CHOICES, blank=False, null=False)
    votouemBranco = models.BooleanField("Voto em Branco?",default=False)

    def __str__(self):
        return self.candidato.nome + ": votos: " + self.Votou + ": votosemBranco:" + self.votouemBranco

class Resultado(models.Model):
    eleicao = models.ForeignKey(Eleicao, related_name='eleicao', null=True, blank=False)

    def __str__(self):
        return '{}'.format(self.cpf)
