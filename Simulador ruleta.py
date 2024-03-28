import random
import sys

# if len(sys.argv) != 3 or sys.argv[1] != "-n":
#     print("Uso: python programa.py -n <num_valores>")
#     sys.exit(1)


# Obtener el número de valores de los argumentos de la línea de comandos
# num_tiradas = int(sys.argv[0])
# num_corridas = int(sys.argv[1])

num_tiradas = 100
num_corridas = 5
numero = int(input('ingrese numero: '))

frecuencias={}
for y in range(num_corridas):
    valores = [random.randint(0, 36) for _ in range(num_tiradas)]
    
    # Calcular la frecuencia relativa de cada valo"
    frecuencias["tirada: " + str(y)] = {"frecuencia relativa": valores.count(numero) / num_tiradas, 
                           "frecuencia_absoluta": valores.count(numero)}


print(frecuencias, "/n")
    



#     return frecuencia_absoluta, frecuencia_relativa

# # Calcular frecuencias iniciales
# frecuencia_absoluta, frecuencia_relativa = calcular_frecuencias(valores)

# # Imprimir los resultados iniciales
# print("Valores generados:", valores)
# print("Frecuencia absoluta de 0:", frecuencia_absoluta[0])
# print("Frecuencia absoluta de 1:", frecuencia_absoluta[1])
# print("Frecuencia relativa de 0:", frecuencia_relativa[0])
# print("Frecuencia relativa de 1:", frecuencia_relativa[1])

# # Simular la adición de nuevos valores
# while True:
#     nuevo_valor = random.randint(0, 1)
#     valores.append(nuevo_valor)
#     frecuencia_absoluta, frecuencia_relativa = calcular_frecuencias(valores)
#     print("\nNuevo valor generado:", nuevo_valor)
#     print("Valores generados:", valores)
#     print("Frecuencia absoluta de 0:", frecuencia_absoluta[0])
#     print("Frecuencia absoluta de 1:", frecuencia_absoluta[1])
#     print("Frecuencia relativa de 0:", frecuencia_relativa[0])
#     print("Frecuencia relativa de 1:", frecuencia_relativa[1])
