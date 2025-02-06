import random
"""num = random.randint(1,10)
if num%2 ==0:
    
    print(f"{num} es impar ")
elif num%2 ==1:
    print(f" {num} es par ")

"""

while True:
        intentos = 5
        print( "bienvenido a loteria GANGAMAX ")
        for i in range(intentos):
            NumParticipante = int(input(" ingresa un numero para probar chance "))
        
            NumRandom = random.randint(1,10)
            if NumParticipante == NumRandom:
                print(" Ganaste la loteria!!!!!!!!!!")
            elif NumParticipante != NumRandom:
                print(f" perdiste el numero ganador era {NumRandom} vuelve a intentar a la proxima ")
        print(" ¿deseas salir?")
        eleccion = int(input("1.Salir 2. continuar "))
        if eleccion == 1:
            break
        elif eleccion ==2:
            print(" Suerte!!! ")
            continue

"""while True:
    numero = int(input(" ingresa un numero para verificar si es par o impar "))
    if numero%2 == 0:
        print(" es par")
    elif numero%2 == 1:
        print(" es impar ")
    print(" ¿deseas salir ?")
    eleccion = int(input(" 1.Salir 2.Continuar"))
    if eleccion == 1:
        break
    elif eleccion ==2:
        continue"""


