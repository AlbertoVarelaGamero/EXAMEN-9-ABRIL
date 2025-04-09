class NodoConcreto:
    def __init__(self, valor=None):
        self._valor = valor
        self._siguiente = None

    def obtener_valor(self):
        return self._valor

    def establecer_valor(self, valor):
        self._valor = valor

    def obtener_siguiente(self):
        return self._siguiente

    def establecer_siguiente(self, nodo):
        self._siguiente = nodo


class ListaEnlazada:
    def __init__(self):
        self._cabeza = None
        self._tamaño = 0  

    def agregar(self, valor):
        nuevo_nodo = NodoConcreto(valor)
        if not self._cabeza:
            self._cabeza = nuevo_nodo
        else:
            actual = self._cabeza
            while actual.obtener_siguiente():
                actual = actual.obtener_siguiente()
            actual.establecer_siguiente(nuevo_nodo)
        self._tamaño += 1  

    def agregar_al_principio(self, valor):
        nuevo_nodo = NodoConcreto(valor)
        nuevo_nodo.establecer_siguiente(self._cabeza)
        self._cabeza = nuevo_nodo
        self._tamaño += 1  

    def eliminar(self, valor):
        actual = self._cabeza
        previo = None
        while actual:
            if actual.obtener_valor() == valor:
                if previo:
                    previo.establecer_siguiente(actual.obtener_siguiente())
                else:
                    self._cabeza = actual.obtener_siguiente() 
                self._tamaño -= 1  
                return True
            previo = actual
            actual = actual.obtener_siguiente()
        return False  

    def buscar(self, valor):
        actual = self._cabeza
        while actual:
            if actual.obtener_valor() == valor:
                return True
            actual = actual.obtener_siguiente()
        return False  

    def tamaño(self):
        return self._tamaño

    def mostrar(self):
        actual = self._cabeza
        while actual:
            print(actual.obtener_valor(), end=" -> ")
            actual = actual.obtener_siguiente()
        print("None")

# EJEMPLO DE USO
"""
# Crear una lista enlazada
lista = ListaEnlazada()

# Agregar elementos
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)

# Mostrar la lista
lista.mostrar()  # Salida: 10 -> 20 -> 30 -> None

# Agregar al principio
lista.agregar_al_principio(5)
lista.mostrar()  # Salida: 5 -> 10 -> 20 -> 30 -> None

# Eliminar un nodo
lista.eliminar(20)
lista.mostrar()  # Salida: 5 -> 10 -> 30 -> None

# Buscar un valor
print(lista.buscar(10))  # Salida: True
print(lista.buscar(99))  # Salida: False

# Mostrar el tamaño de la lista
print(f"Tamaño de la lista: {lista.tamaño()}")  # Salida: 3
    
    """