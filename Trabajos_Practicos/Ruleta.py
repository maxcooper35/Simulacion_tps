import random
import matplotlib.pyplot as plt
import numpy as np
import sys

if len(sys.argv) != 4:
    print("Uso: python programa.py <arg_1> <arg_2> <arg_3>")
    sys.exit(1)

a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])

#Listas para guardar los valores esperados de las variables
frec_esp=[0.027 for _ in range(a)]
prom_esp=[18 for _ in range(a)]
numeros=np.arange(0,36)
var_esp=[np.var(numeros) for _ in range(a)]
desv_esp=[np.std(numeros) for _ in range(a)]
f1, f2, f3, f4 = [], [], [], []

for i in range(b):
    cont, val, suma_cuad, suma = 0, 0, 0, 0
    frec_rel, prom, var_act_lista, desv_act_lista = [], [], [], []
    valores = [random.randint(0, 36) for _ in range(a)]
    for t in range(1, a+1):
        if valores[t-1] / c == 1:
            cont+=1
        frec_rel_act = cont / t           #Calculo de la frecuencia relativa acumulada
        frec_rel.append(frec_rel_act)            

        val += int(random.randint(0, 36))           #Calculo del promedio
        prom.append(val / t)

        suma_cuad += int(random.randint(0, 36)) ** 2       #Calculo de la varianza
        suma += int(random.randint(0, 36))
        var_act=(suma_cuad/t)-(suma/t)**2
        var_act_lista.append(var_act)

        desv_act=var_act ** 0.5                     #Calculo del desvio
        desv_act_lista.append(desv_act)
    f1.append(frec_rel)
    f2.append(prom)
    f3.append(var_act_lista)
    f4.append(desv_act_lista)

    print('prom es: ', prom[a-1], 'Corrida numero: ', i, 'La frecuencia relativa es', frec_rel[a-1])

fig, axs = plt.subplots(2, 2)

#Grafica de FR
for i in range(len(f1)):
    axs[0,0].plot(f1[i], label=f'Línea {i+1}')
axs[0,0].plot(frec_esp , label='F.R. Esperada', linestyle='--',color='red')
axs[0,0].set_xlabel('Número de tirada')
axs[0,0].set_ylabel('Frec Rel')
axs[0,0].set_title('Gráfico de Frecuencia Relativa')
axs[0,0].legend()
axs[0,0].grid(True)

#Grafica de Prom
for i in range(len(f2)):
    axs[0,1].plot(f2[i], label=f'Línea {i+1}')
axs[0,1].plot(prom_esp , label='Promedio esperado', linestyle='--', color='red')
axs[0,1].set_xlabel('Número de tirada')
axs[0,1].set_ylabel('Promedio')
axs[0,1].set_title('Gráfico de Promedio')
axs[0,1].legend()
axs[0,1].grid(True)

#Gráfica de varianza
for i in range(len(f3)):
    axs[1,0].plot(f3[i], label=f'Línea {i+1}')
axs[1,0].plot(var_esp , label='Varianza esperado', linestyle='--', color='red')
axs[1,0].set_xlabel('Número de tirada')
axs[1,0].set_ylabel('Varianza')
axs[1,0].set_title('Gráfico de Varianza')
axs[1,0].legend()
axs[1,0].grid(True)

#Gráfica de desvio
for i in range(len(f4)):
    axs[1,1].plot(f4[i], label=f'Línea {i+1}')
axs[1,1].plot(desv_esp , label='Desvio esperado', linestyle='--', color='red')
axs[1,1].set_xlabel('Número de tirada')
axs[1,1].set_ylabel('Desvio')
axs[1,1].set_title('Gráfico de Desvio')
axs[1,1].legend()
axs[1,1].grid(True)

plt.tight_layout()
plt.show()
