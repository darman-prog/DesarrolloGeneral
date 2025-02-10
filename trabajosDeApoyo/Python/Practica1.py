import unittest
#ejercicio


"""def sum(x,y):
    if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
        raise ValueError("Solo enteros o decimales")
    return x + y  

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(5,7),12)
        self.assertEqual(sum(5,-7),-2)
        self.assertEqual(sum(6.1,6.1),12.2)



        with self.assertRaises(ValueError):
            sum("5",7)
        with self.assertRaises(ValueError):
            sum("4","4")
        with self.assertRaises(ValueError):
            sum(7,"4")
        with self.assertRaises(ValueError):
            sum(None,2)"""

"""unittest.main()"""

"""num = 5
while num <= 10:
    if num % 2 == 0:
        num -= 1
        continue
    if num == -9:
        break
    print(num)
    num -= 1
"""




import time

inicio = time.time()  
limite = 3 
num = 0  

while time.time() - inicio < limite:
    num += 1
    print(f"tu suma es {num}")  # Imprime el valor de 'num'
    time.sleep(1)


i = 1
num = int(input(" Ingresa un numero "))
while i <= 10:
    if num > 10:
        print(" Valor incorrecto ")
    print( num, "x",i,"=",num * i) 
    i = i+1
    
