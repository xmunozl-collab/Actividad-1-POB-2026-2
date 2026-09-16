"""
Ejercicio Propuesto No. 17
Dado el radio de un circulo, haga un algoritmo que obtenga
el area del circulo y la longitud de la circunferencia.

Fuente: Logica de Programacion, Efrain Oviedo Regino, pag. 50.
"""

import math


class Circulo:

    def __init__(self, radio):
        self.radio = radio
        self.area = 0
        self.longitud_circunferencia = 0

    def calcular_area(self):
        self.area = math.pi * self.radio ** 2

    def calcular_longitud_circunferencia(self):
        self.longitud_circunferencia = 2 * math.pi * self.radio

    def mostrar_resultado(self):
        print(f"RADIO: {self.radio}")
        print(f"AREA: {self.area}")
        print(f"LONGITUD DE LA CIRCUNFERENCIA: {self.longitud_circunferencia}")


def main():
    radio = float(input("Ingrese el radio del circulo: "))
    circulo = Circulo(radio)
    circulo.calcular_area()
    circulo.calcular_longitud_circunferencia()
    circulo.mostrar_resultado()


if __name__ == "__main__":
    main()
