'''
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estuiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# Las literalews se escriben x832, la variable y = x576, la variable z = x896
print(id(y))
print(id(z))

#Tipos Int, Flout, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola Alumnos"
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas (String)
miGrupoFavorito = "Guns and Roses"
caracteristicas = "The Best Rock Band"
print("Mi grupo favorito es: "+miGrupoFavorito+" "+caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# Tipos Booleanos(Bool)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# Funcion input
resultado = input("Digite un numero: ") # Regresa un dato tipo string
print(resultado)

# Corversion de la entrada de datos
numero1 = int(input("escribe el primer numero: "))
numero2 = int(input("escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ",resultado)
'''
from operator import truediv

'''
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print("El resultado de la suma es: ",suma)

resta = operandoA - operandoB
print("El resultado de la resta es: ",resta)

multiplicacion = operandoA * operandoB
print("El resultado de la multiplicacion es: ",multiplicacion)

division = operandoA / operandoB
print("El resultado de la division es: ",division)
division = operandoA // operandoB
print("El resultado de la division (int) es: ",division)
modulo = operandoA % operandoB
print("El resultado de la division o residuo (modulo) es: ",modulo)
exponente = operandoA ** operandoB
print("El resultado de la exponente es: ",exponente)
'''
'''
alto = int(input("proporciona el alto del rectangulo: "))
ancho = int(input("proporciona el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print("Area: ",area)
print("Perimetro: ",perimetro)
'''
'''
miVariable3 = 10
print(miVariable3)

# Operadores de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 -2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 *3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 /2
miVariable3 /= 2
print(miVariable3)

# Operadores de comparación

d = 4
b = 2
resultado = d == b # Comprobamos si son iguales
print(resultado)

# Operador diferente
resultado = d != b
print(resultado)

# Operador mayor que
resultado = d > b
print(resultado)

# Operador menor que
resultado = d < b
print(resultado)

# Operador menor o igual que
resultado = d <= b
print(resultado)

# Operador mayor o igual que
resultado = d >= b
print(resultado)
'''
"""a = int(input("Digite un numero: "))
print(f"El residuo de la division es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de a es: {a} es un numero PAR")
else:
    print(f"El valor de a es: {a} es un numero impar")"""
'''
edadAdulto = 18
edadPersona = int(input("Digite su edad: "))
if edadPersona >= edadAdulto:
    print(f"su edad es: {edadPersona} años, es mayor de edad")
else:
    print(f"su edad es: {edadPersona} años, es menor de edad")
    '''
'''
# Operadores Logicos
a = True
b = True
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)
'''
'''
# Ejercicio: valor dentro de un rango
valor = int(input("digite un numero dentro del rango 0 al 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f"el valor{valor} esta dentro del rango")
else:
    print(f"el valor{valor} NO esta dentro del rango")
'''
'''
# Ejercicio con el operador or, Operador Not
vacaciones = False
diaDescanso = False
if not (vacaciones or diaDescanso):
    print("tiene trabajo que hacer")
else:
    print("puede asistir al juego")
'''
# Ejercicio: Rango entre 20 y 30 años
# edad = int(input("digite su edad: "))
# veinte = edad >= 20 and edad < 30
# print(veinte)
# treinta = edad >= 30 and edad < 40
# print(treinta)
'''
if (20 <= edad < 30) or (30 <= edad < 40): # sintaxis simplificada del operador and
    print("Estas dentro del rango de los (20'0) a (30'0) años")
# if veinte:
#    print('Estas dentro del rango de los (20\'0) años')
# elif treinta:
#    print('Estas dentro del rango de los (30\'0) años')
else:
    print("No estas dentro del rango de los (20'0) a (30'0) años")
'''
'''
# Ejercicio: El mayor de dos numeros
numero1 = int(input("digite el valor para el numero1: "))
numero2 = int(input("digite el valor para el numero2: "))

if numero1 > numero2:
    print ("el numero1 es mayor")
else:
    print("el numero2 es mayor")
'''
# Ejercicio: Tienda de libros
print("Digite los siguientes datos del libro")
nombre = input("Digite el nombre del libro: ")
id = int(input("Digite el ID del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGratuito = input("Indicar si el libro es gratuito (True/False): ")
if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrecto, debe escribir True/False"
print(f'''
        Nombre: {nombre}
        ID: {id}
        precio: {precio}
        envio Gratuito?: {envioGratuito}
''')
