from django.contrib import admin
from .models import Cancha, CategoriaCancha, Cliente, Reserva

# Register your models here.
class CanchaAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

class CategoriaCanchaAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

class ReservaAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
    
class ClinteAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
    


admin.site.register(Cancha,CanchaAdmin)
admin.site.register(CategoriaCancha, CategoriaCanchaAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Cliente, ClinteAdmin)

