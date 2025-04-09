import sys
import os
import pygame

# Añadir las rutas de las subcarpetas para importar los módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'REINA'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'HANOI'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'CABALLO'))

# Importamos los lanzadores y clases necesarias
from REINA.lanzador import Lanzador as ReinaLanzador  # Ahora correcto con el nuevo REINA/lanzador.py
from HANOI.torresHanoi import TorresDeHanoi          # Compatible con la versión jugable
from CABALLO.lanzador import Lanzador as CaballoLanzador  # Ya funciona perfectamente

def ejecutar_n_reinas():
    """Ejecuta el ejercicio de N-Reinas en Pygame."""
    print("Ejecutando el ejercicio de N-Reinas...")
    lanzador = ReinaLanzador()  # Crea una instancia con 8 reinas por defecto
    lanzador.ejecutar_simulacion()  # Abre la simulación interactiva

def ejecutar_torres_de_hanoi():
    """Ejecuta el ejercicio de Torres de Hanoi en Pygame."""
    print("Ejecutando el ejercicio de Torres de Hanoi...")
    torres = TorresDeHanoi(6)  # 6 discos, como estaba
    torres.resolver()  # Lanza el juego interactivo (o automático, según tu versión)
    print(torres)  # Imprime el estado final

def ejecutar_caballo():
    """Ejecuta el ejercicio de Movimiento del Caballo en Pygame."""
    print("Ejecutando el ejercicio de Movimiento del Caballo...")
    lanzador = CaballoLanzador()
    try:
        pasos = int(input("Introduce el número de movimientos para el caballo: "))
    except ValueError:
        pasos = 2
        print("Entrada inválida. Usando 2 pasos por defecto.")
    lanzador.ejecutar_simulacion(pasos)  # Simulación ya funcionando

def main():
    """Menú principal para seleccionar y ejecutar ejercicios."""
    pygame.init()
    while True:
        print("\nElige el ejercicio que deseas ejecutar:")
        print("1. N-Reinas")
        print("2. Torres de Hanoi")
        print("3. Movimiento del Caballo")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1/2/3/4): ")

        if opcion == "1":
            ejecutar_n_reinas()
        elif opcion == "2":
            ejecutar_torres_de_hanoi()
        elif opcion == "3":
            ejecutar_caballo()
        elif opcion == "4":
            print("Saliendo del programa...")
            pygame.quit()
            sys.exit()
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()