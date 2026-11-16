libros = [
        ('el principito', 1255, True), 
        ('Python para principiantes', 2020, False), 
        ('dune', 2015, False),
        ('el padrino', 1400, True),
]

print("\n".join(titulo for titulo,anio, disponible in libros if disponible))

palabras = ['hola', 'mundo', 'python']
resultado = '-'.join(palabras)
print(resultado)
# Salida : hola-mundo- python en teoria
# el .join  Toma cada título que generó el filtro y los une todos en una sola cadena de texto, pero poniendo un salto de línea (\n) entre cada uno.