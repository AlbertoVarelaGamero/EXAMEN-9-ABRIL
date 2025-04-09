import pygame



class Caballos:
    def __init__(self, origen, destino=None):
        self.origen = self._notacion_a_coordenadas(origen)
        self.destino = self._notacion_a_coordenadas(destino) if destino else None

    def __repr__(self):
        origen_alg = self._coordenadas_a_notacion(self.origen)
        destino_alg = self._coordenadas_a_notacion(self.destino) if self.destino else "None"
        return f"Caballo(origen='{origen_alg}', destino='{destino_alg}')"

    def movimiento_valido(self):
        if self.destino is None:
            return False
        x1, y1 = self.origen
        x2, y2 = self.destino
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return (dx, dy) in [(2, 1), (1, 2)]

    def mostrar_validacion(self):
        if self.movimiento_valido():
            return "Movimiento válido para el caballo."
        else:
            return "Movimiento inválido para el caballo."

    def movimientos_posibles(self):
        movimientos = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        posibles = []
        x, y = self.origen
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                posibles.append(self._coordenadas_a_notacion((nx, ny)))
        return posibles

    def _notacion_a_coordenadas(self, notacion):
        if notacion is None:
            return None
        columna = ord(notacion[0].lower()) - ord('a') 
        fila = 8 - int(notacion[1]) 
        return (fila, columna)

    def _coordenadas_a_notacion(self, coord):
        if coord is None:
            return None
        fila, columna = coord
        letra = chr(columna + ord('a'))  
        numero = str(8 - fila)           
        return f"{letra}{numero}"
    
"""
# Ejemplo de uso
if __name__ == "__main__":
    caballo = Caballos("e4", "f6")
    print(caballo)  
    print(caballo.movimiento_valido())  
    print(caballo.mostrar_validacion())  
    print(caballo.movimientos_posibles())  
"""
