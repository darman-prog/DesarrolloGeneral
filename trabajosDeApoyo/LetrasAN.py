from word2number import w2n
from num2words import num2words


def LetrasAnum():
  entrada = input(" Escribe en letras un numero = ")

  conversion = w2n.word_to_num(entrada)

  print(f"{conversion}")

def numAletras():
  entrada = int(input(" escribe un numero para pasar a letras = "))

  conversion = num2words(entrada, lang="es")
  
  print(conversion)

numAletras()