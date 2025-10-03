# ARCHIVO: rotar_lista.py
"""
Rotar una lista n posiciones a la derecha o a la izquierda, sin funciones.
"""

if __name__ == '__main__':
    ejemplo = [1, 2, 3, 4, 5, 6]
    print('Lista original:', ejemplo)

    n = 2
    direccion = 'derecha'

    longitud = len(ejemplo)
    n = n % longitud  # asegurar que n sea válido

    if direccion.lower() in ('derecha', 'right'):
        rotada = ejemplo[-n:] + ejemplo[:-n]
    elif direccion.lower() in ('izquierda', 'left'):
        rotada = ejemplo[n:] + ejemplo[:n]
    else:
        raise ValueError("La dirección debe ser 'derecha'/'izquierda' o 'right'/'left'")

    print(f"Rotar {n} posiciones a la {direccion}:", rotada)

    # Otro ejemplo: rotar 8 posiciones a la derecha
    n = 8 % longitud
    rotada = ejemplo[-n:] + ejemplo[:-n]
    print("Rotar 8 posiciones a la derecha:", rotada)
