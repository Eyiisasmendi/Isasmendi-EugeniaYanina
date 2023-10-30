from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
#-----------------Modulo de registro de Categoria de Cancha--------------------------------  
class CategoriaCancha (models.Model):
    nombre = models.CharField(verbose_name="Categoria Cancha", max_length=50)
    img_cancha = models.ImageField(upload_to="canchas", null=True, blank=True, verbose_name="Imgcancha")
    
    DEPORTES =[
        (1 , "Fútbol"),
        (2 , "Rugby"),
        (3 , "Béisbol"),
        (4 , "Hockey"),
        (5 , "Voley"),
        (6 , "Tenis"),
    ]
    categoria = models.CharField(max_length=1, choices=DEPORTES)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Categoria Cancha"
        verbose_name_plural = "Categorias Canchas"
        
    def __str__(self):
        return self.nombre

#-----------------Modulo de registro de cancha--------------------------------  
class Cancha (models.Model):
    nombre =models.CharField(verbose_name="cancha", max_length=50)
    cancha_id  = models.ForeignKey(CategoriaCancha, verbose_name="Categoria Cancha", on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "cancha"
        verbose_name_plural = "canchas"
    
    def __str__(self):
        texto ="{0} ({1})"
        return texto.format(self.nombre, self.cancha_id)
    
    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.updated = timezone.now()
        super(Cancha, self).save(*args, **kwargs)

#-----------------Modulo de Registro de Cliente ------------------------------
class Cliente (models.Model):
    nombre =models.CharField(verbose_name="Cliente", max_length=50)
    apellido =models.CharField(verbose_name="Cliente", max_length=50)
    teléfono_celular = models.IntegerField(null=False, blank=False,verbose_name='Celular')
    correo_electrónico = models.EmailField()
    SOCIOS =[
        ("S1","Miembros Asociados"),
        ("S2","Miembros Afiliado"),
        ("S3","Miembros Social"),     
    ]
    socio = models.CharField(max_length=5,choices=SOCIOS)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
    def __str__(self):
        texto ="{0} {1} "
        return texto.format(self.nombre, self.apellido)

#-----------------Modulo de Registro de Reserva ------------------------------
class Reserva (models.Model):
    nombre = models.CharField(verbose_name="Reserva", max_length=50)
    cliente_id  = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE)
    cancha_id  = models.ForeignKey(Cancha, verbose_name="Cancha", on_delete=models.CASCADE)
    ESTADOS = [
        (1 , "Reservado"),
        (2 , "Confirmado"),
        (3 , "Cancelado"),
    ]
    estado =  models.CharField(max_length=1,choices=ESTADOS)
    precio = models.IntegerField(verbose_name="Precio")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_reserva = models.DateTimeField(verbose_name="Fecha de Reserva", default=timezone.now)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta :
        verbose_name="Reserva"
        verbose_name_plural = "Reservas"
        
    def __str__(self):
        return self.nombre
    
    # @admin.display(ordering="nombre")
    # def reserva(self):
    #         return format_html(f"<span style='color:green;'>{self.nombre}</span>")
