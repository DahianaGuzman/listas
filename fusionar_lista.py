"""
Intercalar elementos de dos listas de igual longitud.
"""
from typing import List, Any


def fusionar_intercalar(a: List[Any], b: List[Any]) -> List[Any]:

    if len(a) != len(b):
        raise ValueError('Las listas deben tener la misma longitud')
    
    resultado: List[Any] = []
    # zip() agrupa los elementos de las listas en tuplas (a[i], b[i])
    for x, y in zip(a, b):
        resultado.append(x)
        resultado.append(y)
    return resultado


if __name__ == '__main__':
    a = [1, 3, 5]
    b = [2, 4, 6]
    print('Lista A:', a)
    print('Lista B:', b)
    print('Listas fusionadas:', fusionar_intercalar(a, b))

    c = ['a', 'c', 'e']
    d = ['b', 'd', 'f']
    print('\nLista C:', c)
    print('Lista D:', d)
    print('Listas fusionadas:', fusionar_intercalar(c, d))
