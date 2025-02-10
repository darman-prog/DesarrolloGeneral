import math 
def potencia():
    while True:
        try:
            numero1 = int(input(" ingresa un numero para multiplicar su potencia "))
            numero2 = int(input(" Cuantas veces lo desea potenciar "))
            operacion = math.pow(numero1,numero2)
            print(operacion)
            eleccion = int(input(" 1.Salir 2.Continuar "))
            if eleccion == 1:
                break
            elif eleccion == 2:
                continue
        except ValueError:
            print(" ingresa un valor correcto ")


def raiz():
    while True:
        numero1 = int(input(" Ingresa un numero para calcular su raiz cuadrada "))
        operacion =  math.sqrt(numero1)
        print(operacion)
        print(" desea salir o continuar ")
        eleccion = int(input(" 1.Salir 2.continuar "))
        if eleccion == 1:
            break
        elif eleccion == 2:
            continue
