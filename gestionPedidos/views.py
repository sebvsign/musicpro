from django.http.response import HttpResponse
from django.shortcuts import render
from gestionPedidos.models import Articulos
# Create your views here.



def home(request):
    return render(request, "gestionPedidos/home.html")



# LO DE ABAJO SOLO ES PRUEBAS 


def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:
        #mensaje = "Articulo buscado: %r" %request.GET["prd"]
        producto = request.GET["prd"]

        if len(producto)>20:
            mensaje = "Texto de busqueda demasiado largo"
        else:
            articulos = Articulos.objects.filter(nombre__icontains = producto)
            return render(request, "resultados_busqueda.html", {"articulos": articulos, "query": producto})

    else:
        mensaje = "no has introducido nada :p"

    return HttpResponse(mensaje)


def contacto (request):
    if request.method == "POST":
        return render(request, "gracias.html")

    return render(request, "contacto.html")




