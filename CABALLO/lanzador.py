import random
import time
import sys
import pygame

class Lanzador:
    def __init__(self):
        # Movimientos posibles del caballo desde cada tecla (forma de L)
        self.movimientos = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

    def contar_movimientos(self, pos, movimientos_restantes):
        if movimientos_restantes == 0:
            return 1
        total = 0
        for siguiente in self.movimientos[pos]:
            total += self.contar_movimientos(siguiente, movimientos_restantes - 1)
        return total

    def calcular_movimientos_iniciales(self, num_movimientos):
        total = 0
        for inicio in range(10):
            total += self.contar_movimientos(inicio, num_movimientos - 1)
        return total

    @staticmethod
    def inicializar_pygame():
        pygame.init()
        WIDTH, HEIGHT = 800, 600
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Movimientos del Caballo en el Teclado")
        return screen

    @staticmethod
    def obtener_colores():
        return {
            "WHITE": (255, 255, 255),
            "BLUE": (0, 0, 255),
            "GREEN": (0, 255, 0),
            "RED": (255, 0, 0),
            "BLACK": (0, 0, 0)
        }

    @staticmethod
    def obtener_teclas_posiciones():
        return {
            1: (200, 100), 2: (300, 100), 3: (400, 100),
            4: (200, 200), 5: (300, 200), 6: (400, 200),
            7: (200, 300), 8: (300, 300), 9: (400, 300),
            0: (300, 400)
        }

    @staticmethod
    def dibujar_teclas(screen, teclas_posiciones, colores):
        for tecla, (x, y) in teclas_posiciones.items():
            pygame.draw.circle(screen, colores["BLUE"], (x, y), 30)
            font = pygame.font.SysFont(None, 24)
            texto = font.render(str(tecla), True, colores["WHITE"])
            screen.blit(texto, (x - 10, y - 10))

    def dibujar_conexiones(self, screen, teclas_posiciones, colores):
        for origen, destinos in self.movimientos.items():
            x1, y1 = teclas_posiciones[origen]
            for destino in destinos:
                x2, y2 = teclas_posiciones[destino]
                pygame.draw.line(screen, colores["GREEN"], (x1, y1), (x2, y2), 2)

    @staticmethod
    def mostrar_resultados(screen, num_movimientos, total, colores):
        font = pygame.font.SysFont(None, 36)
        texto = font.render(f"Movimientos válidos con {num_movimientos} paso(s): {total}", True, colores["BLACK"])
        screen.blit(texto, (50, 500))

    def ejecutar_simulacion(self, num_movimientos=2):
        screen = self.inicializar_pygame()
        colores = self.obtener_colores()
        teclas_posiciones = self.obtener_teclas_posiciones()

        clock = pygame.time.Clock()
        running = True

        while running:
            screen.fill(colores["WHITE"])

            self.dibujar_teclas(screen, teclas_posiciones, colores)
            self.dibujar_conexiones(screen, teclas_posiciones, colores)

            total_movimientos = self.calcular_movimientos_iniciales(num_movimientos)

            self.mostrar_resultados(screen, num_movimientos, total_movimientos, colores)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            clock.tick(60)
        # Sin pygame.quit() ni sys.exit() para que el menú siga activo

# Ejecución directa desde consola (opcional)
if __name__ == "__main__":
    lanzador = Lanzador()
    try:
        pasos = int(input("Introduce el número de movimientos: "))
    except ValueError:
        pasos = 2
        print("Entrada inválida. Usando 2 pasos por defecto.")
    lanzador.ejecutar_simulacion(pasos)