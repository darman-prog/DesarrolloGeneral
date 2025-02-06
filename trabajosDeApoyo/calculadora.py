def menu_calculadora():
    while True:
        print("-----------------------------")
        print("    calculadora en Python    .        ")
        print(" 1. Sumar                    .        ")
        print(" 2. Restar                   .     "                            )
        print(" 3. Multiplicar              .")
        print(" 4. Dividir                  .")
        print(" 5. Potencia                 .")
        print(" 6. Par o impar              . ")
        print(" 7. Salir                    .")
        print("----------------------------")
        try:
            selecion = int(input("escoge un numero del 1 al 6 para escojer el calculo que desees o si deseas salir escoje 7"))

            if selecion == 1:
                suma()
            elif selecion == 2:
                resta()
            elif selecion == 3:
                multiplicar()
            elif selecion == 4:
                dividir()      
            elif selecion == 5:
                potencia()
            elif selecion == 6:
                impar_o_par()
            elif selecion == 7:
                break
        except ValueError:
            print("Error Ingresa un numero del 1 al 4 o 5 para salir  ")


def suma():
    print(" escribe dos numeros para calcular su suma")
    suma1 = int(input())
    suma2 = int(input())
    operacion = suma1 + suma2
    print("tu resultado es =>",operacion)

def resta():
    print(" escribe dos numeros para calcular su resta")
    resta1 = int(input())
    resta2 = int(input())
    operacion = resta1 - resta2
    print("tu resultado es =>",operacion)

def multiplicar():
    print(" escribe dos numeros para calcular su Multiplicacion")
    multi1 = int(input())
    multi2 = int(input())
    operacion = multi1 * multi2
    print("tu resultado es =>",operacion)

def dividir():
    while True:
        print(" escribe dos numeros para calcular su division")
        div1 = int(input())
        div2 = int(input())
        if div1 == 0 or div2 == 0:
            print("Division Por cero Error ingrese otro numero")
            
        operacion = div1 / div2
        print("tu resultado es =>",operacion)
        salida = int(input("deseas seguir con mas operaciones escribe 0 para salir o otra tecla para continuar"))
        if salida == 0:
            break

def potencia():
    print("escribe dos numeros para sacar su potencia")
    potencia1 = int(input())
    potencia2 = int(input())
    operacion = potencia1 ** potencia2
    print("tu resultado es =>",operacion)

def impar_o_par():
        
        n = int(input("ingresa un numero para verificar si es par o impar o neutro y si deseas salir ingresar "))
        if n % 2 == 0 :
            print("par")
            
        elif n % 1 == 0:
            print("impar")
        else:
            print("neutro")

menu_calculadora()

