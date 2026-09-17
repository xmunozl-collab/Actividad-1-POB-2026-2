from potenciacion import Potenciacion


def main():
    numero = float(input("Numero: "))

    cuadrado = Potenciacion.calcular_cuadrado(numero)
    cubo = Potenciacion.calcular_cubo(numero)

    print(f"El cuadrado de {numero:.0f} es: {cuadrado:.0f}")
    print(f"El cubo de {numero:.0f} es: {cubo:.0f}")


if __name__ == "__main__":
    main()
