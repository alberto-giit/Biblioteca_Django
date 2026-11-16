libros = [
        ('el principito', 1255, True), 
        ('Python para principiantes', 2020, False), 
        ('dune', 2015, False),          # Se agregó la coma faltante antes del año
        ('el padrino', 1400, True),     # Se limpió la coma dentro de la cadena (opcional)
]



print(libros) #1
print(len(libros)) #2
print(libros[0]) #3 ("-Dune", 2015, False)
print(libros[0][0]) #4 True

for libro in libros:
    print(libro)
    
for titulo,anio,disponible in libros:
    print(titulo)
    print(anio)
    print(disponible)
    print() # Separador entre libros
    print("-----") #linea separadora entre libros
    
frutas = ['manzana goldem', 'banana canarias', 'naranja valenciana']
for fruta in frutas:
    print(fruta)


# EJERCICIO: Modifica el programa para mostrar exclusivamente los titulos de los libros disponibles.

cont = 0

# Desempaquetamos cada tupla directamente en variables con nombres claros
for titulo, anio, disponible in libros:
    if disponible:  # Si es True
        print(titulo)
        cont += 1

print(f"Total de libros disponibles: {cont}")
# Forma corregida:
print(len([libro[0] for libro in libros if libro[2]]))


for titulo in libros:
    print(titulo)
#3       


print([libro[0] for libro in libros if libro[2]]) # Verificar los títulos de los libros disponibles después de añadir el nuevo libro
#("En un ligar de La Mancha", 1605, True)
titulos =[]
for titulo,anio, disponible in libros:
    if disponible:
       titulos.append(titulo)
print(titulos)