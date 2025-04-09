import pygame
import sys

class Lanzador:
    """Clase que representa el problema de las N-Reinas, ajustada para main.py."""
    def __init__(self):
        # Usamos 8 reinas por defecto para no requerir argumentos
        self.n = 8
        self.soluciones = []

    def es_valida(self, tablero, fila, columna):
        """Verifica si una posición es válida para colocar una reina."""
        for i in range(fila):
            if tablero[i] == columna or abs(tablero[i] - columna) == abs(i - fila):
                return False
        return True

    def resolver(self, fila=0, tablero=None):
        """Resuelve el problema de las N-Reinas."""
        if tablero is None:
            tablero = [-1] * self.n

        if fila == self.n:
            self.soluciones.append(tablero[:])
            return

        for columna in range(self.n):
            if self.es_valida(tablero, fila, columna):
                tablero[fila] = columna
                self.resolver(fila + 1, tablero)
                tablero[fila] = -1

    def obtener_soluciones(self):
        """Devuelve todas las soluciones encontradas."""
        self.soluciones = []  # Reiniciamos para evitar acumulaciones
        self.resolver()
        return self.soluciones

    @staticmethod
    def inicializar_pygame():
        """Inicializa Pygame y configura la ventana."""
        pygame.init()
        WIDTH, HEIGHT = 800, 800
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("N-Reinas")
        return screen

    @staticmethod
    def obtener_colores():
        """Define los colores utilizados en la aplicación."""
        return {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "BLUE": (0, 0, 255),
            "RED": (255, 0, 0),
            "GREEN": (0, 255, 0),
            "YELLOW": (255, 255, 0)
        }

    def dibujar_tablero(self, screen, colores, solucion):
        """Dibuja el tablero de ajedrez y las reinas."""
        cell_size = 800 // self.n
        for fila in range(self.n):
            for columna in range(self.n):
                color = colores["WHITE"] if (fila + columna) % 2 == 0 else colores["BLACK"]
                pygame.draw.rect(screen, color, (columna * cell_size, fila * cell_size, cell_size, cell_size))

                # Dibujar reina si está en esta posición
                if solucion[fila] == columna:
                    pygame.draw.circle(screen, colores["RED"], 
                                       (columna * cell_size + cell_size // 2, fila * cell_size + cell_size // 2), 
                                       cell_size // 3)

    def dibujar_estadisticas(self, screen, colores, solucion, num_solucion, total_soluciones):
        """Dibuja las estadísticas y las posiciones de las reinas."""
        font = pygame.font.Font(None, 30)
        
        # Mostrar el número de solución
        texto_solucion = f"Solución {num_solucion + 1} de {total_soluciones}"
        texto_surface = font.render(texto_solucion, True, colores["BLUE"])
        screen.blit(texto_surface, (10, 10))

        # Mostrar las posiciones de las reinas
        texto_posiciones = f"Posiciones de las reinas: {', '.join(str(x + 1) for x in solucion)}"
        texto_surface = font.render(texto_posiciones, True, colores["YELLOW"])
        screen.blit(texto_surface, (10, 40))

    def ejecutar_simulacion(self):
        """Ejecuta la simulación visual de las soluciones de N-Reinas."""
        screen = self.inicializar_pygame()
        colores = self.obtener_colores()
        soluciones = self.obtener_soluciones()

        clock = pygame.time.Clock()
        running = True
        indice_solucion = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        indice_solucion = (indice_solucion + 1) % len(soluciones)
                    elif event.key == pygame.K_LEFT:
                        indice_solucion = (indice_solucion - 1) % len(soluciones)

            screen.fill(colores["WHITE"])
            self.dibujar_tablero(screen, colores, soluciones[indice_solucion])
            self.dibujar_estadisticas(screen, colores, soluciones[indice_solucion], indice_solucion, len(soluciones))

            pygame.display.flip()
            clock.tick(30)

        # No llamamos a pygame.quit() ni sys.exit() para regresar al menú de main.py

if __name__ == "__main__":
    juego = Lanzador()
    juego.ejecutar_simulacion()