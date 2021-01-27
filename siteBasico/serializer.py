from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from siteBasico.models import * 
from siteBasico.validators import *

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class TextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Texto
        fields = '__all__'

class GaleriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galeria
        fields = '__all__'


class CarroselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrosel
        fields = '__all__'
    
class SobreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobre
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = '__all__'
    
    def validate(self, data):
        if not celular_valido(data['telefone']):
            raise serializers.ValidationError({'Telefone':'O número de celular deve seguir este modelo: 15 91234-1234'})
