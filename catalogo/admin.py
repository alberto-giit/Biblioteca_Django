from django.contrib import admin

# Register your models herge.
from .models import Libro,Genero, Autor, Editorial
admin.site.register(Libro)
admin.site.register(Genero)
admin.site.register(Autor)
admin.site.register(Editorial)