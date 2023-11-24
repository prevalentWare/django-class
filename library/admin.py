from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categoría, Ingreso, Gasto

@admin.register(Categoría)
class CategoríaAdmin(admin.ModelAdmin):
    list_display =  ['id', 'nombre', 'descripcion']

@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    list_display =  ['usuario', 'cantidad', 'fecha', 'categoría' ,  'descripcion']

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display =  ['usuario', 'cantidad', 'fecha', 'categoría' ,  'descripcion']