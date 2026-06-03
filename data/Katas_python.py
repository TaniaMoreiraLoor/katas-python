import math
from functools import reduce

# EJERCICIO 1
# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. 
# Los espacios no deben ser considerados.

def contar_letras(texto):
    frecuencia = {}

    for letra in texto:
        if letra != " ":
            if letra in frecuencia:
                frecuencia[letra] += 1
            else:
                frecuencia[letra] = 1

    return frecuencia

# Ejemplo de uso
resultado = contar_letras("Hola mundo")
print(resultado)

# EJERCICIO 2
# Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def duplicar_valores(lista):
    return list(map(lambda numero: numero * 2, lista))

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
resultado = duplicar_valores(numeros)

print(resultado)

# EJERCICIO 3
# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
# (En este ejemplo hay que tener cuidado porque si buscamos la palabra "casa" dentro de la lista que hemos dado eso es lo que nos va a devolver).
# (Sin embargo si queremos todas las palabras relacionadas con la palabra objetivo deberiamos solo poner "cas").

def buscar_palabras(lista_palabras, palabra_objetivo):
    resultado = []

    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            resultado.append(palabra)

    return resultado

# Ejemplo de uso
palabras = ["casa", "casita", "perro", "caserón", "gato"]

resultado = buscar_palabras(palabras, "cas")
print(resultado)

# EJERCICIO 4
# Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def calcular_diferencia(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

# Ejemplo de uso
lista1 = [10, 20, 30]
lista2 = [1, 2, 3]

resultado = calcular_diferencia(lista1, lista2)

print(resultado)

# EJERCICIO 5
# Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. 
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
# Si es así, el estado será "aprobado", de lo contrario, será "suspenso". 
# La función debe devolver una tupla que contenga la media y el estado.

def evaluar_notas(lista_notas, nota_aprobado=5):
    media = sum(lista_notas) / len(lista_notas)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return (media, estado)

# Ejemplo de uso
notas = [4, 9, 6, 5]

resultado = evaluar_notas(notas)

print(resultado)

# EJERCICIO 6
# Escribe una función que calcule el factorial de un número de manera recursiva

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
    
# Ejemplo de uso
print(factorial(5))

# EJERCICIO 7
# Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    return list(map(str, lista_tuplas))

# Ejemplo de uso
datos = [
    ("Tania", 25),
    ("Juan", 30),
    ("Ana", 22)
]

resultado = tuplas_a_strings(datos)

print(resultado)

# EJERCICIO 8
# Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, 
# maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

try:
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))

    resultado = numero1 / numero2

    print(f"La división es: {resultado}")
    print("La división fue exitosa.")

except ValueError:
    print("Error: Debes introducir valores numéricos.")

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

# EJERCICIO 9
# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def filtrar_mascotas(lista_mascotas):
    mascotas_prohibidas = [
        "Mapache",
        "Tigre",
        "Serpiente Pitón",
        "Cocodrilo",
        "Oso"
    ]

    return list(
        filter(
            lambda mascota: mascota not in mascotas_prohibidas,
            lista_mascotas
        )
    )

# Ejemplo de uso
mascotas = [
    "Perro",
    "Gato",
    "Mapache",
    "Conejo",
    "Oso",
    "Loro"
]

resultado = filtrar_mascotas(mascotas)

print(resultado)

# EJERCICIO 10
# Escribe una función que reciba una lista de números y calcule su promedio. 
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
# (Para este ejercicio he usado "raise", que sirve para lanzar una excepción cuando se cumple una condición).

class ListaVaciaError(Exception):
    pass


def calcular_promedio(lista):
    if len(lista) == 0:
        raise ListaVaciaError("La lista está vacía.")

    return sum(lista) / len(lista)


try:
    numeros = [10, 20, 30, 40]

    promedio = calcular_promedio(numeros)

    print(f"El promedio es: {promedio}")

except ListaVaciaError as error:
    print(f"Error: {error}")

# EJERCICIO 11
# Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado 
# (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

try:
    edad = int(input("Introduce tu edad: "))

    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120 años.")

    print(f"Tu edad es {edad} años.")

except ValueError as error:
    print(f"Error: {error}")

# EJERCICIO 12
# Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase):
    palabras = frase.split()

    return list(map(len, palabras))

# Ejemplo de uso
resultado = longitud_palabras("Hola me llamo Tania")

print(resultado)

# EJERCICIO 13
# Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. 
# Las letras no pueden estar repetidas .Usa la función map()

def letras_mayus_minus(caracteres):
    letras_unicas = set(caracteres)

    return list(map(lambda letra: (letra.upper(), letra.lower()), letras_unicas))

# Ejemplo de uso
resultado = letras_mayus_minus("Tania")

print(resultado)

# EJERCICIO 14
# Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def palabras_por_letra(lista_palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))

# Ejemplo de uso
palabras = ["casa", "perro", "camisa", "gato", "coche"]

resultado = palabras_por_letra(palabras, "c")

print(resultado)

# EJERCICIO 15
# Crea una función lambda que sume 3 a cada número de una lista dada.

sumar_tres = lambda numero: numero + 3

numeros = [1, 2, 3, 4, 5]

resultado = list(map(sumar_tres, numeros))

print(resultado)

# EJERCICIO 16
# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()
# (Este ejercicio es muy parecido al "14", la diferencia es que aquí filtramos por la longitud (len) y en el "14" filtrábamos por la letra inicial (startswith)).

def palabras_largas(texto, n):
    palabras = texto.split()

    return list(filter(lambda palabra: len(palabra) > n, palabras))

# Ejemplo de uso
resultado = palabras_largas("Mi perro es un mastin enorme", 4)

print(resultado)

# EJERCICIO 17
# Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

def lista_a_numero(lista_digitos):
    return reduce(lambda x, y: x * 10 + y, lista_digitos)

# Ejemplo de uso
resultado = lista_a_numero([5, 7, 2])

print(resultado)

# EJERCICIO 18
# Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) 
# y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

def estudiantes_destacados(estudiantes):
    return list(
        filter(
            lambda estudiante: estudiante["calificacion"] >= 90,
            estudiantes
        )
    )

# Ejemplo de uso
estudiantes = [
    {"nombre": "Tania", "edad": 20, "calificacion": 95},
    {"nombre": "Lucero", "edad": 22, "calificacion": 80},
    {"nombre": "Jonna", "edad": 21, "calificacion": 90},
    {"nombre": "Annel", "edad": 19, "calificacion": 85}
]

resultado = estudiantes_destacados(estudiantes)

print(resultado)

# EJERCICIO 19
# Crea una función lambda que filtre los números impares de una lista dada.

def filtrar_impares(lista):
    return list(filter(lambda numero: numero % 2 != 0, lista))

# Ejemplo de uso
numeros = [112, 2, 25, 139, 5, 6, 55, 8, 9]

resultado = filtrar_impares(numeros)

print(resultado)

# EJERCICIO 20
# Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def filtrar_enteros(lista):
    return list(filter(lambda elemento: isinstance(elemento, int), lista))

# Ejemplo de uso
datos = [1, "hola", 5, "perro", 10, "gato", 20]

resultado = filtrar_enteros(datos)

print(resultado)

# EJERCICIO 21
# Crea una función que calcule el cubo de un número dado mediante una función lambda

def calcular_cubo(numero):
    cubo = lambda x: x ** 3
    return cubo(numero)

# Ejemplo de uso
resultado = calcular_cubo(9)

print(resultado)

# EJERCICIO 22
# Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)

# Ejemplo de uso
numeros = [2, 3, 4, 5]

resultado = producto_total(numeros)

print(resultado)

# EJERCICIO 23
# Concatena una lista de palabras.Usa la función reduce() .
def concatenar_palabras(lista_palabras):
    return reduce(lambda x, y: x + y, lista_palabras)

# Ejemplo de uso
palabras = ["Hola", " ", "soy", " ", "Tania"]

resultado = concatenar_palabras(palabras)

print(resultado)

# EJERCICIO 24
# Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)

# Ejemplo de uso
numeros = [20, 5, 3]

resultado = diferencia_total(numeros)

print(resultado)

# EJERCICIO 25
# Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto):
    return len(texto)

# Ejemplo de uso
resultado = contar_caracteres("Hola mundo")

print(resultado)

# EJERCICIO 26
# Crea una función lambda que calcule el resto de la división entre dos números dados.

def calcular_resto(numero1, numero2):
    resto = lambda x, y: x % y
    return resto(numero1, numero2)

# Ejemplo de uso
resultado = calcular_resto(10, 3)

print(resultado)

# EJERCICIO 27
# Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(lista):
    return sum(lista) / len(lista)

# Ejemplo de uso
numeros = [10, 20, 30, 40]

resultado = calcular_promedio(numeros)

print(resultado)

# EJERCICIO 28
# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = set()

    for elemento in lista:
        if elemento in vistos:
            return elemento

        vistos.add(elemento)

    return None

# Ejemplo de uso
numeros = [1, 3, 5, 2, 3, 8, 5]

resultado = primer_duplicado(numeros)

print(resultado)

# EJERCICIO 29
# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarar_dato(valor):
    texto = str(valor)

    return "#" * (len(texto) - 4) + texto[-4:]

# Ejemplo de uso
resultado = enmascarar_dato(123456789)

print(resultado)

# EJERCICIO 30
# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def es_anagrama(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

# Ejemplo de uso
resultado = es_anagrama("roma", "amor")

print(resultado)

# EJERCICIO 31
# Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. 
# Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
# (Este ejercicio lleva trampa asi que los nombres que se ingrsen deben ser sin espacios porque de ponerlos la función lo toma como falso y no lo añade a la lista)

def buscar_nombre():
    nombres = input("Introduce varios nombres separados por comas: ").split(",")

    nombre_buscar = input("Introduce el nombre que deseas buscar: ")

    if nombre_buscar in nombres:
        print(f"El nombre '{nombre_buscar}' fue encontrado.")
    else:
        raise ValueError(f"El nombre '{nombre_buscar}' no fue encontrado.")


try:
    buscar_nombre()

except ValueError as error:
    print(error)

# EJERCICIO 32
# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado 
# si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
# (En este caso aunque no se pedia he puesto "strip y lower" para que la busqueda sea mas robusta y no haya problemas con espacios, mayusculas o minusculas).

def buscar_empleado(nombre_completo, empleados):
    nombre_completo = nombre_completo.strip().lower()

    for empleado in empleados:
        if empleado["nombre"].strip().lower() == nombre_completo:
            return empleado["puesto"]

    return "La persona no trabaja aquí."

# Ejemplo de uso
empleados = [
    {"nombre": "Jonnthan Garcia", "puesto": "Analista de Datos"},
    {"nombre": "Lucero Castro", "puesto": "Desarrollador"},
    {"nombre": "Tania Moreira", "puesto": "Diseñadora"}
]

resultado = buscar_empleado("Lucero castro", empleados)

print(resultado)

# EJERCICIO 33
# Crea una función lambda que sume elementos correspondientes de dos listas dadas.
def sumar_listas(lista1, lista2):
    return list(map(lambda x, y: x + y, lista1, lista2))

# Ejemplo de uso
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

resultado = sumar_listas(lista1, lista2)

print(resultado)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 34
# Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.

class Arbol:
    # 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    # 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
    def crecer_tronco(self):
        self.tronco += 1

    # 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
    def nueva_rama(self):
        self.ramas.append(1)

    # 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
    def crecer_ramas(self):
        self.ramas = list(map(lambda rama: rama + 1, self.ramas))

    # 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
    def quitar_rama(self, posicion):
        self.ramas.pop(posicion)

    # 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
    def info_arbol(self):
        return f"Longitud del tronco: {self.tronco}. Número de ramas: {len(self.ramas)}. Longitudes de las ramas: {self.ramas}" 

# 1. Crear un árbol.    
arbol = Arbol()

# 2. Hacer crecer el tronco del árbol una unidad.
arbol.crecer_tronco()

# 3. Añadir una nueva rama al árbol.
arbol.nueva_rama()

# 4. Hacer crecer todas las ramas del árbol una unidad.
arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas al árbol.
arbol.nueva_rama()
arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2.
arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol.
print(arbol.info_arbol())

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 36
# Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
# Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    # 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No tienes saldo suficiente.")
        else:
            self.saldo -= cantidad

    # 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError("El otro usuario no tiene saldo suficiente.")
        else:
            otro_usuario.saldo -= cantidad
            self.saldo += cantidad

    # 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

try:
    # 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)

    # 2. Agregar 20 unidades de saldo de "Bob".
    bob.agregar_dinero(20)

    # 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia". (Aquí hay que aclarar que la transferencia no fue hecha debido a que Bob tiene saldo insuficiente).
    alicia.transferir_dinero(bob, 80)

    # 4. Retirar 50 unidades de saldo a "Alicia".
    alicia.retirar_dinero(50)

    print(alicia.saldo)
    print(bob.saldo)

except ValueError as error:
    print(error)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 37
# Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,reemplazar_palabras , eliminar_palabra . 
# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .

# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
def contar_palabras(texto):
    palabras = texto.split()
    resultado = {}

    for palabra in palabras:
        if palabra in resultado:
            resultado[palabra] += 1
        else:
            resultado[palabra] = 1

    return resultado

print(contar_palabras("hola mundo hola"))

# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

print(reemplazar_palabras("hola mundo", "mundo", "Python"))

# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
def eliminar_palabra(texto, palabra):
    return texto.replace(palabra, "")

print(eliminar_palabra("hola mundo", "mundo"))

# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.

def procesar_texto(texto, opcion, *args):

    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])

    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])

    else:
        return "Opción no válida"

# Ejemplo de uso    
texto = "hola mundo hola python"

print(procesar_texto(texto, "contar"))

print(procesar_texto(texto, "reemplazar", "hola", "adios"))

print(procesar_texto(texto, "eliminar", "python"))

# EJERCICIO 38
# Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

hora = int(input("Introduce la hora (0-23): "))

if hora >= 6 and hora < 12:
    print("Es de día")

elif hora >= 12 and hora < 20:
    print("Es de tarde")

elif hora >= 20 and hora <= 23:
    print("Es de noche")

elif hora >= 0 and hora < 6:
    print("Es de noche")

else:
    print("Hora no válida")

# EJERCICIO 39
# Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
# 0 - 69 insuficiente
# 70 - 79 bien
# 80 - 89 muy bien
# 90 - 100 excelente

calificacion = float(input("Introduce la calificación: "))

if 0 <= calificacion <= 69:
    print("Insuficiente")

elif 70 <= calificacion <= 79:
    print("Bien")

elif 80 <= calificacion <= 89:
    print("Muy bien")

elif 90 <= calificacion <= 100:
    print("Excelente")

else:
    print("Calificación no válida")

# EJERCICIO 40
# Escribe una función que tome dos parámetros: 
# figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

def calcular_area(figura, datos):

    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        radio = datos[0]
        return math.pi * radio ** 2

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    else:
        return "Figura no válida"
    
# Ejemplo de uso
print(calcular_area("rectangulo", (5, 4)))
print(calcular_area("circulo", (3,)))
print(calcular_area("triangulo", (10, 5)))

# EJERCICIO 41
# En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra 
# en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:

precio = float(input("Introduce el precio del artículo: "))

cupon = input("¿Tienes un cupón de descuento? (si/no): ")

if cupon.lower() == "si":

    descuento = float(input("Introduce el valor del cupón: "))

    if descuento > 0:

        precio_final = precio - descuento

        if precio_final < 0:
            precio_final = 0

        print("El precio final es:", precio_final)

    else:
        print("El descuento no es válido")

else:
    print("El precio final es:", precio)
