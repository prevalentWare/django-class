from rest_framework import serializers
from .models import Categoría, Ingreso, Gasto

class CategoríaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoría
        fields = ['id', 'nombre', 'descripcion']


class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = ['usuario', 'cantidad', 'fecha', 'categoría' ,  'descripcion']
        read_only_fields = ('usuario',) 


    
    

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = ['usuario', 'cantidad', 'fecha', 'categoría' ,  'descripcion']
        read_only_fields = ('usuario',) 
