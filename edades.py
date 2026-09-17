class Edades:
    def calcular_edalber(edjuan):
        return edjuan * 2 / 3

    def calcular_edana(edjuan):
        return edjuan * 4 / 3

    def calcular_edmama(edjuan, edana, edalber):
        return edjuan + edana + edalber


def main():
    edjuan = float(input("Ingrese la edad de Juan: "))

    edalber = Edades.calcular_edalber(edjuan)
    edana = Edades.calcular_edana(edjuan)
    edmama = Edades.calcular_edmama(edjuan, edana, edalber)

    print("La edad de Juan es:", edjuan)
    print("La edad de Alberto es:", edalber)
    print("La edad de Ana es:", edana)
    print("La edad de la mamá es:", edmama)


if __name__ == "__main__":
    main()
