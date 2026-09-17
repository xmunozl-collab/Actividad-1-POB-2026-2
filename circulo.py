import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    # Metodo para calcular el area usando math.pi
    def calcular_area(self):
        return math.pi * self.radio ** 2

    # Metodo para calcular la longitud de la circunferencia
    def calcular_longitud(self):
        return 2 * math.pi * self.radio
