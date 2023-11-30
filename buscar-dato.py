def busqueda_lineal(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice  

    return -1  

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return medio  
        elif valor_medio < objetivo:
            inicio = medio + 1  
        else:
            fin = medio - 1  

    return -1  



# Ejemplo de uso
mi_lista = [15, 7, 23, 4, 11, 29, 18, 6, 25, 8, 13, 20, 3, 9, 27, 14, 5, 12, 21, 1, 10, 19, 28, 16, 2, 24, 17, 26, 22, 30]
objetivo =27

resultado = busqueda_lineal(mi_lista, objetivo)

if resultado != -1:
    print(f"El elemento {objetivo} está en la posición(Por busqueda lineal) {resultado}.")
else:
    print(f"El elemento {objetivo} no está en la lista.")
    
resultado = busqueda_binaria(mi_lista, objetivo)
    
if resultado != -1:
    print(f"El elemento {objetivo} está en la posición (Por busqueda binaria) {resultado}.")
else:
    print(f"El elemento {objetivo} no está en la lista.")