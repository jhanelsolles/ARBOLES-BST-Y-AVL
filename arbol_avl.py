class NodoAVL:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_factor_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izq) - self.obtener_altura(nodo.der)

    def rotacion_derecha(self, y):
        x = y.izq
        T2 = x.der

        # Rotación
        x.der = y
        y.izq = T2

        # Actualizar alturas
        y.altura = 1 + max(self.obtener_altura(y.izq), self.obtener_altura(y.der))
        x.altura = 1 + max(self.obtener_altura(x.izq), self.obtener_altura(x.der))

        return x

    def rotacion_izquierda(self, x):
        y = x.der
        T2 = y.izq

        # Rotación
        y.izq = x
        x.der = T2

        # Actualizar alturas
        x.altura = 1 + max(self.obtener_altura(x.izq), self.obtener_altura(x.der))
        y.altura = 1 + max(self.obtener_altura(y.izq), self.obtener_altura(y.der))

        return y

    def insertar(self, nodo, clave):
        # 1. Insertar nodo como en un ABB normal
        if not nodo:
            return NodoAVL(clave)

        if clave < nodo.clave:
            nodo.izq = self.insertar(nodo.izq, clave)
        elif clave > nodo.clave:
            nodo.der = self.insertar(nodo.der, clave)
        else:
            # Claves duplicadas no permitidas
            return nodo

        # 2. Actualizar altura del nodo actual
        nodo.altura = 1 + max(self.obtener_altura(nodo.izq), self.obtener_altura(nodo.der))

        # 3. Obtener factor de balance para verificar desbalance
        balance = self.obtener_factor_balance(nodo)

        # 4. Casos de desbalance y rotaciones

        # Caso Left Left
        if balance > 1 and clave < nodo.izq.clave:
            return self.rotacion_derecha(nodo)

        # Caso Right Right
        if balance < -1 and clave > nodo.der.clave:
            return self.rotacion_izquierda(nodo)

        # Caso Left Right
        if balance > 1 and clave > nodo.izq.clave:
            nodo.izq = self.rotacion_izquierda(nodo.izq)
            return self.rotacion_derecha(nodo)

        # Caso Right Left
        if balance < -1 and clave < nodo.der.clave:
            nodo.der = self.rotacion_derecha(nodo.der)
            return self.rotacion_izquierda(nodo)

        return nodo

    def insertar_clave(self, clave):
        self.raiz = self.insertar(self.raiz, clave)

    def recorrido_inorder(self, nodo):
        if not nodo:
            return []
        return self.recorrido_inorder(nodo.izq) + [nodo.clave] + self.recorrido_inorder(nodo.der)


# Ejemplo de uso
if __name__ == "__main__":
    arbol = ArbolAVL()
    datos = [10, 20, 30, 40, 50, 25]

    for dato in datos:
        arbol.insertar_clave(dato)

    print("Recorrido inorder del árbol AVL:", arbol.recorrido_inorder(arbol.raiz))
