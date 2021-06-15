from django.db import models

# Create your models here.


class Clientes (models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50, verbose_name="La dirección")
    email = models.EmailField(blank=True, null=True)
    tel = models.CharField(max_length=9, verbose_name="Celular")

    def __str__(self):
        return 'Nombre: %s | Email : %s' % (self.nombre, self.email)

class Articulos (models.Model):
    codigo = models.CharField(max_length=6)
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=40)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return 'Codigo: %s | Nombre : %s - %s | Precio: %s | Stock: %s' % (self.codigo, self.nombre, self.marca, self.precio, self.stock)
    

class Pedidos (models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()