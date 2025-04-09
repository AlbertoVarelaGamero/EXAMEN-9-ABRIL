
from nodo import Nodo  

class NodoConcreto(Nodo):
    def __init__(self, valor=None):
        super().__init__(valor)  
        self._valor = valor
        self._siguiente = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, nuevo_valor):
        self._valor = nuevo_valor

    @property
    def siguiente(self):
        return self._siguiente

    @siguiente.setter
    def siguiente(self, nodo):

        if isinstance(nodo, NodoConcreto) or nodo is None:
            self._siguiente = nodo
        else:
            raise TypeError("El siguiente nodo debe ser una instancia de NodoConcreto o None")

    def __str__(self):
        return str(self._valor)

    def __repr__(self):
        return f"NodoConcreto(valor={self._valor}, siguiente={repr(self._siguiente)})"
    
# EJEMPLO DE USO
"""
# main.py
from nodo_concreto import NodoConcreto  # Importa NodoConcreto desde nodo_concreto.py

# Crear nodos
nodo1 = NodoConcreto(5)  # Nodo con valor 5
nodo2 = NodoConcreto(10)  # Nodo con valor 10
nodo3 = NodoConcreto(15)  # Nodo con valor 15

# Establecer los siguientes nodos
nodo1.siguiente = nodo2  # El siguiente de nodo1 es nodo2
nodo2.siguiente = nodo3  # El siguiente de nodo2 es nodo3

# Recorrer la lista enlazada e imprimir los valores
current_node = nodo1
while current_node is not None:
    print(f"Valor del nodo: {current_node.valor}")
    current_node = current_node.siguiente  # Avanzar al siguiente nodo
"""
