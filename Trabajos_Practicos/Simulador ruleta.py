import json
import random
import argparse

parser = argparse.ArgumentParser(description="Simulador de ruleta")
parser.add_argument("-c", default=50, type=int, help="Número de tiradas")
parser.add_argument("-n", default=1, type=int, help="Número de corridas")
parser.add_argument("-e", required=True, type=int, choices=range(0, 37), help="Número elegido")

args = parser.parse_args()

num_tiradas = args.c
num_corridas = args.n
numero = args.e

frecuencias={}
for y in range(num_corridas):
    valores = []
    for c in range(1,num_tiradas + 1 ,1):
        valores.append(random.randint(0, 36))
        #desvicion y varianza no se si estan bien me lo tiro el copilot
        frecuencias[c] = {"frecuencia relativa": round((valores.count(numero) / c),4), 
                           "valor promedio de las tiradas": round((sum(valores) / len(valores)),4),
                           "desviacion estandar": round(((sum([(x - sum(valores) / len(valores))**2 for x in valores]) / len(valores))**0.5),4),
                           "varianza": round((sum([(x - sum(valores) / len(valores))**2 for x in valores]) / len(valores)),4)}

#esto lo guarda como json
with open('trabajos_practicos/datos.json', 'w') as jf: 
    json.dump(frecuencias, jf, ensure_ascii=False, indent=2)

# print(frecuencias)
    