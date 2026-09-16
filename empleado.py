"""
Ejercicio Propuesto No. 12
Un empleado trabaja 48 horas en la semana a razon de $5.000 hora.
El porcentaje de retencion en la fuente es del 12,5% del salario
bruto. Se desea saber cual es el salario bruto, la retencion en
la fuente y el salario neto del trabajador.

Fuente: Logica de Programacion, Efrain Oviedo Regino, pag. 50.
"""


class Empleado:

    def __init__(self, horas_trabajadas, valor_hora, porcentaje_retencion):
        # Atributos (datos de entrada)
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion

        # Atributos (resultados)
        self.salario_bruto = 0
        self.retencion_fuente = 0
        self.salario_neto = 0

    def calcular_salario(self):
        self.salario_bruto = self.horas_trabajadas * self.valor_hora
        self.retencion_fuente = self.salario_bruto * (self.porcentaje_retencion / 100)
        self.salario_neto = self.salario_bruto - self.retencion_fuente

    def mostrar_resultado(self):
        print(f"SALARIO BRUTO: {self.salario_bruto}")
        print(f"RETENCION EN LA FUENTE: {self.retencion_fuente}")
        print(f"SALARIO NETO: {self.salario_neto}")


def main():
    horas = float(input("Horas trabajadas en la semana: "))
    valor_hora = float(input("Valor de la hora: "))
    porcentaje = float(input("Porcentaje de retencion en la fuente (%): "))

    empleado = Empleado(horas, valor_hora, porcentaje)
    empleado.calcular_salario()
    empleado.mostrar_resultado()


if __name__ == "__main__":
    main()
