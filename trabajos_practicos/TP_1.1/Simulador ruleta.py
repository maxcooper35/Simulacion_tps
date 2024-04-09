import json
import random
import matplotlib.pyplot as plt
import argparse
import os

#################################ARGUMENTOS DE ENTRADA################################
parser = argparse.ArgumentParser(description="Simulador de ruleta")
parser.add_argument("-c", default=1000, type=int, help="Número de tiradas")
parser.add_argument("-n", default=3, type=int, help="Número de corridas")
parser.add_argument("-e", default=0, type=int, choices=range(0, 37), help="Número elegido")
args = parser.parse_args()
num_tiradas = args.c
num_corridas = args.n
numero = args.e
print("#############################################################################################")
print("\nArgumentos de entrada: -c [Número de tiradas] -n [Número de corridas] -e [Número elegido]")
print("Valores elegidos: -c "+str(args.c)+" -n "+str(args.n)+" -e "+str(args.e)+" \n")
print("#############################################################################################")

################################RUTAS################################
# Obtener la ruta completa del directorio
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_graficas = os.path.join(directorio_actual, 'graficas')
ruta_datos = os.path.join(directorio_actual, 'datos_json')
# Verificar si el directorio no existe y crearlo
if not os.path.exists(ruta_graficas):
    os.makedirs(ruta_graficas)
if not os.path.exists(ruta_datos):
    os.makedirs(ruta_datos)

################################FUNCIONES GRAFICAS################################
def graficar (axs, x, y, c, titulo, xlabel, ylabel, ymin, ymax, xmin=0, xmax=num_tiradas):    
    axs.plot(x, y, label='Valor obtenido')    
    axs.plot(c, label='Valor esperado', linestyle='--')
    axs.axis((xmin,xmax ,ymin,ymax))
    axs.set_title(titulo)
    axs.set_xlabel(xlabel)
    axs.set_ylabel(ylabel)
    axs.legend()

def graficar_varias (axs, x, val_y, c, titulo, xlabel, ylabel, ymin, ymax, xmin=0, xmax=num_tiradas):
    #grafica todas las corridas
    for i in range(len(val_y)-1):
        axs.plot(x, val_y[i], label='Valor tirada: '+str(i))
    #el ultimo siempre es el primedio
    axs.plot(x, val_y[len(val_y)-1], label='Valor promedio')
    axs.plot(c, label='Valor esperado', linestyle='--')
    axs.axis((xmin,xmax ,ymin,ymax))
    axs.set_title(titulo)
    axs.set_xlabel(xlabel)
    axs.set_ylabel(ylabel)
    axs.legend()

################################ESTADISTICAS DE CADA CORRIDA################################
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
ruta_archivo = os.path.join(ruta_datos, 'estadisticas.json')
with open(ruta_archivo, 'w') as jf: 
    json.dump(corridas, jf, ensure_ascii=False, indent=2)

################################GRAFICAS################################
#valores en x (es el mismo para todas las graficas)
x = list(range(num_tiradas))
#valores esperados (la linea punteada roja) (es el mismo para todas las graficas)
c_fr = [1/37 for i in range(num_tiradas)]
c_vp = [37/2 for i in range(num_tiradas)]
c_vz = [114 for i in range(num_tiradas)]
c_de = [10.6770 for i in range(num_tiradas)]

#Grafica de cada corrida
val_y_corridas = {}
for c in range(1, num_corridas + 1, 1):
    #valores en y
    y_fr = [corridas[c][i]['frecuencia relativa'] for i in range(1, num_tiradas+1, 1)]
    y_vp = [corridas[c][i]['valor promedio'] for i in range(1, num_tiradas+1, 1)]
    y_vz = [corridas[c][i]['varianza'] for i in range(1, num_tiradas+1, 1)]
    y_de = [corridas[c][i]['desviacion estandar'] for i in range(1, num_tiradas+1, 1)]
    val_y_corridas[c] = {"y_fr": y_fr, "y_vp": y_vp,
                      "y_vz": y_vz, "y_de": y_de}

################################GRAFICA DE CADA CORRIDA################################

for v in range(1, len(val_y_corridas)+1,1):
    #grafica una grafica por cada tirada
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(14, 9))
    graficar(axs[0][0], x, val_y_corridas[v]['y_fr'], c_fr, 'Graf. 1 Cor. '+ str(v)+': Frecuencia relativa del numero '+ str(numero), 'Tiradas', 'Frecuencia relativa',0,c_fr[0] + c_fr[0]*2.3)
    graficar(axs[0][1], x, val_y_corridas[v]['y_vp'], c_vp, 'Graf. 2 Cor. '+ str(v)+': Valor promedio', 'Tiradas', 'Valor promedio',c_vp[0] - c_vp[0]*0.8,c_vp[0] + c_vp[0]*0.8)
    graficar(axs[1][0], x, val_y_corridas[v]['y_vz'], c_vz, 'Graf. 3 Cor. '+ str(v)+': Varianza', 'Tiradas', 'Varianza',c_vz[0] - c_vz[0]*0.8,c_vz[0] + c_vz[0]*0.8)
    graficar(axs[1][1], x, val_y_corridas[v]['y_de'], c_de, 'Graf. 4 Cor. '+ str(v)+': Desvio estandar', 'Tiradas', 'Desvio estandar',c_de[0] - c_de[0]*0.8,c_de[0] + c_de[0]*0.8)
    plt.tight_layout()
    
    ruta_archivo = os.path.join(ruta_graficas, 'estadisticas_corrida_'+str(v)+'.png')
    plt.savefig(ruta_archivo)

################################GRAFICA FINAL################################
################################VALORES PROMEDIOS################################
#Calcula los promedios de todas las corridas
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
#guardar json de promedio de todas las corridas
ruta_archivo = os.path.join(ruta_datos, 'promedios.json')
with open(ruta_archivo, 'w') as jf: 
    json.dump(avg, jf, ensure_ascii=False, indent=2)

#valores en y promedios
y_fr_avg = [avg[i]['frecuencia relativa'] for i in range(1, num_tiradas+1, 1)]
y_vp_avg = [avg[i]['valor promedio'] for i in range(1, num_tiradas+1, 1)]
y_vz_avg = [avg[i]['varianza'] for i in range(1, num_tiradas+1, 1)]
y_de_avg = [avg[i]['desviacion estandar'] for i in range(1, num_tiradas+1, 1)]

#agrega al final de los valores de "y" los promedios para agregarlo a la grafica en las que se ven todas juntas
val_y_corridas[num_corridas + 1] = {"y_fr": y_fr_avg, "y_vp": y_vp_avg, "y_vz": y_vz_avg, "y_de": y_de_avg}
ruta_archivo = os.path.join(ruta_datos, 'estadisticas_y_promedios.json')
with open(ruta_archivo, 'w') as jf:
    json.dump(val_y_corridas, jf, ensure_ascii=False, indent=2)

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(14, 9))
graficar_varias(axs[0][0], x, [val_y_corridas[i]['y_fr'] for i in range(1,len(val_y_corridas)+1)], c_fr, 'Graf. 1: Promedo frecuencias relativas', 'Tiradas', 'Frecuencia relativa',0 ,c_fr[0] + c_fr[0]*1.5)
graficar_varias(axs[0][1], x, [val_y_corridas[i]['y_vp'] for i in range(1,len(val_y_corridas)+1)], c_vp, 'Graf. 2: Promedo valores promedios', 'Tiradas', 'Valor promedio',c_vp[0] - c_vp[0]*0.4,c_vp[0] + c_vp[0]*0.4)
graficar_varias(axs[1][0], x, [val_y_corridas[i]['y_vz'] for i in range(1,len(val_y_corridas)+1)], c_vz, 'Graf. 3: Promedo varianza', 'Tiradas', 'Varianza',c_vz[0] - c_vz[0]*0.4,c_vz[0] + c_vz[0]*0.4)
graficar_varias(axs[1][1], x, [val_y_corridas[i]['y_de'] for i in range(1,len(val_y_corridas)+1)], c_de, 'Graf. 4: Promedo desvio estandar', 'Tiradas', 'Desvio estandar',c_de[0] - c_de[0]*0.4,c_de[0] + c_de[0]*0.4)

plt.tight_layout()

ruta_archivo = os.path.join(ruta_graficas, 'avg_tp1.png')
plt.savefig(ruta_archivo)
plt.show()