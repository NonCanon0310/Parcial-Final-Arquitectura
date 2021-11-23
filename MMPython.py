#!/usr/bin/python3



import sys
import time
import numpy
from numpy import random
from numpy.random.mtrand import uniform

# Se ingresa dimensión de la matriz

N = int(sys.argv[1])

# Se crean las matrices (NxN) con numpy inicializadas aleatoriamente

mat_A = numpy.random.uniform(low=0.75,high=1.25,size=(N,N))
mat_B = numpy.random.uniform(low=0.75,high=1.25,size=(N,N))
mat_C = numpy.zeros([N,N])

# Se crea función para imprimir la matriz
def imprimir_Matriz(matriz, T):
    for i in range(T):
        for j in range(T):
            print(round(matriz[i][j],3), end='\t')
        print(end='\n')

# Se crea función para multiplicar las matrices
def multiplicacion_Matrices(matriz_A, matriz_B, T):

    matriz_C = numpy.zeros([T,T])
    
    for i in range(T):
        for j in range(T):
            for k in range(T):
                matriz_C[i][j] += matriz_A[i][k]*matriz_B[k][j]

    return matriz_C

'''
print(end='\n')
print('========================================================', end='\n')
print(end='\n')
print('Matriz A: ', end='\n')
imprimir_Matriz(mat_A, N)

print(end='\n')
print('========================================================', end='\n')
print(end='\n')
print('Matriz B: ', end='\n')
imprimir_Matriz(mat_B, N)

print(end='\n')
print('========================================================', end='\n')
print(end='\n')
mat_C = multiplicacion_Matrices(mat_A, mat_B, N)
print('Multiplicación: ', end='\n')
imprimir_Matriz(mat_C, N)
print(end='\n')
'''

#for i in range(30):

inicio = time.time()
mat_C = multiplicacion_Matrices(mat_A, mat_B, N)
final = time.time()

print('{:.15f}'.format(final-inicio))
