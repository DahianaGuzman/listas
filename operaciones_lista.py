# ARCHIVO: operaciones_lista.py
"""
Calcular suma, promedio, máximo y mínimo de una lista numérica.
Versión SIN funciones: toda la lógica está en el bloque principal.
"""
if __name__ == '__main__':
    # Cambia esta lista por la que necesites
    ejemplo = [5, 3, 5]

    # Ajusta la cantidad de decimales del promedio (o pon None para no redondear)
    decimales = 2
    print('Lista:', ejemplo)
    # Convertir a lista por si el origen es un iterable
    l = list(ejemplo)
    if not l:
        raise ValueError('La lista está vacía')
    suma = sum(l)
    if decimales is None:
        promedio = suma / len(l)
    else:
        promedio = round(suma / len(l), decimales)
    maximo = max(l)
    minimo = min(l)
    print('suma =', suma)
    print('promedio =', promedio)
    print('maximo =', maximo)
    print('minimo =', minimo)
