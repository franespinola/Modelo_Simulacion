class PropiedadesTermicas:
    def __init__(self):
        self.temperatura = 30
        self.masa = 1000
        self.tiempo = 300
        self.voltaje = 220
        self.indice_conductividad = 0.035
        self.diametro = 0.1
        self.altura = 0.127
        self.espesor = 0.01
        self.sup = 0.0556
        self.temperatura_inicial_fluido = 30
        self.temperatura_deseada = 100

    def calcular_perdida(self):
        perdida = self.indice_conductividad * self.sup / self.espesor
        return perdida

if __name__ == "__main__":
    propiedades = PropiedadesTermicas()
    print(propiedades.calcular_perdida())

