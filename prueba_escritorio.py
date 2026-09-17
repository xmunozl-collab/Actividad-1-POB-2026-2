class PruebaEscritorio:
    def main():
        # Declaramos las variables para poder usar decimales
        suma = 0
        x = 20

        suma += x

        y = 40
        x = x + y ** 2

        # Calculo final
        suma = suma + (x / y)

        print("EL VALOR DE LA SUMA ES:", suma)


if __name__ == "__main__":
    PruebaEscritorio.main()
