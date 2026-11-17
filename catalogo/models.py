from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    #create your models here.
# class Libro(models.Model):
#     ESTADOS = [
#     ('ARCHIVADO', 'Archivado'),
#     ('PERDIDO', 'Perdido'),
#     ('PRESTADO', 'Prestado'),
#     ('DISPONIBLE', 'Disponible'),
# ]
#     estado = models.CharField(max_length=20, choices=ESTADOS, default='DISPONIBLE')
#     titulo = models.CharField(max_length=200)
#     sinopsis = models.TextField(blank=True)
#     autor = models.CharField(max_length=200)
#     anio = models.IntegerField()
#     disponible = models.BooleanField(default=True)
#     precio = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True)
#     genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
#     editorial = models.ForeignKey(
#     Editorial,
#     on_delete=models.CASCADE,
#     null=True,
#     blank=True
# )
    
    
#     autores = models.ManyToManyField(Autor)
    
#     def __str__(self):
#         return self.titulo


class Libro(models.Model):

    ESTADOS = [
        ('ARCHIVADO', 'Archivado'),
        ('PERDIDO', 'Perdido'),
        ('PRESTADO', 'Prestado'),
        ('DISPONIBLE', 'Disponible'),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='DISPONIBLE'
    )

    titulo = models.CharField(max_length=200)
    sinopsis = models.TextField(blank=True)
    anio = models.IntegerField()
    disponible = models.BooleanField(default=True)
    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True
    )

    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
#     usuario = models.ForeignKey(
#     User,
#     on_delete=models.CASCADE,
#     null=True,
#     blank=True
# )

    usuario = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)

    autores = models.ManyToManyField(Autor)

    def __str__(self):
        return self.titulo