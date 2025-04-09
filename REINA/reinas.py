class Reinas:
    def __init__(self, origen, destino):
        self.origen = origen  
        self.destino = destino  
        self.posicion_actual = origen  

    def __repr__(self):
        return f"Reina(origen={self.origen}, destino={self.destino}, posición_actual={self.posicion_actual})"
    
    def es_movimiento_valido(self, tablero):
        fila_origen, col_origen = self.origen
        fila_destino, col_destino = self.destino
        
        if fila_origen == fila_destino:  
            paso_col = 1 if col_destino > col_origen else -1
            for col in range(col_origen + paso_col, col_destino, paso_col):
                if tablero[fila_origen][col] != 0:  
                    return False
            return True
        elif col_origen == col_destino:  
            paso_fila = 1 if fila_destino > fila_origen else -1
            for fila in range(fila_origen + paso_fila, fila_destino, paso_fila):
                if tablero[fila][col_origen] != 0:  
                    return False
            return True
        elif abs(fila_origen - fila_destino) == abs(col_origen - col_destino):  
            paso_fila = 1 if fila_destino > fila_origen else -1
            paso_col = 1 if col_destino > col_origen else -1
            fila, col = fila_origen + paso_fila, col_origen + paso_col
            while fila != fila_destino and col != col_destino:
                if tablero[fila][col] != 0:  
                    return False
                fila += paso_fila
                col += paso_col
            return True
        return False

    def mover(self, tablero):
        if self.es_movimiento_valido(tablero):
            fila_origen, col_origen = self.origen
            fila_destino, col_destino = self.destino
            

            if tablero[fila_destino][col_destino] == 0:
                tablero[fila_destino][col_destino] = 1  
                tablero[fila_origen][col_origen] = 0  
                self.posicion_actual = self.destino  
                return True
        return False

    def mostrar_tablero(self, tablero):
        for fila in tablero:
            print(" ".join(str(celda) for celda in fila))
        print() 










# Ejemplo de uso:
"""
tablero = [[0] * 8 for _ in range(8)]  


reina = Reinas((0, 0), (4, 4))  
tablero[0][0] = 1  


print("Tablero antes del movimiento:")
reina.mostrar_tablero(tablero)


if reina.mover(tablero):
    print("Movimiento realizado con éxito!")
else:
    print("Movimiento inválido.")


print("Tablero después del movimiento:")
reina.mostrar_tablero(tablero)
"""
