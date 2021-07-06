from django.db import router
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos',views.ProductoViewSet)


urlpatterns = [
    path('', views.tienda, name="Tienda"),
    path('tbk/', views.tbk, name="tbk"),
    path('api/',include(router.urls) ),
] 
