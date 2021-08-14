def main():
    #escribe tu código abajo de esta línea
    año1 = int(input("Dame el año actual: "))
    edad = int(input("Dame tu edad: "))
    rest = (100-edad)
    resultado = (rest+año1)
    print("Cumplirás 100 años en el año:",resultado)

if __name__ == '__main__':
    main()
