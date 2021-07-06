from django.shortcuts import  render
from .models import Producto
from .services import get_initTrxTBK
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import ProductoSerializer

# Create your views here.

def tienda(request):

    productos = Producto.objects.all()
  
    return render(request, "tienda/tienda.html", {"productos": productos})

def tbk(request):
    data ={
        'resultado':get_initTrxTBK()
    }
    return render(request, 'tienda/initTrxTbk.html',data)


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer