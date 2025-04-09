class Nodo:
    def __init__(self, valor):
        """Inicializa el nodo con un valor y apunta a None (sin siguiente nodo)."""
        self.valor = valor
        self.siguiente = None

    def __str__(self):
        """Devuelve una representación en cadena del valor del nodo."""
        return str(self.valor)

class ListaEnlazada:
    def __init__(self):
        """Inicializa la lista vacía (sin nodos)."""
        self.cabeza = None

    def agregar_al_final(self, valor):
        """Agrega un nuevo nodo con el valor al final de la lista."""
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def agregar_al_principio(self, valor):
        """Agrega un nuevo nodo con el valor al principio de la lista."""
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar(self, valor):
        """Elimina el primer nodo que contiene el valor especificado."""
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  
            anterior = actual
            actual = actual.siguiente
        return False 

    def mostrar(self):
        """Muestra todos los valores de la lista enlazada."""
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(str(actual.valor))
            actual = actual.siguiente
        return " -> ".join(valores) if valores else "Lista vacía."

    def contar_nodos(self):
        """Cuenta el número de nodos en la lista enlazada."""
        count = 0
        actual = self.cabeza
        while actual:
            count += 1
            actual = actual.siguiente
        return count

    def invertir(self):
        """Invierte el orden de los nodos en la lista."""
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente  
            actual.siguiente = anterior 
            anterior = actual  
            actual = siguiente 
        self.cabeza = anterior  

    def obtener_nodo(self, posicion):
        """Devuelve el valor del nodo en una posición específica (empezando desde 0)."""
        actual = self.cabeza
        index = 0
        while actual:
            if index == posicion:
                return actual.valor  
            actual = actual.siguiente
            index += 1
        return None  
