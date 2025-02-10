from funcionesRaizPotencia import potencia as pt
from funcionesRaizPotencia import raiz as rz

while True:    
    print(" calculadora potencia y raiz")
    print(" 1. potencia ")
    print(" 2. raiz   ")
    print(" 3. Salir  ")
    eleccion = int(input(" ¿Cual opcion deseas?"))
    if eleccion == 1:
        pt()
    elif eleccion == 2: 
        rz()
    elif eleccion == 3:
        break
    else:
        print(" escoje una opcion correcta ")
