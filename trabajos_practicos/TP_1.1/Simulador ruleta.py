import json
import random
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description="Simulador de ruleta")
parser.add_argument("-c", default=37, type=int, help="Número de tiradas")
parser.add_argument("-n", default=1, type=int, help="Número de corridas")
parser.add_argument("-e", required=True, type=int, choices=range(0, 37), help="Número elegido")

args = parser.parse_args()
num_tiradas = args.c
num_corridas = args.n
numero = args.e

corridas={}
for y in range(num_corridas):
    tiradas={}
    valores = []
    suma = 0
    for c in range(1, num_tiradas+1, 1):
        ruleta = random.randint(0, 37)        
        valores.append(ruleta)

        suma = suma + ruleta
        fr = round((valores.count(numero) / c),4)
        vp = round((suma / c),4)
        vz = round((sum([(x - vp)**2 for x in valores]) / c),4)
        de = round((vz**0.5),4)
        tiradas[c] = {"frecuencia relativa": fr, "valor promedio": vp,
                         "varianza": vz, "desviacion estandar": de}
        
    corridas[y] = tiradas

with open('trabajos_practicos/TP_1.1/datos.json', 'w') as jf: 
    json.dump(corridas, jf, ensure_ascii=False, indent=2)

x = list(range(num_tiradas))
#valores en y
y_fr = [corridas[0][i]['frecuencia relativa'] for i in range(1, num_tiradas+1, 1)]
y_vp = [corridas[0][i]['valor promedio'] for i in range(1, num_tiradas+1, 1)]
y_vz = [corridas[0][i]['varianza'] for i in range(1, num_tiradas+1, 1)]
y_de = [corridas[0][i]['desviacion estandar'] for i in range(1, num_tiradas+1, 1)]
#valores esperados
c_fr = [1/37 for i in range(num_tiradas)]
c_vp = [18 for i in range(num_tiradas)]
c_vz = [324 for i in range(num_tiradas)]
c_de = [18 for i in range(num_tiradas)]

# Crear la figura y los subgráficos
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(18, 9))

# Graficar frecuencia relativa
axs[0][0].plot(x, y_fr, color='blue')
axs[0][0].plot(c_fr, label='Valor esperado', linestyle='--', color='red')
axs[0][0].set_title('Gráfico 1: Frecuencia relativa')
axs[0][0].set_xlabel('Tiradas')
axs[0][0].set_ylabel('Frecuencia relativa')

# Graficar valor primedio
axs[0][1].plot(x, y_vp, color='blue')
axs[0][1].plot(c_vp, label='Valor esperado', linestyle='--', color='red')
axs[0][1].set_title('Gráfico 2: Valor promedio')
axs[0][1].set_xlabel('Tiradas')
axs[0][1].set_ylabel('Valor promedio')

# Graficar varianza
axs[1][0].plot(x, y_vz, color='blue')
axs[1][0].plot(c_vz, label='Valor esperado', linestyle='--', color='red')
axs[1][0].set_title('Gráfico 3: Varianza')
axs[1][0].set_xlabel('Tiradas')
axs[1][0].set_ylabel('Varianza')

# Graficar desvio estandar
axs[1][1].plot(x, y_de, color='blue')
axs[1][1].plot(c_de, label='Valor esperado', linestyle='--', color='red')
axs[1][1].set_title('Gráfico 4: Desvio estandar')
axs[1][1].set_xlabel('Tiradas')
axs[1][1].set_ylabel('Desvio estandar')

# Ajustar diseño y mostrar gráficos
plt.tight_layout()

# Guardar la figura en disco
plt.savefig('trabajos_practicos/TP_1.1/cuatro_graficas_tp1.png')

# Mostrar la figura
plt.show()
    