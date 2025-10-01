"""
Rotar una lista n posiciones a la derecha o a la izquierda.
"""
from typing import List, Any


def rotar_lista(lst: List[Any], n: int, direccion: str = 'derecha') -> List[Any]:

    if not lst:
        return []
    
    longitud = len(lst)
    # El operador módulo asegura que n sea efectivo para cualquier entero
    n = n % longitud
    
    # Si n es 0, la lista no cambia, devolvemos una copia
    if n == 0:
        return lst[:]

    dir_lower = direccion.lower()
    if dir_lower in ('derecha', 'right'):
        # Combina el final de la lista con el principio
        return lst[-n:] + lst[:-n]
    elif dir_lower in ('izquierda', 'left'):
        # Combina el principio de la lista con el final
        return lst[n:] + lst[:n]
    else:
        raise ValueError("La dirección debe ser 'derecha'/'izquierda' o 'right'/'left'")


if __name__ == '__main__':
    ejemplo = [1, 2, 3, 4, 5, 6]
    print('Lista original:', ejemplo)
    print("Rotar 2 posiciones a la derecha:", rotar_lista(ejemplo, 2, 'derecha'))
    print("Rotar 2 posiciones a la izquierda:", rotar_lista(ejemplo, 2, 'izquierda'))
    # Rotar 8 a la derecha es igual que rotar 2 (8 % 6 = 2)
    print("Rotar 8 posiciones a la derecha:", rotar_lista(ejemplo, 8, 'derecha'))