class Trabajador:
    def main():
        # Datos dados del trabajador
        horas_trabajadas = 48
        valor_hora = 5000

        # 0.125 / 12.5% de retencion en la fuente
        porcentaje_retencion = 0.125

        salario_bruto = horas_trabajadas * valor_hora
        retencion = salario_bruto * porcentaje_retencion
        salario_neto = salario_bruto - retencion

        print(f"El salario bruto es: ${salario_bruto:.0f}")
        print(f"La retención en la fuente es: ${retencion:.0f}")
        print(f"El salario neto es: ${salario_neto:.0f}")


if __name__ == "__main__":
    Trabajador.main()
