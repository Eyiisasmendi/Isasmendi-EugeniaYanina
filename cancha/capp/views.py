from django.shortcuts import render, redirect

## -----------------importaciones de Vistas para el home
from django.views.generic import TemplateView


# ----------------- importaciones de Vistas para los modelos  
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from capp.models import CategoriaCancha, Cancha, Cliente, Reserva
from capp.forms import CategoriaCanchaForm, CanchaForm, ClienteForm, ReservaForm

# Create your views here.

# ----------------- Vistas para Home -----------------
class HomeView(TemplateView):
    template_name = "capp/home.html"
    
# ----------------- Vistas para Cancha -----------------

class CanchaList(ListView):
    model = Cancha
    template_name = 'capp/cancha_list.html'

class CanchaCreate(CreateView):
    model = Cancha
    form_class = CanchaForm
    template_name = 'capp/cancha_form.html'
    success_url = reverse_lazy('cancha_list')

class CanchaUpdate(UpdateView):
    model = Cancha
    form_class = CanchaForm
    template_name = 'capp/cancha_form.html'
    success_url = reverse_lazy('cancha_list')

class CanchaDelete(DeleteView):
    model = Cancha
    template_name = 'capp/cancha_confirm_delete.html'
    success_url = reverse_lazy('cancha_list')

# ----------------- Vistas para Reserva -----------------

class ReservaList(ListView):
    model = Reserva
    template_name = 'capp/reserva_list.html'

class ReservaCreate(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'capp/reserva_form.html'
    success_url = reverse_lazy('reserva_list')

class ReservaUpdate(UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'capp/reserva_form.html'
    success_url = reverse_lazy('reserva_list')

class ReservaDelete(DeleteView):
    model = Reserva
    template_name = 'capp/reserva_confirm_delete.html'
    success_url = reverse_lazy('reserva_list')

class ReservaDetail(DetailView):
    model = Reserva
    template_name = 'capp/reserva_detail.html' 

# ----------------- Vistas para Cliente -----------------

class ClienteList(ListView):
    model = Cliente
    template_name = 'capp/cliente_list.html'

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'capp/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'capp/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'capp/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')

# ----------------- Vistas para Categoría_Cancha -----------------

class CategoriaCanchaList(ListView):
    model = CategoriaCancha
    template_name = 'capp/categoriaCancha_list.html'

class CategoriaCanchaCreate(CreateView):
    model = CategoriaCancha
    formclass = CategoriaCanchaForm
    template_name = 'capp/categoriaCancha_form.html'
    success_url = reverse_lazy('categoriaCancha_list')

class CategoriaCanchaUpdate(UpdateView):
    model = CategoriaCancha
    formclass = CategoriaCanchaForm
    template_name = 'capp/categoriaCancha_form.html'
    success_url = reverse_lazy('categoriaCancha_list')

class CategoriaCanchaDelete(DeleteView):
    model = CategoriaCancha
    template_name = 'cpapp/categoriacancha_confirm_delete.html'
    success_url = reverse_lazy('categoriaCancha_list')






#from django.contrib.auth.decorators import login_required

# @login_required
# def mi_vista_protegida(request):
#     # Lógica de la vista
