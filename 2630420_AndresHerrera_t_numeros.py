#1. PROPÓSITO
#Que el estudiante practique el uso de los tipos de datos numéricos y booleanos en Python (int, float y bool):
# operaciones aritméticas, comparaciones y operadores lógicos para tomar decisiones. Además, que pueda validar
# entradas (rangos, división entre cero) y documentar sus soluciones con descripción, casos de prueba y conclusiones.

#2. PORTADA
"""
Enteros, flotantes y booleanos en Python

Estudiante: Andrés Manuel Herrera Compean
Matrícula: 2630420
Grupo: I-M1

"""
#4. RESUMEN EJECUTIVO (COMENTARIOS EN EL .py)
"""
¿Qué son los tipos int y float en Python y en qué se diferencian?
    int es un número entero, sin decimales (5, -3, 0) y float es un número con punto decimal (3.14, 35.5).
    El int se usa para contar cosas (puntaje, cantidad) y el float para medir cosas con decimales
    (temperatura, dinero, peso). Al dividir con / siempre sale float, aunque sea 21 / 3 = 7.0.

¿Qué es un booleano (True/False) y cómo se obtiene a partir de comparaciones?
    Un booleano (bool) solo puede valer True o False. Se obtiene al comparar con <, >, <=, >=, == o !=,
    por ejemplo 35.5 >= 30.0 da True. Y se pueden juntar con and, or y not.

¿Por qué es importante validar rangos y evitar división entre cero?
    Porque si el programa recibe datos que no tienen sentido (horas negativas, una estatura de 0)
    da resultados raros o se rompe, por ejemplo con ZeroDivisionError al dividir entre cero.

¿Qué cubrirá tu documento?: descripción de cada problema, diseño de entradas y salidas, validaciones
aplicadas y uso de enteros, flotantes y booleanos para tomar decisiones.
    Cubre 6 problemas (temperatura, pago con horas extra, descuento, estadísticas de 3 enteros,
    préstamo y BMI) cada uno con sus entradas, salidas, validaciones y 3 casos de prueba.
"""
#PRINCIPIOS Y BUENAS PRÁCTICAS DE PROGRAMACIÓN
"""
- Usar el tipo correcto: int para contadores y puntajes, float para cantidades con decimales.
- Guardar los resultados intermedios en variables en lugar de repetir la misma operación.
- Validar los datos antes de operar (que horas y salarios no sean negativos, que no haya división entre cero).
- Usar nombres de variables claros y mensajes fáciles de entender para el usuario.
- Documentar qué significa true y qué significa false en cada problema (por ejemplo,
  "High temperature: true" quiere decir que hay 30.0 °C o más).
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
(1) 7.1 Problem 1: Temperature converter and range flag
Descripción:
    Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin. Además, determina un valor
    booleano is_high_temperature que sea true si la temperatura en Celsius es mayor o igual que 30.0 y
    false en caso contrario.

Entradas:
    - temp_c (float; temperatura en °C).

Salidas:
    - "Fahrenheit:" <temp_f>
    - "Kelvin:" <temp_k>
    - "High temperature:" true|false

Validaciones:
    - Verificar que temp_c pueda convertirse a float.
    - No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).

Test cases:
    1) Normal: temp_c_text = "35.5"
       Fahrenheit: 95.9
       Kelvin: 308.65
       High temperature: true
    2) Border: temp_c_text = "30.0" (justo el límite de temperatura alta)
       Fahrenheit: 86.0
       Kelvin: 303.15
       High temperature: true
    3) Error: temp_c_text = "-300.0" (el Kelvin sale negativo)
       Error: invalid input
"""
print("PROGRAM 1")
HIGH_TEMP_LIMIT = 30.0

temp_c_text = "35.5"

is_number = temp_c_text.replace("-", "", 1).replace(".", "", 1).isdigit()

if is_number:
    temp_c = float(temp_c_text)
    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15
    is_high_temperature = temp_c >= HIGH_TEMP_LIMIT

    if temp_k < 0.0:
        print("Error: invalid input")
    else:
        print("Fahrenheit: " + str(round(temp_f, 2)))
        print("Kelvin: " + str(round(temp_k, 2)))
        print("High temperature: " + str(is_high_temperature).lower())
else:
    print("Error: invalid input")

"""
(2) 7.2 Problem 2: Work hours and overtime payment
Descripción:
    Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a hourly_rate (float).
    Las horas extra (> 40) se pagan al 150% de la tarifa normal. Además, genera un booleano has_overtime
    que indique si el trabajador hizo horas extra.

Entradas:
    - hours_worked (float; horas trabajadas en la semana).
    - hourly_rate (float; pago por hora).

Salidas:
    - "Regular pay:" <regular_pay>
    - "Overtime pay:" <overtime_pay>
    - "Total pay:" <total_pay>
    - "Has overtime:" true|false

Validaciones:
    - hours_worked >= 0
    - hourly_rate > 0
    - Si alguno no cumple, mostrar "Error: invalid input".

Test cases:
    1) Normal: hours_worked = 45.0, hourly_rate = 100.0
       Regular pay: 4000.0
       Overtime pay: 750.0
       Total pay: 4750.0
       Has overtime: true
    2) Border: hours_worked = 40.0, hourly_rate = 100.0 (justo 40 horas, sin extras)
       Regular pay: 4000.0
       Overtime pay: 0.0
       Total pay: 4000.0
       Has overtime: false
    3) Error: hours_worked = -5.0, hourly_rate = 100.0 (horas negativas)
       Error: invalid input
"""
print("PROGRAM 2")
MAX_REGULAR_HOURS = 40.0
OVERTIME_MULTIPLIER = 1.5

hours_worked = 45.0
hourly_rate = 100.0

if hours_worked >= 0 and hourly_rate > 0:
    regular_hours = min(hours_worked, MAX_REGULAR_HOURS)
    overtime_hours = max(hours_worked - MAX_REGULAR_HOURS, 0.0)

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > MAX_REGULAR_HOURS

    print("Regular pay: " + str(regular_pay))
    print("Overtime pay: " + str(overtime_pay))
    print("Total pay: " + str(total_pay))
    print("Has overtime: " + str(has_overtime).lower())
else:
    print("Error: invalid input")

"""
(3) 7.3 Problem 3: Discount eligibility with booleans
Descripción:
    Determina si un cliente obtiene un descuento en su compra. La regla es:
    - Tiene descuento si:
        - is_student es true OR
        - is_senior es true OR
        - purchase_total >= 1000.0
    Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.

Entradas:
    - purchase_total (float; total de la compra).
    - is_student_text (string; "YES" o "NO").
    - is_senior_text (string; "YES" o "NO").

Salidas:
    - "Discount eligible:" true|false
    - "Final total:" <final_total>

Validaciones:
    - purchase_total >= 0.0
    - Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, is_senior.
    - Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".

Test cases:
    1) Normal: purchase_total = 500.0, is_student_text = "yes", is_senior_text = "no"
       Discount eligible: true
       Final total: 450.0
    2) Border: purchase_total = 1000.0, is_student_text = "NO", is_senior_text = "NO" (justo 1000.0)
       Discount eligible: true
       Final total: 900.0
    3) Error: purchase_total = 500.0, is_student_text = "maybe" (no es YES ni NO)
       Error: invalid input
"""
print("PROGRAM 3")
DISCOUNT_FACTOR = 0.9
MIN_PURCHASE_FOR_DISCOUNT = 1000.0

purchase_total = 500.0
is_student_text = "yes"
is_senior_text = "no"

is_student_text = is_student_text.upper()
is_senior_text = is_senior_text.upper()

valid_total = purchase_total >= 0.0
valid_student = is_student_text == "YES" or is_student_text == "NO"
valid_senior = is_senior_text == "YES" or is_senior_text == "NO"

if valid_total and valid_student and valid_senior:
    is_student = is_student_text == "YES"
    is_senior = is_senior_text == "YES"

    discount_eligible = is_student or is_senior or (purchase_total >= MIN_PURCHASE_FOR_DISCOUNT)

    if discount_eligible:
        final_total = purchase_total * DISCOUNT_FACTOR
    else:
        final_total = purchase_total

    print("Discount eligible: " + str(discount_eligible).lower())
    print("Final total: " + str(final_total))
else:
    print("Error: invalid input")

"""
(4) 7.4 Problem 4: Basic statistics of three integers
Descripción:
    Lee tres números enteros y calcula: suma, promedio (float), valor máximo, valor mínimo y un booleano
    all_even que indique si los tres números son pares.

Entradas:
    - n1 (int)
    - n2 (int)
    - n3 (int)

Salidas:
    - "Sum:" <sum_value>
    - "Average:" <average_value>
    - "Max:" <max_value>
    - "Min:" <min_value>
    - "All even:" true|false

Validaciones:
    - Verificar que los tres valores se puedan convertir a int.
    - No se requieren restricciones adicionales (se permiten negativos).

Test cases:
    1) Normal: n1_text = "4", n2_text = "7", n3_text = "10"
       Sum: 21
       Average: 7.0
       Max: 10
       Min: 4
       All even: false
    2) Border: n1_text = "-2", n2_text = "0", n3_text = "4" (negativo y cero)
       Sum: 2
       Average: 0.67
       Max: 4
       Min: -2
       All even: true
    3) Error: n1_text = "abc", n2_text = "7", n3_text = "10" (no es un entero)
       Error: invalid input
"""
print("PROGRAM 4")
n1_text = "4"
n2_text = "7"
n3_text = "10"

valid_n1 = n1_text.replace("-", "", 1).isdigit()
valid_n2 = n2_text.replace("-", "", 1).isdigit()
valid_n3 = n3_text.replace("-", "", 1).isdigit()

if valid_n1 and valid_n2 and valid_n3:
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum: " + str(sum_value))
    print("Average: " + str(round(average_value, 2)))
    print("Max: " + str(max_value))
    print("Min: " + str(min_value))
    print("All even: " + str(all_even).lower())
else:
    print("Error: invalid input")

"""
(5) 7.5 Problem 5: Loan eligibility (income and debt ratio)
Descripción:
    Determina si una persona es elegible para un préstamo con base en:
    - monthly_income (float)
    - monthly_debt (float)
    - credit_score (int)
    La regla es:
    - debt_ratio = monthly_debt / monthly_income
    - eligible es true si:
        - monthly_income >= 8000.0 AND
        - debt_ratio <= 0.4 AND
        - credit_score >= 650

Entradas:
    - monthly_income (float; ingreso mensual).
    - monthly_debt (float; pagos mensuales de deuda).
    - credit_score (int; puntaje de crédito).

Salidas:
    - "Debt ratio:" <debt_ratio>
    - "Eligible:" true|false

Validaciones:
    - monthly_income > 0.0 (evitar división entre cero).
    - monthly_debt >= 0.0
    - credit_score >= 0
    - Si no se cumple, mostrar "Error: invalid input".

Test cases:
    1) Normal: monthly_income = 12000.0, monthly_debt = 3000.0, credit_score = 700
       Debt ratio: 0.25
       Eligible: true
    2) Border: monthly_income = 8000.0, monthly_debt = 3200.0, credit_score = 650 (justo en los límites)
       Debt ratio: 0.4
       Eligible: true
    3) Error: monthly_income = 0.0, monthly_debt = 3000.0, credit_score = 700 (ingreso en cero)
       Error: invalid input
"""
print("PROGRAM 5")
MIN_INCOME = 8000.0
MAX_DEBT_RATIO = 0.4
MIN_CREDIT_SCORE = 650

monthly_income = 12000.0
monthly_debt = 3000.0
credit_score = 700

if monthly_income > 0.0 and monthly_debt >= 0.0 and credit_score >= 0:
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= MIN_INCOME and debt_ratio <= MAX_DEBT_RATIO and credit_score >= MIN_CREDIT_SCORE)

    print("Debt ratio: " + str(round(debt_ratio, 2)))
    print("Eligible: " + str(eligible).lower())
else:
    print("Error: invalid input")

"""
(6) 7.6 Problem 6: Body Mass Index (BMI) and category flag
Descripción:
    Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
    - bmi = weight_kg / (height_m * height_m)
    Además, genera booleanos para indicar:
    - is_underweight (bmi < 18.5)
    - is_normal (18.5 <= bmi < 25.0)
    - is_overweight (bmi >= 25.0)

Entradas:
    - weight_kg (float; peso en kilogramos).
    - height_m (float; estatura en metros).

Salidas:
    - "BMI:" <bmi_redondeado>
    - "Underweight:" true|false
    - "Normal:" true|false
    - "Overweight:" true|false

Validaciones:
    - weight_kg > 0.0
    - height_m > 0.0
    - Si no se cumple, mostrar "Error: invalid input".

Test cases:
    1) Normal: weight_kg = 70.0, height_m = 1.75
       BMI: 22.86
       Underweight: false
       Normal: true
       Overweight: false
    2) Border: weight_kg = 100.0, height_m = 2.0 (el BMI sale justo 25.0)
       BMI: 25.0
       Underweight: false
       Normal: false
       Overweight: true
    3) Error: weight_kg = 70.0, height_m = 0.0 (estatura en cero, evita dividir entre cero)
       Error: invalid input
"""
print("PROGRAM 6")
UNDERWEIGHT_LIMIT = 18.5
OVERWEIGHT_LIMIT = 25.0

weight_kg = 70.0
height_m = 1.75

if weight_kg > 0.0 and height_m > 0.0:
    bmi = weight_kg / (height_m * height_m)

    is_underweight = bmi < UNDERWEIGHT_LIMIT
    is_normal = bmi >= UNDERWEIGHT_LIMIT and bmi < OVERWEIGHT_LIMIT
    is_overweight = bmi >= OVERWEIGHT_LIMIT

    print("BMI: " + str(round(bmi, 2)))
    print("Underweight: " + str(is_underweight).lower())
    print("Normal: " + str(is_normal).lower())
    print("Overweight: " + str(is_overweight).lower())
else:
    print("Error: invalid input")

#Conclusiones
"""
1. Los int y float se usan juntos en casi todo, por ejemplo en el pago (horas x tarifa)
y hasta el promedio de enteros da float.

2. Las comparaciones dan True o False y con eso el programa decide con if,
como en el descuento o en si alcanza el prestamo.

3. Validar rangos es importante, si no el programa se rompe (division entre cero)
o da resultados sin sentido.

4. Con and, or y not junte varias condiciones, hay que fijarse en cuales deben cumplirse
todas y en cuales basta con una.

5. Estos patrones se repiten en nomina, descuentos, prestamos y BMI, solo cambian los datos y las reglas.
"""
#Referencias
#https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
#https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
#https://docs.python.org/3/library/functions.html
#https://www.w3schools.com/python/python_numbers.asp
#https://www.w3schools.com/python/python_booleans.asp
