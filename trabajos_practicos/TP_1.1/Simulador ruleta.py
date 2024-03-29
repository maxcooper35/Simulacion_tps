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

def graficar (axs, x, y, c, titulo, xlabel, ylabel, color1, color2):
    axs.plot(x, y, label='Valor obtenido',color=color1)
    axs.plot(c, label='Valor esperado', linestyle='--', color=color2,)
    axs.axis((0,num_tiradas ,0,c[0]*2))
    axs.set_title(titulo)
    axs.set_xlabel(xlabel)
    axs.set_ylabel(ylabel)
    axs.legend()

corridas={}
for n in range(1, num_corridas + 1, 1):
    tiradas={}
    valores = []
    suma = 0
    for c in range(1, num_tiradas + 1, 1):
        ruleta = random.randint(0, 37)        
        valores.append(ruleta)
        suma = suma + ruleta

        fr = valores.count(numero) / c
        vp = suma / c
        vz = sum([(x - vp)**2 for x in valores]) / c
        de = vz**0.5
        tiradas[c] = {"frecuencia relativa": fr, "valor promedio": vp,
                      "varianza": vz, "desviacion estandar": de}
    corridas[n] = tiradas
#guardar json
with open('trabajos_practicos/TP_1.1/datos.json', 'w') as jf: 
    json.dump(corridas, jf, ensure_ascii=False, indent=2)

#Grafica primera corrida
#valores en x
x = list(range(num_tiradas))
#valores esperados
c_fr = [1/37 for i in range(num_tiradas)]
c_vp = [18 for i in range(num_tiradas)]
c_vz = [114 for i in range(num_tiradas)]
c_de = [10.68 for i in range(num_tiradas)]
#valores en y
y_fr = [corridas[1][i]['frecuencia relativa'] for i in range(1, num_tiradas+1, 1)]
y_vp = [corridas[1][i]['valor promedio'] for i in range(1, num_tiradas+1, 1)]
y_vz = [corridas[1][i]['varianza'] for i in range(1, num_tiradas+1, 1)]
y_de = [corridas[1][i]['desviacion estandar'] for i in range(1, num_tiradas+1, 1)]
#graficar
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(14, 9))
graficar(axs[0][0], x, y_fr, c_fr, 'Gráfico 1: Frecuencia relativa', 'Tiradas', 'Frecuencia relativa', 'blue', 'red')
graficar(axs[0][1], x, y_vp, c_vp, 'Gráfico 2: Valor promedio', 'Tiradas', 'Valor promedio', 'blue', 'red')
graficar(axs[1][0], x, y_vz, c_vz, 'Gráfico 3: Varianza', 'Tiradas', 'Varianza', 'blue', 'red')
graficar(axs[1][1], x, y_de, c_de, 'Gráfico 4: Desvio estandar', 'Tiradas', 'Desvio estandar', 'blue', 'red')
plt.tight_layout()
plt.savefig('trabajos_practicos/TP_1.1/cuatro_graficas_tp1.png')
plt.show()

#Grafica promedio de cada tirada
avg = {}
for c in range(1, num_tiradas + 1, 1):
    frs = []
    vps = []
    vzs = []
    des = []
    for n in range(1, num_corridas + 1, 1):
        frs.append(corridas[n][c]['frecuencia relativa'])
        vps.append(corridas[n][c]['valor promedio'])
        vzs.append(corridas[n][c]['varianza'])
        des.append(corridas[n][c]['desviacion estandar'])
    avg[c] = {"frecuencia relativa": (sum(frs) / num_corridas),
                "valor promedio": (sum(vps) / num_corridas),
                "varianza": (sum(vzs) / num_corridas),
                "desviacion estandar": (sum(des) / num_corridas)} 
#guardar json
with open('trabajos_practicos/TP_1.1/datos_promedios.json', 'w') as jf: 
    json.dump(avg, jf, ensure_ascii=False, indent=2)
#valores en y (valores en x son los mismos)
y_fr_avg = [avg[i]['frecuencia relativa'] for i in range(1, num_tiradas+1, 1)]
y_vp_avg = [avg[i]['valor promedio'] for i in range(1, num_tiradas+1, 1)]
y_vz_avg = [avg[i]['varianza'] for i in range(1, num_tiradas+1, 1)]
y_de_avg = [avg[i]['desviacion estandar'] for i in range(1, num_tiradas+1, 1)]
#graficar
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(14, 9))
graficar(axs[0][0], x, y_fr_avg, c_fr, 'Gráfico 1: Frecuencia relativa', 'Tiradas', 'Frecuencia relativa', 'green', 'red')
graficar(axs[0][1], x, y_vp_avg, c_vp, 'Gráfico 2: Valor promedio', 'Tiradas', 'Valor promedio', 'green', 'red')
graficar(axs[1][0], x, y_vz_avg, c_vz, 'Gráfico 3: Varianza', 'Tiradas', 'Varianza', 'green', 'red')
graficar(axs[1][1], x, y_de_avg, c_de, 'Gráfico 4: Desvio estandar', 'Tiradas', 'Desvio estandar', 'green', 'red')
plt.tight_layout()
plt.savefig('trabajos_practicos/TP_1.1/cuatro_graficas_avg_tp1.png')
plt.show()
