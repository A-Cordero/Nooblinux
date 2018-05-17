#Resolucion de ecuaciones lineales por metodo de Doolittle
#@Autor : Cordero Ariano

import numpy as np
from math import fabs
from math import sqrt
from sys import exit
np.set_printoptions(formatter={"float": lambda x:"%0.5f"%(x)})

def inputMatrix() :

    n = 4
    A = np.array([[ 0 for x in range(n)]  for y in range(n)], dtype =  float)
    A[0][0] = 2
    A[0][1] = 1
    A[0][2] = 1
    A[0][3] = 0
    A[1][0] = 4
    A[1][1] = 3
    A[1][2] = 3
    A[1][3] = 1
    A[2][0] = 8
    A[2][1] = 7
    A[2][2] = 9
    A[2][3] = 5
    A[3][0] = 6
    A[3][1] = 7
    A[3][2] = 9
    A[3][3] = 8

    return A

def inputMatrixb() :

    n = 4
    b = np.array([0 for x in range(n)], dtype =  float)
    b[0] = 1
    b[1] = 8
    b[2] = 30
    b[3] = 41

    return b

def aumentada( A, b) :

    M = np.c_[ A, b]
    return M

def printMatrix( A ) :

    print A,"\n"

def exchangeRows(M, r1, r2):
    """Intercambia las filas r1 y r2 de M"""
    temp = np.array([0 for x in range(len(M[r1]))], dtype =  float)
    for i in range( len(M[r1])) :
        temp[i] = M[r1][i]
    M[r1] = M[r2]
    M[r2] = temp
    return M

def exchangeCols(M, c1, c2):
    """Intercambia las columnas c1 y c2 de M"""

    for k in range(len(M)):
        temp = M[k][c1]
        M[k][c1] = M[k][c2]
        M[k][c2] = temp
    return M

def pivotP(M, r1, r2):
    """Permuta la fila r1 con la fila r2 de la matriz M"""

    return exchangeRows(M, r1, r2)

def Pr(n, r1, r2):
    """Calcula la matriz de permutacion de fila"""

    #Matriz identidad
    I = [[float(i == j) for j in range(n)] for i in range(n)]
    return exchangeRows(I, r1, r2)

def Pc(n, c1, c2):
    """Calcula la matriz de permutacion de columna"""

    #Matriz identidad
    I = [[float(i == j) for j in range(n)] for i in range(n)]
    return exchangeCols(I, c1, c2)

def maxColum(M, c):

    r = c #fila
    maximum = M[c][c]
    for i in range(c+1,len(M)):
        if(fabs(maximum) < fabs(M[i][c])):
            maximum = M[i][c]
            r = i
    return r

def pivote( a, P, Q, colum) :
    n = len(a)

    row_maxColumn = maxColum(a, colum)
    if row_maxColumn != colum:
        a = pivotP(a, row_maxColumn, colum)
        P = exchangeRows(P, row_maxColumn, colum)
        print 'P(%d,%d)' % (row_maxColumn, colum)
        printMatrix(Pr(n, row_maxColumn, colum))

    print "nueva matrix"
    printMatrix(a)
    return a,P,Q

def L1U( A, b) :

    n = len(A)
    a = A
    U = np.array([[ 0 for x in range(n)]  for y in range(n)], dtype =  float)
    L = m=np.eye(n, dtype = float)
    P = [[float(i == j) for j in range(n)] for i in range(n)]
    Q = [[float(i == j) for j in range(n)] for i in range(n)]
    for k in range(n):
        a, P, Q = pivote(a, P, Q, k)
    for k in range(n):
        for i in range(k, n):
            U[k][i] = a[k][i] - sum(L[k][p]*U[p][i] for p in range(k))
        for i in range(k+1, n):
            if U[k][k] == 0:
                exit('Debe usarse pivoteo parcial')
            L[i][k] = (a[i][k] - sum(L[i][p]*U[p][k] for p in range(k))) / float(U[k][k])

    print "L\n",L
    print "U\n",U
    #por sustitucion progresiva
    a = aumentada(L, b)
    y =  np.array([0 for x in range(n)], dtype =  float)
    y[0] = a[0][n]/float(a[0][0])
    for i  in range( 1, n) :
        y[i] = a[i][n]
        for j in range( i - 1, -1, -1) :
            y[i] = y[i] - a[i][j]*y[j]
        y[i] = y[i]/float( a[i][i])
    print y
    a = aumentada(U, y)
    x =  np.array([0 for x in range(n)], dtype =  float)
    x[n-1] = a[n-1][n]/float( a[n-1][n-1])
    for i  in range( n - 2, -1, -1) :
        x[i] = a[i][n]
        for j in range( i + 1, n) :
            x[i] = x[i] - a[i][j]*x[j]
        x[i] = x[i]/float( a[i][i])
    print x

def main() :

    A = inputMatrix()
    b = inputMatrixb()
    printMatrix(A)
    printMatrix(b)
    M = aumentada(A, b)
    printMatrix(M)
    L1U(A, b)
main()
