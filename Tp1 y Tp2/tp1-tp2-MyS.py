import matplotlib.pyplot as plt 
# Q=1116,26 * t
# deltaT=Q/(m*c)
# mostrar en grafico la temperatura respecto del tiempo por cada segundo que pase(suponiendo q no hay perdida de calor)
def graficar_temperatura(temperatura, tiempo):
    plt.plot(tiempo, temperatura)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Temperatura (°C)')
    plt.title('Temperatura en función del tiempo')
    plt.show()

def main():
    temperatura = []
    tiempo = []
    for i in range(1, 301):
        Q=(1116.26 * i)/(1*4186)
        temperatura.append(Q)
        tiempo.append(i)
    graficar_temperatura(temperatura, tiempo)
main()    