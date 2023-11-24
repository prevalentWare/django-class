from django.db import models
from django.contrib.auth.models import User

class Categoría(models.Model):
   nombre = models.CharField(max_length=200)
   descripcion = models.TextField(blank=True)

class Ingreso(models.Model):
   usuario = models.ForeignKey(User, on_delete=models.CASCADE)
   cantidad = models.DecimalField(max_digits=10, decimal_places=2)
   fecha = models.DateField()
   categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE)
   descripcion = models.TextField(blank=True)

class Gasto(models.Model):
   usuario = models.ForeignKey(User, on_delete=models.CASCADE)
   cantidad = models.DecimalField(max_digits=10, decimal_places=2)
   fecha = models.DateField()
   categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE)
   descripcion = models.TextField(blank=True)