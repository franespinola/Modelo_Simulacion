import matplotlib.pyplot as plt

class DispositivoTermico:
    def __init__(self, temperatura_inicial, masa, tiempo, voltaje):
        self.temperatura = temperatura_inicial
        self.masa = masa
        self.tiempo = tiempo
        self.voltaje = voltaje
        self.constante_calor_especifico = 4.18

    def calcular_resistencia(self):
        delta_temperatura = 100 - self.temperatura
        energia_calorifica = self.constante_calor_especifico * self.masa * delta_temperatura
        potencia = energia_calorifica / self.tiempo
        corriente = potencia / self.voltaje
        resistencia = self.voltaje / corriente
        return resistencia

def simular_temperatura(dispositivo, con_perdidas=True):
    potencia_resistencia = dispositivo.voltaje ** 2 / dispositivo.calcular_resistencia()
    masa_fluido = 1 
    calor_especifico_fluido = 4186 
    ticks_por_segundo = 10  
    ticks_totales = dispositivo.tiempo * ticks_por_segundo
    temperaturas = [dispositivo.temperatura]

    for _ in range(1, ticks_totales + 1):
        temperatura_actual = temperaturas[-1]
        if con_perdidas:
            potencia_efectiva = potencia_resistencia - (temperatura_actual - dispositivo.temperatura) * 10
        else:
            potencia_efectiva = potencia_resistencia
        
        calor_suministrado = potencia_efectiva / ticks_por_segundo
        calor_absorbido = calor_especifico_fluido * masa_fluido
        delta_temperatura = calor_suministrado / calor_absorbido
        temperaturas.append(temperatura_actual + delta_temperatura)

    tiempo = [i / ticks_por_segundo for i in range(ticks_totales + 1)]
    return tiempo, temperaturas

# Parámetros de simulación
temperatura_inicial = 30
masa = 1000
tiempo_simulacion = 300
voltaje = 220

# Crear dispositivo y simular
dispositivo = DispositivoTermico(temperatura_inicial, masa, tiempo_simulacion, voltaje)
tiempo_con_perdidas, temp_con_perdidas = simular_temperatura(dispositivo, con_perdidas=True)
tiempo_sin_perdidas, temp_sin_perdidas = simular_temperatura(dispositivo, con_perdidas=False)

# Graficar resultados
plt.plot(tiempo_con_perdidas, temp_con_perdidas, label='Con pérdidas')
plt.plot(tiempo_sin_perdidas, temp_sin_perdidas, label='Sin pérdidas')
plt.xlabel('Tiempo')
plt.ylabel('Temperatura del agua')
plt.title('Temperatura del agua en el dispositivo térmico')
plt.legend()
plt.grid(True)
plt.show()

