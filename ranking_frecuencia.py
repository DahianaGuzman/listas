# ARCHIVO: ranking_frecuencias.py
"""
Versión simple: contar cuántas veces aparece cada palabra
y mostrar el ranking sin usar funciones.
"""

if __name__ == '__main__':
    ejemplo = ['manzana', 'pera', 'manzana', 'naranja', 'pera', 'manzana']
    print('Lista de palabras:', ejemplo)

    # Creamos un diccionario vacío
    conteo = {}

    # Contamos las palabras
    for palabra in ejemplo:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    # Convertimos a lista de tuplas (palabra, frecuencia)
    pares = list(conteo.items())

    # Ordenamos por frecuencia de mayor a menor
    pares.sort(key=lambda x: x[1], reverse=True)

    print('Ranking de frecuencias:', pares)
