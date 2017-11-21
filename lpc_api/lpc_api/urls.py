from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from evento.views import *

router = routers.DefaultRouter()
router.register(r'token', TokenViewSet)
router.register(r'eleitor', EleitorViewSet)
router.register(r'candidato', CandidatoViewSet)
router.register(r'eleicao', EleicaoViewSet)
router.register(r'vagas', VagaViewSet)
router.register(r'votar', VotarViewSet)
#router.register(r'resultado', ResultadoViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^resultado/$', Resultado, name = 'Resultado'),
]
