from circulo import Circulo


def main():
    radio = float(input("Ingrese el radio del círculo: "))

    # Creo aca el objeto Circulo pasandole el radio ingresado
    mi_circulo = Circulo(radio)

    print("El área del círculo es:", mi_circulo.calcular_area())
    print("La longitud de la circunferencia es:", mi_circulo.calcular_longitud())


if __name__ == "__main__":
    main()
