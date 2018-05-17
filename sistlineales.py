
from math import fabs
from math import sqrt
from sys import exit


def inputMatrix():

        n=6	

        A = [[0 for x in xrange(n)] for x in xrange(n)]
        #return A
	A[0][0] = 23.0000
	A[0][1] = 0.00000	
	A[0][2] = 0.00000
	A[0][3] = 25.0000
	A[0][4] = 0.00000
	A[0][5] = 0.00000
	A[1][0] = 23.0000
	A[1][1] = -35.0000
	A[1][2] = 0.00000
	A[1][3] = 0.00000
	A[1][4] = 16.0000
	A[1][5] = 0.00000
	A[2][0] = 0.00000
	A[2][1] = 0.00000
	A[2][2] = 35.0000
	A[2][3] = -35.0000
	A[2][4] = 16.0000
	A[2][5] = 0.00000
	A[3][0] = 1.00000
	A[3][1] = 1.00000
	A[3][2] = 0.00000
	A[3][3] = 0.00000
	A[3][4] = 0.00000
	A[3][5] = -1.00000
	A[4][0] = -1.00000
	A[4][1] = 0.00000
	A[4][2] = 0.00000
	A[4][3] = 1.00000
	A[4][4] = 1.0000000
	A[4][5] = 0.00000
	A[5][0] = 0.00000
	A[5][1] = 1.00000
	A[5][2] = -1.00000
	A[5][3] = 0.00000
	A[5][4] = 1.00000
	A[5][5] = 0.00000


        return A



def inputVector(M):
	"""Ingreso de datos del vector independiente"""

	n = len(M)
	#print 'Ingrese los elementos del vector b'
	b = [0]*n
	"""temp = raw_input();
	b = temp.split()
	for i in range(n):
		b[i] = float(b[i])"""
        b[0] = 30.00004
        b[1] = 0.00004
        b[2] = 0.00004
        b[3] = 0.00004
        b[4] = 0.00004
        b[5] = 0.00004

	return b	
	
def printMatrixD(M):
	"""Imprime la matriz, version debugger."""

	for i in range(len(M)):
		# print '|',
		for j in range(len(M[i])):
			if(i == 0 and j == 0):
				print " ",
				for x in range(len(M[i])):
					print '{0:8}'.format(x),
				print
				print
			if(j == 0):
				print i,

			if(j == len(M)):
				print '|',
				print '{0:8.4f}'.format(M[i][j]),
			else:
				print '{0:8.4f}'.format(M[i][j]),	
		print '|'
	print

def printMatrix(M):
	"""Imprime la matriz de una forma legible."""

	for i in range(len(M)):
		print '|',
		for j in range(len(M[i])):
			if(j == len(M)):
				print '|',
				print '{0:8.4f}'.format(M[i][j]),
			else:
				print '{0:8.4f}'.format(M[i][j]),	
		print '|'
	print  

def Matrizsimetrica(A):
	"""Calcula la matriz simetrica de A"""

	for i in range(len(A)):
		for j in range(i+1,len(A)):
			if A[i][j] != A[j][i]:
				return False
	return True 


def reverseSub(a):

	n = len(a)
	x = [0]*n
	for j in range(n-1, -1, -1):
		x[j] = (a[j][n] - sum(a[j][k]*x[k] for k in range(j+1, n)))/float(a[j][j])
                x[j] = round( x[j], 5)
	return x	

def solMatrixSup(M, b):

	x = []
	for i in range(len(M)-1,-1,-1):
		x.append((1.0/(M[i][i]))*(b[i]-sum(M[i][len(M)-j-1]*x[j] for j in range(len(x)))))
	x.reverse()
	
	return x

def solMatrixInf(M, b):

	x = []
	for i in range(len(M)):
		x.append((1.0/(M[i][i]))*(b[i]-sum(M[i][j]*x[j] for j in range(len(x)))))
	return x
	
def aumentada(M, b):
	
	a = M
	for i in range(len(M)):
		a[i].append(b[i])

	return a	

def maxColum(M, c):

	r = c #fila
	maximum = M[c][c]
	for i in range(c+1,len(M)):
		if(fabs(maximum) < fabs(M[i][c])):
			maximum = M[i][c]
			r = i
	return r

def maxSubMatrix(M, c):
        rw = c
	colum = c
	n = len(M)
	maximum = M[c][c]
		
	for j in range(c, n):
		for k in range(c, n):
			maxTemp = M[k][j]
			if(fabs(maximum) < fabs(maxTemp)):
				maximum = maxTemp
				colum = j
				rw = k

	return rw , colum			

def exchangeRows(M, r1, r2):
	"""Intercambia las filas r1 y r2 de M"""

	M[r1], M[r2] = M[r2], M[r1]
	return M

def exchangeCols(M, c1, c2):
	"""Intercambia las columnas c1 y c2 de M"""

	for k in range(len(M)):
		M[k][c1] , M[k][c2] = M[k][c2], M[k][c1]
	return M	

def pivot(a, P, Q, colum, piv=0):
	"""Se encarga del pivoteo en cualquier metodo."""

	if piv > 2 or piv < 0:
		exit('Valores invalidos para el parametro pivoteo, valores validos: 0, 1, 2.')
	n = len(a)
		
	temp = a[colum][colum]
	if(temp == 0.0 and piv == 0):
		row_maxColumn = maxColum(a, colum)
		a = pivotP(a, row_maxColumn, colum)
		P = exchangeRows(P, row_maxColumn, colum)
		print 'P(%d,%d)' % (row_maxColumn, colum)
		printMatrix(Pr(n, row_maxColumn, colum))
		
	elif piv == 1:
		row_maxColumn = maxColum(a, colum)
		if row_maxColumn != colum:
			a = pivotP(a, row_maxColumn, colum)
			P = exchangeRows(P, row_maxColumn, colum)
			print 'P(%d,%d)' % (row_maxColumn, colum)
			printMatrix(Pr(n, row_maxColumn, colum))
			
	elif piv == 2:
		row, c = maxSubMatrix(a, colum)	
		if (row != colum) or (c != colum) :
			a = pivotT(a, colum)
			P = exchangeCols(P, row, colum)
			Q = exchangeCols(Q, colum, c)
			print 'P(%d,%d):' % (colum, row)
			printMatrix(Pr(n, row, colum))
			print 'Q(%d,%d):' % (colum, c)
			printMatrix(Pr(n, c, colum))

	return 	a, P, Q		

def pivotP(M, r1, r2):
	"""Permuta la fila r1 con la fila r2 de la matriz M"""

	return exchangeRows(M, r1, r2)

def pivotT(M, i):
	"""Busca el mayor elemento de la submatriz A[i] y permuta filas y columnas"""

	r, c = maxSubMatrix(M, i)
	M = pivotP(M, i, r)		

	return exchangeCols(M, c, i)

def L(n, ri, c):
	"""Calcula las matrices Li.
		
	"""
	#Matriz identidad
	L = [[float(i == j) for j in range(n)] for i in range(n)]
	for k in range(c+1, n):
		L[k][c] = -ri[k]
			
	return L

def matrixMulti(A, B):
	"""Multiplica dos matrices, C = A*B """

	rowsA, colsA = len(A), len(A[0])
	rowsB, colsB = len(B), len(B[0])

	if colsA != rowsB:
		exit('Dimensiones incorrectas')

	C = [[0 for row in range(colsB)] for col in range(rowsA)]

	for i in range(rowsA):
		for j in range(colsB):
			for k in range(colsA):
				C[i][j] += A[i][k]*B[k][j]
	return C

def T(n, ri, c):
	
	T = [[float(i == j) for j in range(n)] for i in range(n)]
	for k in range(n):
		T[k][c] = -ri[k]

	return T

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

def multi(A,x):
	
	c=[]
	for i in range(len(A)):
		c.append(sum(A[i][j]*x[j] for j in range(len(A))))
	return c

def invLU(A):
	P, L, U = croutLU1(A)
	for x in range(1,10):
		pass
		
def gauss(A, b, piv=0):
	
	a = aumentada(A, b)
	n = len(A)
	P = [[float(i == j) for j in range(n)] for i in range(n)]
	Q = [[float(i == j) for j in range(n)] for i in range(n)]
	for j in range(len(a[0])):
		r = [0]*n
		# pivoteo
		if j < n:
			a, P, Q = pivot(a, P, Q, j, piv)

		for i in range(j+1, n):		
			
			#Eliminacion de gauss
			r[i] = a[i][j] / float(a[j][j])
                        r[i] = round(r[i], 5)
			for k in range(j, len(a[0])):
				a[i][k] = a[i][k] - r[i]*a[j][k]
				a[i][k] = round(a[i][k], 5)	
		if j < n:
			temp = [0]*n
			if (temp != r):
				print 'L%d' % (j+1)
				printMatrix(L(n, r, j))			

	print 'A|b:'			
	printMatrix(a)

	if piv == 2:
		return multi(Q, reverseSub(a))	

	return reverseSub(a)			

def gaussJordan(A, b, piv=0):
 	

	a = aumentada(A, b)
	n_rows = len(a)
	n_cols = len(a[0])
	P = [[float(i == j) for j in range(n_rows)] for i in range(n_rows)]
	Q = [[float(i == j) for j in range(n_rows)] for i in range(n_rows)]
	for j in range(n_cols): #0, 1, 2, 3, 4
		r = [0]*n_rows
		for i in range(j+1, n_rows+1):		
			#pivoteo
			if i < n_rows:
				a, P, Q = pivot(a, P, Q, j, piv)

			if i == j+1:			
			#Eliminacion de gauss			
				for m in range(j):
					r[m] = a[m][j] / float(a[j][j])
                                        r[m]=round(r[m], 5)
				for l in range(j):
					for k in range(j, n_cols):
						if l < n_rows:
							a[l][k] = a[l][k] - r[l]*a[j][k]
                                                        a[l][k] = round(a[l][k], 5)
			if i < n_rows:		
				r[i] = a[i][j] / float(a[j][j])
				#r[i] = round(r[i][j], 5)			
				for k in range(j, n_cols):
					a[i][k] = a[i][k] - r[i]*a[j][k]				
                                        a[i][k] = round(a[i][k], 5)
		if j < n_rows:
			temp = [0]*n_rows
			if (temp != r):
				print 'T%d' % (j+1)
				printMatrix(T(n_rows, r, j))			

	#para convertir la diagonal en 1's.
	for i in range(n_rows):
		temp = float(a[i][i])
		for j in range(n_cols):
			a[i][j] = a[i][j] / temp

	print 'A|b:'			
	printMatrix(a)
	if piv == 2:
		return multi(Q, reverseSub(a))	

	return reverseSub(a)	

def croutLU1(A, piv=0):
	"""Calcula el metodo LU1"""

	n = len(A)
	L = [[0.0]*n for j in range(n)];
	U = [[float(i == j) for j in range(n)] for i in range(n)]
	P = [[float(i == j) for j in range(n)] for i in range(n)]
	Q = [[float(i == j) for j in range(n)] for i in range(n)]

	#pivot
	if piv:
		for j in range(len(A)):
			A, P, Q = pivot(A, P, Q, j, piv)

	for k in range(n):
		for i in range(k, n):
			L[i][k] = A[i][k] - sum(L[i][p]*U[p][k] for p in range(k))
                        L[i][k] = round(L[i][k], 5)
		for i in range(k+1, n):
			if L[k][k] == 0:
				exit('Debe usarse pivoteo parcial')
			U[k][i] = (A[k][i] - sum(L[k][p]*U[p][i] for p in range(k))) / float(L[k][k])	
                        U[k][i] = round(U[k][i], 5)
	if piv == 2:
		return P, Q, L, U	
	return P, L, U

def croutL1U(A, piv=0):
	"""Calcula el metodo L1U"""

	n = len(A)
	U = [[0.0]*n for j in range(n)];
	L = [[float(i == j) for j in range(n)] for i in range(n)]
	P = [[float(i == j) for j in range(n)] for i in range(n)]
	Q = [[float(i == j) for j in range(n)] for i in range(n)]

	#pivot
	if piv:
		for j in range(len(A)):
			A, P, Q = pivot(A, P, Q, j, piv)

	for k in range(n):
		for i in range(k, n):
			U[k][i] = A[k][i] - sum(L[k][p]*U[p][i] for p in range(k))
		        U[k][i] = round(U[k][i], 5)
		for i in range(k+1, n):
			if U[k][k] == 0:
				exit('Debe usarse pivoteo parcial')
			L[i][k] = (A[i][k] - sum(L[i][p]*U[p][k] for p in range(k))) / float(U[k][k])	
	                L[i][k] = round(L[i][k], 5)
	if piv == 2:
		return P, Q, L, U

	return P, L, U

def Doolittle(A, piv=0):

	n = len(A)
	U = [[0.0]*n for j in range(n)]
	L = [[float(i == j) for j in range(n)] for i in range(n)]
	P = [[float(i == j) for j in range(n)] for i in range(n)]
	Q = [[float(i == j) for j in range(n)] for i in range(n)]

	#pivot
	if piv:
		for j in range(len(A)):
			A, P, Q = pivot(A, P, Q, j, piv)

	for k in range(n):
		for i in range(n):
			U[k][i] = A[k][i] - sum(L[k][p]*U[p][i] for p in range(k))
                        U[k][i] = round(U[k][i], 5)
		for i in range(k, n):
			if U[k][k] == 0:
				exit('Debe usarse pivoteo parcial')
			L[i][k] = (A[i][k] - sum(L[i][p]*U[p][k] for p in range(k))) / float(U[k][k])	
                        L[i][k] = round(L[i][k], 5)
	if piv == 2:
		return P, Q, L, U
	return P, L, U

def LDMt(A, piv=0):
	""""""
	if piv == 2:
		P, I, L, U = croutLU1(A, piv)
	else:
		P, L, U = croutLU1(A, piv)

	D, M = diagonalDMt(U)
	return L, D, M

def diagonalDMt(U):

	n = len(U)
	D = [[float(i == j) for j in range(n)] for i in range(n)]
	for i in range(n):
		D[i][i] = float(U[i][i])
		D[i][j] = round(U[i][j], 5)
	for i in range(n):
		for j in range(n):
			U[i][j] /= (D[i][i])
                        U[i][j] = round(U[i][j], 5)
	return D, U

def cholesky(A):
	if not Matrizsimetrica(A):
		exit('La matriz no es simetrica')
	n = len(A)
	G = [[0.0]*n for j in range(n)]
	for i in range(n):
		suma = A[i][i]
		for k in range(i):
			suma -= A[k][i]**2
		if suma < 0:
			exit('No es definida positiva')	
		A[i][i] = sqrt(suma)
		for j in range(i+1, n):
			suma = A[i][j]
			for k in range(i):
				suma -= A[k][i]*A[k][j]
			A[i][j] = suma / A[i][i]
                        A[i][j] = round(A[i][j], 5)

	for j in range(n):
		for i in range(n):
			if(i > j):
				A[i][j] = 0.0
	return A	



def menu():

	opc = 1
	while(opc):
		print "Metodo a usar:\n"
		print """
			1.  Eliminacion Gauss
			2.  Gauss-Jordan
			3.  Factorizacion Crout LU1
			4.  Factorizacion Crout L1U
			5.  Doolittle
			6.  LDMt
			7.  Factorizacion Cholesky		
			8. Salir
			  """
		#opc = input('Ingrese opcion\n')
                opc = 6	
		if type(opc) != type(1):
			exit('vuela a intentarlo')
		if opc == 16:
			exit('Salir')
		if opc < 0 or opc > 16:
			print 'Opcion incorrecta'
			continue
		
		Matrix = inputMatrix()		 		
		#Matrix = [
		#		[1, -4, 2, 1],
		 #		[2, -6, 1, 4],
		 #		[-1, 2, 3, 4],
		 #		[0, -1, 1, 1]
		 #		]		 		
		#El condicionamiento no necesita el vector b
		if opc != 15:
			
			b = inputVector(Matrix)
	 	 
			#b = [-4, 1, 12, 0]	 	 
			restric = [7, 10, 11, 12, 13, 14, 3, 4 ,5 ,6]
			if opc not in restric:
				print "Elija el pivoteo a usar:\n"
				print """
					0.  Sin pivoteo
					1.  Pivoteo parcial
					2.  Pivoteo total
						
					  """
				#piv = int(raw_input('Ingrese opcion\n'))
 				piv = 1
		#Gauss
		if opc == 1:
			x = gauss(Matrix, b, piv)
			print 'x:'
			print ["%0.5f" % i for i in x]
			#print x
                        exit()
		#Gauss-Jordan	
		elif opc == 2:
			x = gaussJordan(Matrix, b, piv)
			print 'x:'
			print ["%0.5f" % i for i in x]
			#print x
                        exit()
		#croutLU1, croutL1U, Doolittle
		elif opc == 3 or opc == 4 or opc == 5:
			#croutLU1
                        piv = 1
			if opc == 3:
				
					
					P, L, U = croutLU1(Matrix, piv)
			#croutL1U		
			elif opc == 4:
				
					P, L, U = croutL1U(Matrix, piv)
			#Doolittle		
			elif opc == 5:
			
					P, L, U = Doolittle(Matrix, piv)			

			#Imprimir las matrices	
			print 'P:'
			printMatrix(P)
			if piv == 2:
				print 'Q:'
				printMatrix(Q)		
			print 'L:'
			printMatrix(L)
			print 'U:'
			printMatrix(U)
		
			#calcula las soluciones de Lz=b y Ux=z	
			if piv == 2:
				z = solMatrixInf(L, b)
				y = solMatrixSup(U,z)
				x = multi(P, y)
			else:
				z = solMatrixInf(L, b)
				x = solMatrixSup(U,z) 	

			#imprime las soluciones
			print "z:"
			print z
			print "x:"
			print ["%0.5f" % i for i in x]
			#print x
                      
                        exit()
		#LDMt
		elif opc == 6:
			L,D,M = LDMt(Matrix, 1)
			print 'L:'
			printMatrix(L)		
			print "D:"
			printMatrix(D)
			print "M:"
			printMatrix(M)

			#calcula las soluciones
			y = solMatrixInf(L, b)
			z = solMatrixInf(D, y)
			x = solMatrixSup(M, z)
			
			#imprime las soluciones
			print "y:"
			print y
			print "z:"
			print z
			print "x:"
			print ["%0.5f" % i for i in x]
			#print x
                        exit()
		#Cholesky
		elif opc == 7:
			G = cholesky(Matrix)
			Gt = trans(G) 
			print "G:"
			printMatrix(G)
			print "Gt:"
			printMatrix(Gt)

			#calcula las soluciones
			z = solMatrixInf(Gt, b)
			x = solMatrixSup(G, z)
			
			#imprime las soluciones
			print "z:"
			print z
			print "x:"
			print ["%0.5f" % i for i in x]
			#print x
                        exit()
		
        
	print 'Resultado obtenido con exito'	
 
if __name__ == '__main__':
	menu()	
