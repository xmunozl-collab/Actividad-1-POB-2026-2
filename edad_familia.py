"""
Ejercicio Resuelto No. 4
A la mama de Juan le preguntan su edad, y contesta: tengo 3 hijos,
preguntele a Juan su edad. Alberto tiene 2/3 de la edad de Juan,
Ana tiene 4/3 de la edad de Juan y mi edad es la suma de las tres.
Hacer un algoritmo que muestre la edad de los cuatro.

Fuente: Logica de Programacion, Efrain Oviedo Regino, pag. 48-49.
"""


class EdadFamilia:

    def __init__(self, edad_juan):
        # Atributos
        self.edad_juan = edad_juan
        self.edad_alberto = 0
        self.edad_ana = 0
        self.edad_mama = 0

    def calcular_edades(self):
        self.edad_alberto = (2 / 3) * self.edad_juan
        self.edad_ana = (4 / 3) * self.edad_juan
        self.edad_mama = self.edad_alberto + self.edad_juan + self.edad_ana

    def mostrar_edades(self):
        print("LAS EDADES SON:")
        print(f"ALBERTO: {self.edad_alberto}")
        print(f"JUAN: {self.edad_juan}")
        print(f"ANA: {self.edad_ana}")
        print(f"MAMA: {self.edad_mama}")


def main():
    edad_juan = float(input("Ingrese la edad de Juan: "))
    familia = EdadFamilia(edad_juan)
    familia.calcular_edades()
    familia.mostrar_edades()


if __name__ == "__main__":
    main()
