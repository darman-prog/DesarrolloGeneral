"""def organigrama():
  numero_asteriscos = int(input("ingresa numero de asteriscos")) 
  for i in range(1, numero_asteriscos + 1):
      
      espacios = " " * (numero_asteriscos - i)

      asterisco = "°" * (2 * i - 1)

      print(espacios + asterisco)
organigrama()
"""


"""operacion = input(" escribe una operacion ")
resultado = eval(operacion)
print(f" este fue tu resultado {resultado}")"""

#serie fibonacci
"""n_tems = 100
a , b = 0,1
for i in range(n_tems):
    print(a)    
    a, b = b, a + b"""

#serie fibonacci avanzado
"""def fib(n):
    if n < 2:
        return n   
    else:
        return fib(n-1) + fib(n-2)
    
for i in range(30):
    print(fib(i))"""


"""
saludo = "Hola mundo"
print(f"{saludo}")"""
"""
pregunta = input("¿cual es tu nombre?").lower()
print(f"hola {pregunta} como estas?")"""

"""print(((3+2)/(2*5))**2)"""
"""
while True:
  print("bienvenido usuario por favor digite el numero de horas trabajadas y digitaremos el monto")
  horas = int(input("digite sus horas trabajadas"))
  seguimiento = int(input(f"sus horas trabajadas fueron {horas} si desea cancelar escriba 0 y si quiere continuar escriba 1"))

  if seguimiento == 1:
    print("sigamos con el proceso")
    coste = int(input("cual fue el coste por hora"))
    operacion =  horas * coste 
    print(f"este es su paga {operacion}")
    break
  if seguimiento == 0:
    print("Proceso Cancelado")
    break
    
"""

