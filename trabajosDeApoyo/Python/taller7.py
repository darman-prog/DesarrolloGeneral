def decimal_a_binario(n):
    parte_entera = int(n)
    parte_decimal = n - parte_entera

    if parte_entera < 0:
        parte_entera = (1 << 16) + parte_entera
    binario_entero = bin(parte_entera).replace("0b","").zfill(16)

    binario_decimal = ""
    while parte_decimal > 0 and len(binario_decimal) < 10:
        parte_decimal *= 2
        bit = int(parte_decimal)
        if bit == 1:
            parte_decimal -= bit
            binario_decimal += "1"
        else:
            binario_decimal += "0"

    
    return binario_entero + "." + binario_decimal if binario_decimal else binario_entero

numero_decimal1 = float(input(" ingresa un numero para convertir a binario "))
numero_decimal2= float(input(" ingresa un numero para convertir a binario "))


if -32768 <= numero_decimal1 <= 32.767 and -32.768 <= numero_decimal2 <= 32.767:
    suma_decimal = numero_decimal1 + numero_decimal2
    Suma_binarios = decimal_a_binario(suma_decimal)
    print(f"El número {numero_decimal1} + {numero_decimal2} en binario es: {Suma_binarios}")
else:
    print(None)


