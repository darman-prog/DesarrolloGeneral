with open ("trabajosDeApoyo/TxtPrueba.txt", "r") as file:
  Texto = file.read()
  
caracteres_a_eliminar = ".,:;!?¡¿()[]{}\'"

TextoLimpio = ""

for i in Texto:
  if i not in caracteres_a_eliminar:
    TextoLimpio += i

TextoLimpio = TextoLimpio.lower()

palabras = TextoLimpio.split()

frecuencia = {}

for palabra in palabras:
  if palabra in frecuencia:
    frecuencia[palabra] += 1
  else:
    frecuencia[palabra] = 1  

frecuencia_ordenadas = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)

top_10_palabras = frecuencia_ordenadas[:10]

for palabra, freq in top_10_palabras:
  print(f"{palabra},{freq}")



