from django.contrib import admin

# Register your models herge.
from .models import Libro,Genero
admin.site.register(Libro)
admin.site.register(Genero)