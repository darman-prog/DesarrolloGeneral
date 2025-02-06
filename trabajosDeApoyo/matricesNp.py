"""

# Definimos la matriz de coeficientes A
A = np.array([  [5, -8, -10],
                [1, -7, 0  ],
                [10, 10, 6 ]])

# Calculamos el determinante de A
det_A = np.linalg.det(A)


print(det_A)"""
import numpy as np
# Definimos la matriz de coeficientes A y el vector de términos independientes B
A = np.array(   [[5, -8, -10],
                [1, -7, 0],
                [10, 10, 6]])

B = np.array([8, -2, 9])

Det = 5
# Resolvemos el sistema de ecuaciones usando numpy (Cramer's rule isn't needed here, numpy can solve the system directly)
solution = np.linalg.solve(A, B)

solucion = np.linalg.det(A)
# Extraemos el valor de x
print(solucion)