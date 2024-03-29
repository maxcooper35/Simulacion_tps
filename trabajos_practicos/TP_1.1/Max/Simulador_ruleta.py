import random
import sys
import matplotlib.pyplot as plt
import statistics
import math

# Verificar si se proporciona el número de valores como argumento
if len(sys.argv) != 7 or sys.argv[1] != "-c":
    print("Uso: python file.py -c XXX -n YYY -e ZZ).")
    sys.exit(1)



# Obtener la cantidad de corridas, camtodad de tiradas y valor elegido de los argumentos de la línea de comandos
cant_corridas = int(sys.argv[2])
cant_tiradas= int(sys.argv[4])
numero_elegido= int(sys.argv[6])

# Define constantes globales
fr_esperada = 1/37
prom_esperado = 37/2

varianza = (37 - 0 )**2
varianza /= 12
expected_std_dev = math.sqrt(varianza)
frecuencias_relativas_ac2=[]


for i in range(cant_corridas):

        # Generar los valores aleatorios entre 0 y 36 y almacenarlos en una lista
    valores = [random.randint(0, 37) for _ in range(cant_tiradas)]


    def calcular_frecuencias(valores, numero_elegido):

                frecuencias_relativas_ac=[]

                numero_ocurrencias = 0

                # Itera el rango de valores
                for i in range(len(valores)):
                    # Si el numero elegido coincide con el numero en el indice, incrementa el numero de ocurrencias
                    if valores[i] == numero_elegido:
                        numero_ocurrencias += 1
                    
                    # Calcula la frecuencia relativa acumulada hasta ese indice
                    frecuencia_relativa = numero_ocurrencias / (i + 1)
                    
                    # Hace un append the la frecuencia acumulada en ese indice al arreglo
                    frecuencias_relativas_ac.append(frecuencia_relativa)
                
                return frecuencias_relativas_ac

    def calcular_promedio(valores):
        
                promedios_acumulados=[]

                # Itera el rango de valores
                for i in range(1, len(valores) + 1):
                    
                    # Calcula la frecuencia relativa acumulada hasta ese indice
                    promedio = statistics.mean(valores[:i])
                    
                    # Hace un append del promedio acumulado en ese indice a la lista
                    promedios_acumulados.append(promedio)

                return promedios_acumulados
    

    def calcular_destandard(valores):
        destandar_acumulada = []

        # Es importante comenzar el rango en 2 porque stdev requiere al menos dos puntos de datos
        for i in range(1, len(valores) + 1):
            # Manejar el caso para el primer índice
            if i == 1:
                # Añadir 0 o 'None' porque la desviación estándar no está definida para un solo valor
                destandar_acumulada.append(0)
            else:
                # Calcular la desviación estándar para el segmento hasta el índice actual 'i'
                destandar = statistics.stdev(valores[:i])
                # Añadir la desviación estándar calculada a la lista
                destandar_acumulada.append(destandar)

        return destandar_acumulada


    def calcular_varianza(valores):
        varianza_acumulada = []

        # Es importante comenzar el rango en 2 porque stdev requiere al menos dos puntos de datos
        for i in range(1, len(valores) + 1):
            # Manejar el caso para el primer índice
            if i == 1:
                # Añadir 0 o 'None' porque la desviación estándar no está definida para un solo valor
                varianza_acumulada.append(0)
            else:
                # Calcular la desviación estándar para el segmento hasta el índice actual 'i'
                varianza = statistics.variance(valores[:i])
                # Añadir la varianza calculada a la lista
                varianza_acumulada.append(varianza)

        return varianza_acumulada
        


    # Calcular los estadisticos
    frecuencias_relativas_ac=(calcular_frecuencias(valores, numero_elegido))

    frecuencias_relativas_ac2.append(calcular_frecuencias(valores, numero_elegido)) 

    promedios_ac=calcular_promedio(valores)

    destandar_ac=calcular_destandard(valores)

    varianza_ac=calcular_varianza(valores)


    # Eje x: Número de repeticiones (desde 1 hasta el total de repeticiones)
    x_axis = list(range(1, len(valores) + 1))

    # Eje y: Las frecuencias relativas acumulativas calculadas
    y_axis = frecuencias_relativas_ac

    # Ahora grafica estas frecuencias acumulativas
    plt.figure(figsize=(10, 6))
    plt.plot(x_axis, y_axis, label='Frecuencia Relativa Acumulativa', color='blue')

    # Añade una línea horizontal en y = 1/36
    plt.axhline(fr_esperada, color='red', linestyle='--', label='Frecuencia Relativa esperada Teórica')

    # Etiquetando el gráfico
    plt.xlabel('Número de Repeticiones')
    plt.ylabel('Frecuencia Relativa Acumulativa')
    plt.title(f'Frecuencia Relativa Acumulativa del Número {numero_elegido} a lo Largo de las Repeticiones')

    # Añadiendo una leyenda para distinguir las líneas
    plt.legend()

    # Mostrar la cuadrícula para una mejor legibilidad
    plt.grid(True)

    #Crea archivos png
    plt.savefig('Frecuencia_Relativa_Corrida ' + str(i+1) + '.png')

    # Mostrar el gráfico
    plt.show()





    # Eje x: Número de repeticiones (desde 1 hasta el total de repeticiones)
    x_axis = list(range(1, len(valores) + 1))

    # Eje y: Los promedios acumulativos calculados
    y_axis = promedios_ac

    # Ahora grafica estos promedios acumulativos
    plt.figure(figsize=(10, 6))
    plt.plot(x_axis, y_axis, label='Promedio Acumulativo', color='blue')

    # Añade una línea horizontal en y = promedio esperado
    plt.axhline(prom_esperado, color='red', linestyle='--', label='Promedio teorico')

    # Etiquetando el gráfico
    plt.xlabel('Número de Repeticiones')
    plt.ylabel('Promedio Acumulativo')
    plt.title(f'Promedio Acumulativo y Promedio Esperado')

    # Añadiendo una leyenda para distinguir las líneas
    plt.legend()

    # Mostrar la cuadrícula para una mejor legibilidad
    plt.grid(True)

    #Crea archivos png
    plt.savefig('Promedio_Corrida ' + str(i+1) + '.png')

    # Mostrar el gráfico
    plt.show()




    # Eje x: Número de repeticiones (desde 1 hasta el total de repeticiones)
    x_axis = list(range(1, len(valores) + 1))

    # Eje y: Las desviaciones estándar acumulativas calculadas
    y_axis = destandar_ac

    # Ahora grafica estas desviaciones estándar acumulativas
    plt.figure(figsize=(10, 6))
    plt.plot(x_axis, y_axis, label='Desviación Estándar Acumulativa', color='blue')

    # Añade una línea horizontal en y = desviación estándar esperada
    plt.axhline(expected_std_dev, color='red', linestyle='--', label='Desviación Estándar Teórica')

    # Etiquetando el gráfico
    plt.xlabel('Número de Repeticiones')
    plt.ylabel('Desviación Estándar Acumulativa')
    plt.title(f'Desviación Estándar Acumulativa y Desviación Estándar Esperada')

    # Añadiendo una leyenda para distinguir las líneas
    plt.legend()

    # Mostrar la cuadrícula para una mejor legibilidad
    plt.grid(True)

    #Crea archivos png
    plt.savefig('Desvio estandard_Corrida ' + str(i+1) + '.png')

    # Mostrar el gráfico
    plt.show()



    #Genera grafico para la varianza y varianza esperada

    # Eje x: Número de repeticiones (desde 1 hasta el total de repeticiones)
    x_axis = list(range(1, len(valores) + 1))

    # Eje y: Las varianzas acumulativas calculadas
    y_axis = varianza_ac

    # Ahora grafica estas varianzas acumulativas
    plt.figure(figsize=(10, 6))
    plt.plot(x_axis, y_axis, label='Varianza Acumulativa', color='blue')

    # Añade una línea horizontal en y = varianza esperada
    plt.axhline(varianza, color='red', linestyle='--', label='Varianza Teórica')

    # Etiquetando el gráfico
    plt.xlabel('Número de Repeticiones')
    plt.ylabel('Varianza Acumulativa')
    plt.title(f'Varianza Acumulativa y Varianza Esperada')

    # Añadiendo una leyenda para distinguir las líneas
    plt.legend()

    # Mostrar la cuadrícula para una mejor legibilidad
    plt.grid(True)

    #Crea archivos png
    plt.savefig('Varianza_Corrida ' + str(i+1) + '.png')

    # Mostrar el gráfico
    plt.show()

   
# Plotea cada grafico para las distintas corridas
for i, y_values in enumerate(frecuencias_relativas_ac2, start=1):
    plt.plot(list(range(1, len(valores) + 1)), y_values, label=f'Corrida_{i}')

# Calcula la media para cada corrida
means_of_lists = [sum(lst) / len(lst) for lst in frecuencias_relativas_ac2]

# Calcula la media de medias
mean_of_means = sum(means_of_lists) / len(means_of_lists)

plt.xlabel('Repeticiones')
plt.ylabel('Frecuencia relativa')
# Añade una línea horizontal en y = varianza esperada
plt.axhline(mean_of_means, color='red', linestyle='--', label='Promedio conjunto de las corridas')
plt.title('Multiples frecuencias relativas para distintas tiradas')
plt.legend()
# Mostrar la cuadrícula para una mejor legibilidad
plt.grid(True)

#Crea archivos png
plt.savefig('Multiples_Corridas_FR.png')

#Muestra
plt.show()





