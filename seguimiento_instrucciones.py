"""
Ejercicio Resuelto No. 5
Hacer un seguimiento (prueba de escritorio) del siguiente grupo
de instrucciones:

INICIO
    SUMA = 0
    X = 20
    SUMA = SUMA + X
    Y = 40
    X = X + Y ** 2
    SUMA = SUMA + X / Y
    ESCRIBA: "EL VALOR DE LA SUMA ES:", SUMA
FIN_INICIO

Fuente: Logica de Programacion, Efrain Oviedo Regino, pag. 49-50.

Esta clase modela, paso a paso, el seguimiento de las variables
SUMA, X y Y (equivalente en codigo a la prueba de escritorio
manual pedida por el ejercicio).
"""


class SeguimientoInstrucciones:

    def __init__(self):
        # Atributos (equivalen a las variables del pseudocodigo)
        self.suma = 0
        self.x = 0
        self.y = 0

    def ejecutar(self):
        self.suma = 0
        self._imprimir_estado("SUMA = 0")

        self.x = 20
        self._imprimir_estado("X = 20")

        self.suma = self.suma + self.x
        self._imprimir_estado("SUMA = SUMA + X")

        self.y = 40
        self._imprimir_estado("Y = 40")

        self.x = self.x + self.y ** 2
        self._imprimir_estado("X = X + Y ** 2")

        self.suma = self.suma + self.x / self.y
        self._imprimir_estado("SUMA = SUMA + X / Y")

        print()
        print(f"EL VALOR DE LA SUMA ES: {self.suma}")

    def _imprimir_estado(self, instruccion):
        print(f"{instruccion:<22} -> SUMA={self.suma:<10} X={self.x:<10} Y={self.y}")


def main():
    seguimiento = SeguimientoInstrucciones()
    seguimiento.ejecutar()


if __name__ == "__main__":
    main()
