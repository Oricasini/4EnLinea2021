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
		fichaNumero = 1 + (i % 2)
		soltarFichaEnColumna(fichaNumero, columna, tablero)
	return tablero

def soltarFichaEnColumna(ficha, columna, tablero):
	for fila in range(6, 0, -1):
		if tablero [fila-1] [columna-1] == 0:
			tablero [fila -1] [columna-1] = ficha
			return

def dibujarTablero(tablero):
		for fila in tablero:
			for celda in fila:
				if celda == 0:
					print('  ', end = '')
				else:
					print(' %s' % celda, end = '')
				print('')

def contenidoFila(nroFila, tablero):
	return tablero[fila-1]

def contenidoColumna(nroColumna, tablero):
	return tablero[columna-1]

secuencia = [1, 2, 3, 1]
dibujarTablero(completarTableroEnOrden(secuencia, tableroVacio))