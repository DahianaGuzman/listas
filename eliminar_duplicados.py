# ARCHIVO: eliminar_duplicados.py
"""
Eliminar duplicados conservando el orden de primera aparición.
"""
from typing import List, TypeVar
T = TypeVar('T')


def eliminar_duplicados(lst: List[T]) -> List[T]:
    vistos = set()
    resultado: List[T] = []
    for x in lst:
        if x not in vistos:
            vistos.add(x)
            resultado.append(x)
    return resultado


if __name__ == '__main__':
    ejemplo = [1, 2, 2, 3, 1]
    print('Entrada:', ejemplo)
    print('Salida:', eliminar_duplicados(ejemplo))
    