# Enunciado
# Siguiendo la presentación UD9. de Estructuras en algoritmos de Python, debemos mostrar las tablas de multiplicar del 1 al 10.
# Podemos utilizar un bucle anidado.
# también puedes hacer una segunda versión utilizando programación funcional.

# Entrega.
# Comparte el enlace de tu Github en el chat y añade tu enlace a esta tarea.

lista = []
for n in range(1,11):
    lista.append(n)

def tabla(x):
    for f in range(1,11): 
        print(f'{x} x {f} = {x * f}')

pares = filter(tabla, lista)
print(list(pares))

