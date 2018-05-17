#Resolucion de ecuaciones lineales por metodo de Doolittle
#@Autor : Cordero Ariano

import numpy as np
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

def LU1( A, b) :

    n = len(A)
    a = A
    U = np.array([[ 0 for x in range(n)]  for y in range(n)], dtype =  float)
    L = m=np.eye(n, dtype = float)

    for k in range(n):
        for i in range(k, n):
            U[k][i] = A[k][i] - sum(L[k][p]*U[p][i] for p in range(k))
        for i in range(k+1, n):
            if U[k][k] == 0:
                exit('Debe usarse pivoteo parcial')
            L[i][k] = (A[i][k] - sum(L[i][p]*U[p][k] for p in range(k))) / float(U[k][k])

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
    LU1(A, b)
main()
