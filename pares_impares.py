# ARCHIVO: separar_pares_impares.py
"""
Separar números pares e impares de una lista sin usar funciones.
"""

if __name__ == '__main__':
    ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    pares = []
    impares = []

    for x in ejemplo:
        if not isinstance(x, int):
            raise TypeError('Todos los elementos deben ser enteros')
        if x % 2 == 0:
            pares.append(x)
        else:
            impares.append(x)

    print('Lista original:', ejemplo)
    print('Pares:', pares)
    print('Impares:', impares)
