def busqueda_lineal(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice  # Se encontró el elemento

    return -1  # El elemento no está en la lista

# Ejemplo de uso
mi_lista = [15, 7, 23, 4, 11, 29, 18, 6, 25, 8, 13, 20, 3, 9, 27, 14, 5, 12, 21, 1, 10, 19, 28, 16, 2, 24, 17, 26, 22, 30]
objetivo =11

resultado = busqueda_lineal(mi_lista, objetivo)

if resultado != -1:
    print(f"El elemento {objetivo} está en la posición {resultado}.")
else:
    print(f"El elemento {objetivo} no está en la lista.")