from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from siteBasico.views import * 

router = routers.DefaultRouter()
router.register('texto',TextoViewSet,basename='texto')
router.register('minda',AdminViewSet,basename='admin')
router.register('galeria',GaleriaViewSet,basename='Galeria')
router.register('carrosel',CarroselViewSet,basename='Carrosel')
router.register('sobre',SobreViewSet,basename='Sobre')
router.register('email',EmailViewSet,basename='Email')
router.register('telefone',TelefoneViewSet,basename='Telefone')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
 
]
