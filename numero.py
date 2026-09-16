"""
Ejercicio Propuesto No. 14
Elabore un algoritmo que lea un numero y obtenga su cuadrado
y su cubo.

Fuente: Logica de Programacion, Efrain Oviedo Regino, pag. 50.
"""


class Numero:

    def __init__(self, valor):
        self.valor = valor
        self.cuadrado = 0
        self.cubo = 0

    def calcular_cuadrado(self):
        self.cuadrado = self.valor ** 2

    def calcular_cubo(self):
        self.cubo = self.valor ** 3

    def mostrar_resultado(self):
        print(f"NUMERO: {self.valor}")
        print(f"CUADRADO: {self.cuadrado}")
        print(f"CUBO: {self.cubo}")


def main():
    valor = float(input("Ingrese un numero: "))
    numero = Numero(valor)
    numero.calcular_cuadrado()
    numero.calcular_cubo()
    numero.mostrar_resultado()


if __name__ == "__main__":
    main()
