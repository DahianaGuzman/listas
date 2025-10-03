# ARCHIVO: fusionar_listas.py
"""
Intercalar elementos de dos listas de igual longitud, sin usar funciones.
"""

if __name__ == '__main__':
    lista1 = [1, 3, 5, 7]
    lista2 = [2, 4, 6, 8]

    print("Lista 1:", lista1)
    print("Lista 2:", lista2)

    resultado = []
    for i in range(len(lista1)):
        resultado.append(lista1[i])
        resultado.append(lista2[i])

    print("Lista intercalada:", resultado)
