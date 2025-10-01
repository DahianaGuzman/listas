# ARCHIVO: operaciones_lista.py
"""
Calcular suma, promedio, máximo y mínimo de una lista numérica.
"""
from typing import Iterable


def suma_lista(lst: Iterable[float]) -> float:
    return sum(lst)


def promedio_lista(lst: Iterable[float], decimales: int | None = 2) -> float:
    l = list(lst)
    if not l:
        raise ValueError('La lista está vacía')
    prom = sum(l) / len(l)
    if decimales is None:
        return prom
    return round(prom, decimales)


def maximo_lista(lst: Iterable[float]) -> float:
    l = list(lst)
    if not l:
        raise ValueError('La lista está vacía')
    return max(l)


def minimo_lista(lst: Iterable[float]) -> float:
    l = list(lst)
    if not l:
        raise ValueError('La lista está vacía')
    return min(l)


if __name__ == '__main__':
    ejemplo = [5, 3, 5]
    print('Lista:', ejemplo)
    print('suma =', suma_lista(ejemplo))
    print('promedio =', promedio_lista(ejemplo))
    print('maximo =', maximo_lista(ejemplo))
    print('minimo =', minimo_lista(ejemplo))
