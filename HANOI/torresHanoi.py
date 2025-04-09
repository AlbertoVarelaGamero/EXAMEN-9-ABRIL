
import pygame

WIDTH, HEIGHT = 800, 600
TOWER_WIDTH = 20
DISK_HEIGHT = 30
DISK_GAP = 5
FPS = 60

WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class TorresDeHanoi:
    def __init__(self, discos):
        self.discos = discos
        self.torres = [list(range(discos, 0, -1)), [], []]
        self.selected_disk = None
        self.selected_tower = None

    def mover(self, origen, destino):
        """Mueve un disco de una torre a otra."""
        if self.torres[origen] and (not self.torres[destino] or self.torres[origen][-1] < self.torres[destino][-1]):
            disco = self.torres[origen].pop()
            self.torres[destino].append(disco)
            return True
        return False

    def es_victoria(self):
        """Comprueba si el jugador ha ganado."""
        return len(self.torres[2]) == self.discos

    def resolver(self):
        """Ejecuta el juego interactivo en lugar de resolver automáticamente."""
        # Configuración de Pygame
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Torres de Hanoi - Juego")
        clock = pygame.time.Clock()

        mensaje = "Selecciona un disco"
        victoria = False
        running = True

        while running:
            screen.fill(WHITE)

            self.draw_towers(screen)
            self.draw_disks(screen)
            self.draw_text(screen, mensaje, 10, 10)

            if victoria:
                self.draw_text(screen, "¡Ganaste! Presiona R para reiniciar", WIDTH // 2 - 200, HEIGHT // 2, size=40, color=GREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not victoria:
                    x, y = pygame.mouse.get_pos()
                    tower_index = self.get_tower_index(x)

                    if tower_index is not None:
                        if self.selected_disk is None:
                            if self.torres[tower_index]:
                                self.selected_disk = self.torres[tower_index][-1]
                                self.selected_tower = tower_index
                                mensaje = f"Disco {self.selected_disk} seleccionado"
                            else:
                                mensaje = "No hay discos en esta torre"
                        else:
                            if self.mover(self.selected_tower, tower_index):
                                mensaje = "Movimiento realizado"
                                if self.es_victoria():
                                    victoria = True
                                    mensaje = "¡Ganaste!"
                            else:
                                mensaje = "Movimiento inválido"
                            self.selected_disk = None
                            self.selected_tower = None
                elif event.type == pygame.KEYDOWN and victoria:
                    if event.key == pygame.K_r:
                        self.torres = [list(range(self.discos, 0, -1)), [], []]
                        victoria = False
                        mensaje = "Selecciona un disco"

            pygame.display.flip()
            clock.tick(FPS)

    def draw_towers(self, screen):
        """Dibuja las tres torres."""
        tower_x = [200, 400, 600]
        for i, x in enumerate(tower_x):
            pygame.draw.rect(screen, GRAY, (x - TOWER_WIDTH//2, HEIGHT - 150, TOWER_WIDTH, 150))
            pygame.draw.line(screen, BLACK, (x - TOWER_WIDTH//2, HEIGHT - 150), (x + TOWER_WIDTH//2, HEIGHT - 150), 5)

    def draw_disks(self, screen):
        """Dibuja los discos en las torres."""
        tower_x = [200, 400, 600]
        for t in range(3):
            for i, disk in enumerate(self.torres[t]):
                disk_width = disk * 40
                color = RED if self.selected_disk == disk else BLUE
                pygame.draw.rect(screen, color, 
                                 (tower_x[t] - disk_width // 2, HEIGHT - 150 - (i + 1) * (DISK_HEIGHT + DISK_GAP), 
                                  disk_width, DISK_HEIGHT))

    def draw_text(self, screen, text, x, y, size=30, color=BLACK):
        """Dibuja texto en la pantalla."""
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

    def get_tower_index(self, x):
        """Devuelve el índice de la torre según la posición del click."""
        if 200 - TOWER_WIDTH // 2 < x < 200 + TOWER_WIDTH // 2:
            return 0
        elif 400 - TOWER_WIDTH // 2 < x < 400 + TOWER_WIDTH // 2:
            return 1
        elif 600 - TOWER_WIDTH // 2 < x < 600 + TOWER_WIDTH // 2:
            return 2
        return None

    def __str__(self):
        """Representación en cadena del estado de las torres (placeholder)."""
        return f"Torre 1: {self.torres[0]}\nTorre 2: {self.torres[1]}\nTorre 3: {self.torres[2]}"

if __name__ == "__main__":
    pygame.init()
    game = TorresDeHanoi(3)
    game.resolver()
    pygame.quit()