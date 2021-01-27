
from django.db.models.query import QuerySet
from rest_framework import viewsets,generics
from siteBasico.models import *
from .serializer import *

class TextoViewSet(viewsets.ModelViewSet):
    queryset = Texto.objects.all()
    serializer_class = TextoSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class GaleriaViewSet(viewsets.ModelViewSet):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer

class CarroselViewSet(viewsets.ModelViewSet):
    queryset = Carrosel.objects.all()
    serializer_class = CarroselSerializer

class SobreViewSet(viewsets.ModelViewSet):
    queryset = Sobre.objects.all()
    serializer_class = SobreSerializer

class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class TelefoneViewSet(viewsets.ModelViewSet):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer