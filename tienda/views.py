from django.shortcuts import  render
from .models import Producto
from .services import get_initTrxTBK
# Create your views here.

def tienda(request):

    productos = Producto.objects.all()
  
    return render(request, "tienda/tienda.html", {"productos": productos})

def tbk(request):
    data ={
        'resultado':get_initTrxTBK()
    }
    return render(request, 'tienda/tienda.html',data)