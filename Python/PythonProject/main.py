# Ejercicio 3: Leer 10 números e imprimir cuantos son positivos,
# cuantos negativos y cuantos neutros.

def ejercicio_3():
    # Inicializar contadores
    conteo_positivos = 0
    conteo_negativos = 0
    conteo_neutros = 0

    # Ciclo 'Para' (for) de 1 hasta 10
    for i in range(1, 11):
        # Leer el número (usamos int() para asegurarnos de que sea un entero)
        num = int(input(f"{i}. Digite un numero: "))

        # Estructura condicional (Si - Sino)
        if num == 0:
            conteo_neutros += 1
        elif num > 0:
            conteo_positivos += 1
        else:
            conteo_negativos += 1

    # Mostrar los resultados
    print("La cantidad de positivos es:", conteo_positivos)
    print("La cantidad de negativos es:", conteo_negativos)
    print("La cantidad de neutros es:", conteo_neutros)