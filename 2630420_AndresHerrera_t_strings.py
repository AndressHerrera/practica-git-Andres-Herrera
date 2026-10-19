#1. PROPÓSITO
#Que el estudiante domine el uso de cadenas de texto (strings) en Python: creación, lectura, indexación, slicing, 
# concatenación, búsqueda, reemplazo, división, unión y formato de texto. Además, que pueda validar y transformar 
# entradas de usuario (normalización de mayúsculas/minúsculas, eliminación de espacios extra, verificación de patrones 
# simples) y documentar sus soluciones con descripción, casos de prueba y conclusiones.

#2. PORTADA
"""
Manejo de strings en Python

Estudiante: Andrés Manuel Herrera Compean
Matrícula: 2630420
Grupo: I-M1

"""
#4. RESUMEN EJECUTIVO (COMENTARIOS EN EL .py)
"""
¿Qué es un string en Python (tipo de dato, inmutabilidad)?
    un string es tipo de dato de cadena de texto en una secuencia de caracteres 
    encerrada entre comillas simples (' ') o dobles (" ").
    Y una vez que se crea un objeto o valor de tipo string, 
    su contenido no puede ser alterado

¿Qué operaciones básicas se pueden realizar: concatenar, obtener 
longitud, extraer sub-cadenas, buscar patrones, reemplazar texto?
    Concatenar:	+ o f-string	"Hola " + "mundo" → Hola mundo
    longitud:	len()	len("Hola") → 4
    Sacar un pedazo: "Hola mundo"[0:4] → Hola
    Buscar si algo está: in	"mundo" in "Hola mundo" = True
    Buscar en qué posición está: .find() "Hola mundo".find("mundo") → 5
    Reemplazar texto: .replace() "Hola mundo".replace("mundo", "Andrés") → Hola Andrés

 ¿Por qué es importante validar y normalizar texto de entrada (por ejemplo, correos, nombres, contraseñas)?
    Porque los datos pueden venir en diferentes formatos, con errores tipográficos o inconsistencias y es 
    importante para para facilitar su manejo y comparación.

¿Qué cubrirá tu documento?: descripción de cada problema, diseño de entradas y salidas, validaciones 
aplicadas y uso de métodos de string con casos de prueba (incluyendo el código).
"""
#PRINCIPIOS Y BUENAS PRÁCTICAS DE PROGRAMACIÓN
"""
- Los strings son inmutables: cualquier cambio genera una nueva cadena.
- Es buena práctica normalizar entrada con strip() y lower() antes de compararla.
- Evitar "números mágicos" en índices; documentar qué extrae cada slice.
- Usar métodos de string en lugar de reescribir lógica básica.
- Diseñar validaciones claras: primero que no esté vacío, luego el formato.
- Escribir código legible: nombres de variables claros y mensajes de error entendibles.
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
(1) 7.1 Problem 1: Full name formatter (name + initials)
Descripción:
    Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
    1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
    2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).

Entradas:
    - full_name (string; nombre completo, puede venir en mayúsculas, minúsculas o mezclado, con espacios extra).

Salidas:
    - "Formatted name: <Name In Title Case>"
    - "Initials: <X.X.X.>"

Validaciones:
    - full_name no debe estar vacío después de strip().
    - Debe contener al menos dos palabras (por ejemplo, nombre y apellido).
    - No aceptar cadenas que sean solo espacios.

Test cases:
    1) Normal: full_name = "Andres ManuEl herrera  Compean"
       Formatted name: Andres Manuel Herrera Compean
       Initials: A.M.H.C.
    2) Border: full_name = "   JUAN   carlos  TOVAR   lopez   " (mayúsculas y espacios de más)
       Formatted name: Juan Carlos Tovar Lopez
       Initials: J.C.T.L.
    3) Error: full_name = "Juan Carlos" (solo 2 palabras)
       El programa se rompe con IndexError: list index out of range,
       porque words[2] y words[3] no existen.
"""
print("PROGRAM 1")
full_name = "Andres ManuEl herrera  Compean"
full_name = full_name.strip().title()
words = full_name.split()
initials = words[0][0] + "." + words[1][0] + "." + words[2][0] + "." + words[3][0] + "."
print("Formatted name: " + " ".join(words))
print("Initials: " + initials)

"""
(2) 7.2 Problem 2: Simple email validator (structure + domain)
Descripción:
    Valida si una dirección de correo tiene un formato básico correcto:
    - Contiene exactamente un '@'.
    - Después del '@' debe haber al menos un '.'.
    - No contiene espacios en blanco.
    Si el correo es válido, también muestra el dominio (la parte después de '@').

Entradas:
    - email_text (string).

Salidas:
    - "Valid email: true" o "Valid email: false"
    - Si es válido: "Domain: <domain_part>"

Validaciones:
    - email_text no vacío tras strip().
    - Contar cuántas veces aparece '@'.
    - Verificar que no haya espacios (no debe haber " " en email_text).

Test cases:
    1) Normal: email_text = "user@example.com"
       Valid email: true
       Domain: example.com
    2) Border: email_text = "a@b.c" (el correo más corto que cumple las reglas)
       Valid email: true
       Domain: b.c
    3) Error: email_text = "user@@example.com" (dos arrobas)
       Valid email: false
       Domain: (vacío, no se muestra el dominio)
"""
print("PROGRAM 2")
email_text = "user@example.com".strip()

position = email_text.find("@")
domain = email_text[position + 1:]

check1 = email_text != ""
check2 = email_text.count("@") == 1
check3 = " " not in email_text
check4 = "." in domain

valid = check1 and check2 and check3 and check4

print("Valid email: " + str(valid).lower())
print("Domain: " + domain * valid)

"""
(3) 7.3 Problem 3: Palindrome checker (ignoring spaces and case)

Descripción:
    Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha y
    de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.

Ejemplos:
    - "Anita lava la tina" -> palíndromo.
    - "Hola mundo" -> no palíndromo.

Entradas:
    - phrase (string).

Salidas:
    - "Is palindrome: true" o "Is palindrome: false"
    - (Opcional) Mostrar también la versión normalizada de la frase.

Validaciones:
    - phrase no vacía tras strip().
    - Longitud mínima razonable después de limpiar espacios (por ejemplo, al menos 3 caracteres).

Test cases:
    1) Normal: phrase = "Anita lava la tina"
       Is palindrome: true
       Normalized: anitalavalatina
    2) Border: phrase = "Ana" (justo 3 caracteres, el mínimo permitido)
       Is palindrome: true
       Normalized: ana
    3) Error: phrase = "" (vacía)
       Is palindrome: false
       Normalized: (vacío)
"""
print("PROGRAM 3")
phrase = "Anita lava la tina".strip()

clean = phrase.lower()
clean = clean.replace(" ", "")

reverse = clean[::-1]

check_one = phrase != ""
check_two = len(clean) >= 3
check_three = clean == reverse

result = check_one and check_two and check_three

print("Is palindrome: " + str(result).lower())
print("Normalized: " + clean)

"""
(4) 7.4 Problem 4: Sentence word stats (lengths and first/last word)

Descripción:
Dada una oración, el programa debe:
    1) Normalizar espacios (quitar espacios al principio y al final).
    2) Separar las palabras por espacios.
    3) Mostrar:
    - Número total de palabras.
    - Primera palabra.
    - Última palabra.
    - Palabra más corta y más larga (por longitud).

Entradas:
    - sentence (string).

Salidas:
    - "Word count: <n>"
    - "First word: <...>"
    - "Last word: <...>"
    - "Shortest word: <...>"
    - "Longest word: <...>"

Validaciones:
    - Oración no vacía tras strip().
    - Debe contener al menos una palabra válida después de split().

Test cases:
    1) Normal: sentence = "  Esta es una palabra para el programa  "
       Word count: 7
       First word: Esta
       Last word: programa
       Shortest word: es
       Longest word: programa
    2) Border: sentence = "Hola" (una sola palabra)
       Word count: 1
       First word: Hola
       Last word: Hola
       Shortest word: Hola
       Longest word: Hola
    3) Error: sentence = "     " (solo espacios)
       El programa se rompe con IndexError: list index out of range,
       porque split() da una lista vacía y words[0] no existe.
"""
print("PROGRAM 4")
sentence = "  Esta es una palabra para el programa  ".strip()

words = sentence.split()

count = len(words)
first = words[0]
last = words[-1]
shortest = min(words, key=len)
longest = max(words, key=len)

print("Word count: " + str(count))
print("First word: " + first)
print("Last word: " + last)
print("Shortest word: " + shortest)
print("Longest word: " + longest)

"""
(5) 7.5 Problem 5: Password strength classifier

Descripción:
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas (puedes afinarlas, pero documéntalas en los comentarios).

Ejemplo de reglas:
    - Weak: longitud < 8 o todo en minúsculas o muy simple.
    - Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
    - Strong: longitud >= 8 y contiene al menos:
    - una letra mayúscula,
    - una letra minúscula,
    - un dígito,
    - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).

Entradas:
    - password_input (string).

Salidas:
    - "Password strength: weak"
    - "Password strength: medium"
    - "Password strength: strong"

Validaciones:
    - No aceptar contraseña vacía.
    - Verificar longitud con len().

Test cases:
    1) Normal: password_input = "Str0ngP@ssw0rd!"
       Password strength: strong
    2) Border: password_input = "Hola1234" (justo 8 caracteres, con mayúscula y minúscula pero sin símbolo)
       Password strength: medium
    3) Error: password_input = "" (vacía)
       Password strength: weak

Operaciones clave sugeridas:
    - Recorrer carácter por carácter.
    - Métodos: isupper(), islower(), isdigit(), isalnum().
    - Uso de banderas booleanas (has_upper, has_lower, etc.).
"""
print("PROGRAM 5")
password_input = "Str0ngP@ssw0rd!".strip()

long_enough = len(password_input) >= 8
has_upper = password_input != password_input.lower()
has_lower = password_input != password_input.upper()
has_symbol = not password_input.isalnum()

strong = long_enough and has_upper and has_lower and has_symbol
medium = long_enough and has_upper and has_lower and not strong
weak = not (strong or medium)

print("Password strength: " + "weak" * weak + "medium" * medium + "strong" * strong)

"""
(6) Descripción:
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:
    Product: <NAME> | Price: $<PRICE>
    La cadena completa debe tener exactamente 30 caracteres:
    - Si es más corta, rellena con espacios al final.
    - Si es más larga, recorta hasta 30 caracteres.

Entradas:
    - product_name (string).
    - price_value (puede leerse como string o número; conviértelo a string para mostrarlo).

Salidas:
    - "Label: <exactly 30 characters>"
    (Puedes mostrar la etiqueta entre comillas para que se vean los espacios.)

Validaciones:
    - product_name no vacío tras strip().
    - price_value debe poder convertirse a un número positivo.

Test cases:
    1) Normal: product_name = "Mouse", price_value = "25"
       Label: "Product: Mouse | Price: $25   "
    2) Border: product_name = "Teclado mecanico gamer", price_value = "899.99" (se recorta a 30)
       Label: "Product: Teclado mecanico game"
    3) Error: product_name = "Mouse", price_value = "-5" (precio negativo)
       Label: "" (no se muestra la etiqueta)

Operaciones clave sugeridas:
    - Uso de f-strings o concatenación para formar la etiqueta base.
    - len() para medir la longitud.
    - slicing para recortar: label[:30].
    - Relleno con espacios hasta alcanzar 30 caracteres.
"""
print("PROGRAM 6")
product_name = "Mouse"
price_value = "25"

product_name = product_name.strip()

name_ok = product_name != ""
price_ok = float(price_value) > 0
valid = name_ok and price_ok

label = f"Product: {product_name} | Price: ${price_value}"
label = (label + " " * 30)[:30]

print("Label: " + '"' + label * valid + '"')

#Conclusiones
"""
1. Strings en la entrada y salida de datos
Casi todo lo que el usuario escribe llega como texto y lo que el programa muestra tambien,
 entonces si no sabes manejar strings no puedes leer bien los datos ni mostrar un resultado
   ordenado. Hasta el precio, que es un numero, hay que pasarlo a texto para pegarlo en la etiqueta.

2. Cuando usar lower(), strip(), split(), join()
strip() cuando el usuario deja espacios de mas, lower() o title() para que todo tenga el
 mismo formato, split() para separar un texto en palabras y join() para volver a juntarlas. 
 Lo mejor es usarlos al principio para trabajar con el texto ya limpio.

3. Por que normalizar antes de comparar
Para la computadora “Anita” y “anita” no son lo mismo, ni “hola” y “hola “ con espacio al final. 
En el palindromo tuve que quitar espacios y pasar todo a minusculas, si no nunca me daba bien.

4. Validaciones
Una validacion es como un filtro que revisa los datos antes de usarlos. Si no 
checas que el nombre no este vacio o que el precio sea positivo, el programa se rompe o 
da resultados sin sentido.

5. Inmutabilidad y slices
Un string no se puede cambiar por dentro, replace() o lower() crean uno nuevo y 
hay que guardarlo en una variable. Los slices como texto[:30] o texto[::-1] me parecieron 
muy utiles porque con una sola linea recortas o das vuelta el texto.
"""
#Bibliografias
    #https://j2logo.com/como-concatenar-y-formatear-strings/
    #https://docs.python.org/es/3.9/library/functions.html
    #https://www.freecodecamp.org/espanol/news/metodos-de-string-de-python-explicados-con-ejemplo/
    #https://www.geeksforgeeks.org/python-strings/
    #https://www.w3schools.com/python/python_strings.asp