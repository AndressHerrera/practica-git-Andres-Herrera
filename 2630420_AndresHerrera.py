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
(3) 7.3 Problem 3: Product catalog with dictionary
Descripción:
    Administra un pequeño catálogo de productos usando un diccionario donde:
    - clave: nombre del producto (string)
    - valor: precio unitario (float)
    El programa debe:
    1) Crear un diccionario inicial con al menos 3 productos.
    2) Leer el nombre de un producto y la cantidad a comprar.
    3) Calcular el total a pagar si el producto existe.
    4) Si el producto no existe, mostrar un mensaje de error.

Entradas:
    - product_name (string).
    - quantity (int; cantidad a comprar).

Salidas:
    - Si el producto existe:
        - "Unit price:" <unit_price>
        - "Quantity:" <quantity>
        - "Total:" <total_price>
    - Si el producto no existe:
        - "Error: product not found"

Validaciones:
    - quantity > 0.
    - product_name no vacío tras strip().
    - Verificar si product_name está en el diccionario (clave).

Test cases:
    1) Normal: product_name = "apple", quantity = 3
       Unit price: 10.0
       Quantity: 3
       Total: 30.0
    2) Border: product_name = "banana", quantity = 1 (la cantidad mínima permitida)
       Unit price: 5.5
       Quantity: 1
       Total: 5.5
    3) Error: product_name = "mango", quantity = 2 (el producto no está en el catálogo)
       Error: product not found
"""
print("PROGRAM 3")
product_prices = {"apple": 10.0, "banana": 5.5, "orange": 8.0}

product_name = "apple"
quantity = 3

product_name = product_name.strip()

if quantity > 0 and product_name != "":
    if product_name in product_prices:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity

        print("Unit price: " + str(unit_price))
        print("Quantity: " + str(quantity))
        print("Total: " + str(total_price))
    else:
        print("Error: product not found")
else:
    print("Error: invalid input")

"""
(4) 7.4 Problem 4: Student grades with dict and list
Descripción:
    Administra las calificaciones de un grupo usando un diccionario:
    - clave: nombre del estudiante (string)
    - valor: lista de calificaciones (list of float)
    El programa debe:
    1) Crear un diccionario con al menos 3 estudiantes, cada uno con una lista de calificaciones.
    2) Leer el nombre de un estudiante.
    3) Calcular el promedio de sus calificaciones.
    4) Indicar si el estudiante está aprobado (average >= 70.0) con un booleano is_passed.

Entradas:
    - student_name (string).

Salidas:
    - Si el estudiante existe:
        - "Grades:" <grades_list>
        - "Average:" <average>
        - "Passed:" true|false
    - Si el estudiante no existe:
        - "Error: student not found"

Validaciones:
    - student_name no vacío tras strip().
    - Verificar si student_name es una clave en el diccionario.
    - Verificar que la lista de calificaciones no esté vacía antes de calcular el promedio.

Test cases:
    1) Normal: student_name = "Alice"
       Grades: [90.0, 85.0, 70.0]
       Average: 81.67
       Passed: true
    2) Border: student_name = "Bob" (su promedio es justo 70.0)
       Grades: [70.0, 70.0]
       Average: 70.0
       Passed: true
    3) Error: student_name = "Zoe" (no está en el diccionario)
       Error: student not found
"""
print("PROGRAM 4")
PASSING_GRADE = 70.0

grades = {
    "Alice": [90.0, 85.0, 70.0],
    "Bob": [70.0, 70.0],
    "Carlos": [60.0, 55.0, 40.0]
}

student_name = "Alice"
student_name = student_name.strip()

if student_name == "":
    print("Error: invalid input")
else:
    if student_name in grades:
        grades_list = grades[student_name]

        if len(grades_list) == 0:
            print("Error: invalid input")
        else:
            average = sum(grades_list) / len(grades_list)
            is_passed = average >= PASSING_GRADE

            print("Grades: " + str(grades_list))
            print("Average: " + str(round(average, 2)))
            print("Passed: " + str(is_passed).lower())
    else:
        print("Error: student not found")

"""
(5) 7.5 Problem 5: Word frequency counter (list + dict)
Descripción:
    Cuenta la frecuencia de cada palabra en una oración usando:
    - Una lista de palabras.
    - Un diccionario donde:
        - clave: palabra (string)
        - valor: frecuencia (int)
    El programa debe:
    1) Leer una oración.
    2) Convertirla a minúsculas y separarla en una lista de palabras.
    3) Construir un diccionario de frecuencias.
    4) Mostrar el diccionario completo y la palabra más frecuente.

Entradas:
    - sentence (string).

Salidas:
    - "Words list:" <words_list>
    - "Frequencies:" <freq_dict>
    - "Most common word:" <word> (si hay empate, cualquier una es válida)

Validaciones:
    - sentence no vacía tras strip().
    - Manejar signos de puntuación simples si el estudiante decide hacerlo (documentar su decisión).
    - Verificar que la lista de palabras no esté vacía.
    - Decisión: se quitan las comas y los puntos con replace() antes de separar las palabras.

Test cases:
    1) Normal: sentence = "Hello world, hello Python. Hello world"
       Words list: ['hello', 'world', 'hello', 'python', 'hello', 'world']
       Frequencies: {'hello': 3, 'world': 2, 'python': 1}
       Most common word: hello
    2) Border: sentence = "Python" (una sola palabra)
       Words list: ['python']
       Frequencies: {'python': 1}
       Most common word: python
    3) Error: sentence = "   " (solo espacios)
       Error: invalid input
"""
print("PROGRAM 5")

sentence = "Hello world, hello Python. Hello world"
sentence = sentence.strip()

if sentence == "":
    print("Error: invalid input")
else:
    sentence = sentence.lower()
    sentence = sentence.replace(",", "")
    sentence = sentence.replace(".", "")

    words_list = sentence.split()
    freq_dict = {}
if len(words_list) == 0:
    print("Error: invalid input")
else:
    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    most_common_word = words_list[0]

    for word in freq_dict:
        if freq_dict[word] > freq_dict[most_common_word]:
            most_common_word = word
    print("Error: contact not found")
    print("Words list: " + str(words_list))
    print("Frequencies: " + str(freq_dict))
    print("Most common word: " + most_common_word)

"""
(6) 7.6 Problem 6: Simple contact book (dictionary CRUD)
Descripción:
    Implementa un mini "contact book" usando un diccionario donde:
    - clave: nombre de contacto (string)
    - valor: número de teléfono (string)
    El programa debe:
    1) Crear un diccionario inicial con algunos contactos.
    2) Leer una acción action_text ("ADD", "SEARCH" o "DELETE").
    3) Según la acción:
        - "ADD": lee name y phone, agrega o actualiza el contacto.
        - "SEARCH": lee name y muestra el teléfono si existe.
        - "DELETE": lee name y elimina el contacto si existe.
    4) Mostrar un mensaje indicando el resultado de la operación.

Entradas:
    - action_text (string; "ADD", "SEARCH" o "DELETE").
    - name (string; depende de la acción).
    - phone (string; solo para "ADD").

Salidas:
    - Para "ADD":
        - "Contact saved:" name, phone
    - Para "SEARCH":
        - Si existe: "Phone:" <phone>
        - Si no existe: "Error: contact not found"
    - Para "DELETE":
        - Si existe: "Contact deleted:" name
        - Si no existe: "Error: contact not found"

Validaciones:
    - Normalizar action_text a mayúsculas.
    - Verificar que action_text sea una de las tres opciones válidas.
    - name no vacío tras strip().
    - Para "ADD": phone no vacío tras strip().

Test cases:
    1) Normal: action_text = "add", name = "Diana", phone = "5559876543"
       Contact saved: Diana, 5559876543
    2) Border: action_text = "  search  ", name = "Alice", phone = "" (acción en minúsculas y con espacios de más)
       Phone: 1234567890
    3) Error: action_text = "DELETE", name = "Zoe", phone = "" (el contacto no existe)
       Error: contact not found
"""
print("PROGRAM 6")

contacts = {
    "Alice": "1234567890",
    "Bob": "9876543210",
    "Carlos": "5551234567",
}

action_text = "add"
name = "Diana"
phone = "5559876543"

action_text = action_text.strip().upper()
name = name.strip()
phone = phone.strip()

valid_action = action_text == "ADD" or action_text == "SEARCH" or action_text == "DELETE"

if not valid_action or name == "":
    print("Error: invalid input")
else:
    if action_text == "ADD":
        if phone == "":
            print("Error: invalid input")
        else:
            contacts[name] = phone
            print("Contact saved: " + name + ", " + phone)

    if action_text == "SEARCH":
        if name in contacts:
            print("Phone: " + contacts[name])
        else:
            print("Contact not found")

    if action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted: " + name)
        else:
            print("Contact not found")

#Conclusiones
"""
1. Las listas me parecieron lo mas flexible porque puedes agregar y quitar cosas,
como en la lista de compras con append().

2. Las tuplas sirven para datos que no deben cambiar, como las coordenadas de un punto,
y despues de crearlas ya no se pueden modificar.

3. Los diccionarios facilitan buscar por clave, en el catalogo y en los contactos
solo pones el nombre y sale el dato, pero hay que checar con in que la clave exista.

4. Un patron que se repite es el diccionario de listas (calificaciones) y lista + diccionario
juntos (contar palabras).
"""
#Referencias
#https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
#https://docs.python.org/3/tutorial/datastructures.html
#https://www.w3schools.com/python/python_lists.asp
#https://www.w3schools.com/python/python_tuples.asp
#https://www.w3schools.com/python/python_dictionaries.asp
