#1. PROPÓSITO
#Que el estudiante practique el uso de las estructuras de datos básicas de Python (listas, tuplas y diccionarios):
# creación, acceso, modificación, búsqueda y recorrido de elementos. Además, que pueda validar entradas
# (datos vacíos, claves que no existen, listas vacías) y documentar sus soluciones con descripción,
# casos de prueba y conclusiones.

#2. PORTADA
"""
Listas, tuplas y diccionarios en Python

Estudiante: Andrés Manuel Herrera Compean
Matrícula: 2630420
Grupo: I-M1

"""
#4. RESUMEN EJECUTIVO (COMENTARIOS EN EL .py)
"""
¿Qué es una lista, una tupla y un diccionario en Python y en qué se diferencian?
    Una lista se escribe con [ ] y guarda elementos en orden (["apple", "banana"]). Una tupla también guarda
    elementos en orden, pero se escribe con ( ) ((1.0, 2.0)). Un diccionario se escribe con { } y guarda
    parejas clave-valor ({"apple": 10.0}), y ahí se busca por la clave y no por la posición.

¿Qué significa que una lista sea mutable y una tupla inmutable?
    Mutable es que después de crearla le puedes agregar, quitar o cambiar elementos (append(), pop()).
    Inmutable es que una vez creada ya no se puede cambiar, si quieres otra tienes que crear una nueva.

¿Cómo se usan los diccionarios para asociar claves con valores?
    Cada clave apunta a un valor, por ejemplo el nombre del producto apunta a su precio. Con
    product_prices["apple"] sacas el valor y con "apple" in product_prices revisas si la clave existe.

¿Qué cubrirá tu documento?: descripción de cada problema, diseño de entradas y salidas, validaciones aplicadas
y uso de listas, tuplas y diccionarios en contextos prácticos (por ejemplo, catálogos, registros, estadísticas).
    Cubre 6 problemas (lista de compras, puntos con tuplas, catálogo de productos, calificaciones,
    frecuencia de palabras y libreta de contactos) cada uno con sus entradas, salidas, validaciones y 3 casos de prueba.
"""
#PRINCIPIOS Y BUENAS PRÁCTICAS DE PROGRAMACIÓN
"""
- Usar listas cuando necesites agregar o eliminar elementos con frecuencia.
- Usar tuplas para datos que no deben cambiar (coordenadas, fechas, configuraciones fijas).
- Usar diccionarios cuando necesites buscar información por una clave (nombre, id, código).
- Evitar modificar una lista mientras la recorres con un for, a menos que sepas exactamente lo que haces.
- Usar nombres de claves descriptivos en los diccionarios (por ejemplo, "name", "age", "price").
- Escribir código legible y mensajes claros para el usuario.
"""

#6. PLANTILLA POR PROBLEMA
"""
Antes del código de cada problema, agrega algo como (en comentarios):

Problem X: <short title>
Description: 2–4 lines explaining what the program does.

Inputs:
- ...

Outputs:
- ...

Validations:
- ...

Test cases:
1) Normal: ...
2) Border: ...
3) Error: ...
"""

#7. PROBLEMAS
"""
(1) 7.1 Problem 1: Shopping list basics (list operations)
Descripción:
    Trabaja con una lista de productos (strings). El programa debe:
    1) Crear una lista inicial de productos.
    2) Permitir agregar un nuevo producto al final.
    3) Mostrar la cantidad total de elementos en la lista.
    4) Verificar si un producto específico está en la lista (booleano is_in_list).

Entradas:
    - initial_items_text (string; por ejemplo, "apple,banana,orange").
    - new_item (string; producto a agregar).
    - search_item (string; producto a buscar).

Salidas:
    - "Items list:" <items_list>
    - "Total items:" <len_list>
    - "Found item:" true|false

Validaciones:
    - initial_items_text no vacío tras strip().
    - Separar la cadena por comas y eliminar espacios extra en cada elemento.
    - new_item y search_item no vacíos.
    - Decisión: si la lista inicial viene vacía se muestra "Error: invalid input".

Test cases:
    1) Normal: initial_items_text = "apple, banana ,orange", new_item = "grape", search_item = "banana"
       Items list: ['apple', 'banana', 'orange', 'grape']
       Total items: 4
       Found item: true
    2) Border: initial_items_text = "apple", new_item = "pear", search_item = "kiwi" (lista de un solo elemento)
       Items list: ['apple', 'pear']
       Total items: 2
       Found item: false
    3) Error: initial_items_text = "   ", new_item = "grape", search_item = "banana" (lista inicial vacía)
       Error: invalid input
"""
print("PROGRAM 1")
initial_items_text = "apple, banana ,orange"
new_item = "grape"
search_item = "banana"

initial_items_text = initial_items_text.strip()
new_item = new_item.strip()
search_item = search_item.strip()

if initial_items_text == "" or new_item == "" or search_item == "":
    print("Error: invalid input")
else:
    items_list = initial_items_text.split(",")

    for item in range(len(items_list)):
        items_list[item] = items_list[item].strip()

    items_list.append(new_item)

    is_in_list = search_item in items_list

    print("Items list: " + str(items_list))
    print("Total items: " + str(len(items_list)))
    print("Found item: " + str(is_in_list).lower())

"""
(2) 7.2 Problem 2: Points and distances with tuples
Descripción:
    Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). El programa debe:
    1) Crear dos tuplas point_a y point_b a partir de entradas numéricas.
    2) Calcular la distancia euclidiana entre ambos puntos.
    3) Crear una nueva tupla midpoint con el punto medio entre ellos.

Entradas:
    - x1, y1, x2, y2 (float; coordenadas de los puntos).

Salidas:
    - "Point A:" (x1, y1)
    - "Point B:" (x2, y2)
    - "Distance:" <distance>
    - "Midpoint:" (mx, my)

Validaciones:
    - Verificar que las 4 entradas se puedan convertir a float.
    - No se requieren restricciones adicionales en el rango.

Test cases:
    1) Normal: x1_text = "1.0", y1_text = "2.0", x2_text = "4.0", y2_text = "6.0"
       Point A: (1.0, 2.0)
       Point B: (4.0, 6.0)
       Distance: 5.0
       Midpoint: (2.5, 4.0)
    2) Border: x1_text = "0.0", y1_text = "0.0", x2_text = "0.0", y2_text = "0.0" (los dos puntos son el mismo)
       Point A: (0.0, 0.0)
       Point B: (0.0, 0.0)
       Distance: 0.0
       Midpoint: (0.0, 0.0)
    3) Error: x1_text = "abc", y1_text = "2.0", x2_text = "4.0", y2_text = "6.0" (no es un número)
       Error: invalid input
"""
print("PROGRAM 2")

x1_text = "1.0"
y1_text = "2.0"
x2_text = "4.0"
y2_text = "6.0"

try:
    x1 = float(x1_text)
    y1 = float(y1_text)
    x2 = float(x2_text)
    y2 = float(y2_text)

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A: " + str(point_a))
    print("Point B: " + str(point_b))
    print("Distance: " + str(round(distance, 2)))
    print("Midpoint: " + str(midpoint))

except ValueError:
    print("Error: invalid input")
"""

#Conclusiones
"""
1. Las listas me parecieron lo mas flexible porque puedes agregar y quitar cosas,
como en la lista de compras con append().

2. Las tuplas sirven para datos que no deben cambiar, como las coordenadas de un punto,
y despues de crearlas ya no se pueden modificar.

"""
#Referencias
#https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
#https://docs.python.org/3/tutorial/datastructures.html
#https://www.w3schools.com/python/python_lists.asp
#https://www.w3schools.com/python/python_tuples.asp
#https://www.w3schools.com/python/python_dictionaries.asp
