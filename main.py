from arbol.arbol_binario_busqueda import ArbolBinarioBusqueda

if __name__ == "__main__":
    abb = ArbolBinarioBusqueda()
    abb.insertar(10)
    abb.insertar(5)
    abb.insertar(15)
    print("Inorden:", abb.recorrido_inorden())
    print("Buscar 15:", abb.buscar(15))
    abb.eliminar(10)
    print("Inorden después de eliminar 10:", abb.recorrido_inorden())
    print("Altura del árbol:", abb.calcular_altura())
