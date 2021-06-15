from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class CategoriaProd (models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'CategoriaProd'
        verbose_name_plural = 'CategoriasProd'

    def __str__(self):
        return self.nombre
    

class Producto (models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    categorias = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    precio = models.FloatField()
    stock = models.IntegerField()


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return 'Codigo: %s | Nombre : %s - %s | Precio: %s | Stock: %s' % (self.codigo, self.nombre, self.categorias, self.precio, self.stock)
    

