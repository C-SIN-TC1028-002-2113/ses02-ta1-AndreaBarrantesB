def main():
    #escribe tu código abajo de esta línea
    nacimiento = float(input("Dame el año de nacimiento: "))
    actualidad = float(input("Dame el año actual: "))
    Lustro = (actualidad-nacimiento)/5
    print("Los lustros que has vivido son:",Lustro)

if __name__ == '__main__':
    main()
