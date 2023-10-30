from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    #-------------rutas del Home ------------------------------------------
    path('', views.HomeView.as_view(), name='home'),
    
    #-------------rutas de Cancha CRUD---------------------------------
    path('cancha/', CanchaList.as_view(), name="cancha"),
    path('cancha_crear/', CanchaCreate.as_view(), name="cancha-crear"),
    path('cancha_actualizar/<int:pk>/', CanchaUpdate.as_view(), name="cancha-actualizar"),
    path('cancha_eliminar/<int:pk>/', CanchaDelete.as_view(), name="cancha-eliminar"),
    
    #-------------rutas de Reserva CRUD---------------------------------
    path('reserva/',ReservaList.as_view(), name="reserva"),
    path('reserva_crear/', ReservaCreate.as_view(), name="reserva-crear"),
    path('reserva_actualizar/<int:pk>/', ReservaUpdate.as_view(), name="reserva-actualizar"),
    path('reserva_eliminar/<int:pk>/', ReservaDelete.as_view(), name="reserva-eliminar"),
    path('reserva_detalle/<int:pk>/', ReservaDetail.as_view(), name="reserva-detalle"),
    
    #-------------rutas de Cliente CRUD---------------------------------
    path('cliente/', ClienteList.as_view(), name="cliente"),
    path('cliente_crear/', ClienteCreate.as_view(), name="cliente-crear"),
    path('cliente_actualizar/<int:pk>/', ClienteUpdate.as_view(), name="cliente-actualizar"),
    path('cliente_eliminar/<int:pk>/', ClienteDelete.as_view(), name="cliente-eliminar"),

    #-------------rutas de categoria CRUD---------------------------------
    path('categorias/', CategoriaCanchaList.as_view(), name="categorias"),
    path('categorias_crear/', CategoriaCanchaCreate.as_view(), name="categorias-crear"),
    path('categorias_actualizar/<int:pk>/', CategoriaCanchaUpdate.as_view(), name="categorias-actualizar"),
    path('categorias_eliminar/<int:pk>/', CategoriaCanchaDelete.as_view(), name="categorias-eliminar"),

]
    # path('buscador/', Busqueda.as_view(), name='buscador'),  

