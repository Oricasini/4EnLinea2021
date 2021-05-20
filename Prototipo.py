def tableroVacio():
	return [
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			]

def completarTableroEnOrden(secuencia,tablero):
	for i, columna in enumerate(secuencia):
		if i % 2 :
			fichaNumero = 2 
		else:
			fichaNumero = 1
		soltarFichaEnColumna(fichaNumero, columna, tablero)
	return tablero

def soltarFichaEnColumna(ficha, columna, tablero):
	for fila in range(6, 0, -1):
		if tablero [fila - 1] [columna - 1] == 0:
			tablero [fila - 1] [columna - 1] = ficha
			return

def marcoTablero(tablero):			#Modifique la función anterior (dibujarTablero) para crear marcoTablero y así mostrar una mejor estetica
	for fila in tablero:
			print("║", end =" ")
			for celda in fila:
				if celda == 0:
				  	print(' o ', end = '')
				else:
					print(' %s ' % celda, end = '')
			print('║')	
	print("╚══════════════════════╝")

def secuenciaValida(secuencia):
	for columna in secuencia:
		if columna < 1 or columna > 7:
			return False
	return True

def contenidoColumna(nro_columna, tablero):
	columna = []
	for fila in tablero:
		celda = fila[nro_columna - 1]
		columna.append(celda)
	return columna

def todasColumnas(tablero):
	columnas = []
	for i in range(7):
		columna = contenidoColumna((i+1), tablero)
		columnas.append(columna)
	return columnas

def contenidoFila(nro_fila, tablero):
    fila = tablero[nro_fila-1]
    return fila

def todasFilas(tablero):
	return tablero

secuencia = [1, 2, 3, 1]

tablero = []
if secuenciaValida(secuencia):
	tablero = completarTableroEnOrden(secuencia, tableroVacio())
	marcoTablero(tablero)
else:
	print("Las columnas deberian ir de 1 al 7")




