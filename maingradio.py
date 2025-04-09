import gradio as gr
import subprocess
import sys
import os

# Ruta absoluta al script original (ajústala si es necesario)
script_path = os.path.abspath("main.py")

def lanzar_simulacion(opcion):
    if opcion == "N-Reinas":
        comando = [sys.executable, script_path, "1"]
    elif opcion == "Torres de Hanoi":
        comando = [sys.executable, script_path, "2"]
    elif opcion == "Movimiento del Caballo":
        comando = [sys.executable, script_path, "3"]
    else:
        return "Opción no válida."

    subprocess.Popen(comando)
    return f"Lanzando {opcion}..."

interface = gr.Interface(
    fn=lanzar_simulacion,
    inputs=gr.Dropdown(["N-Reinas", "Torres de Hanoi", "Movimiento del Caballo"]),
    outputs="text",
    title="Simulaciones en Pygame",
    description="Selecciona una simulación para ejecutar en tu sistema local (Pygame)."
)

if __name__ == "__main__":
    interface.launch()
