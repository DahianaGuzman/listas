# ARCHIVO: buscar_elemento.py
"""
Buscar un valor y devolver las posiciones (índices) en que aparece.
"""
from typing import List, Any


def buscar_elemento(lst: List[Any], valor: Any) -> List[int]:
    posiciones: List[int] = []
    for i, v in enumerate(lst):
        if v == valor:
            posiciones.append(i)
    return posiciones


if __name__ == '__main__':
    ejemplo = [5, 3, 5]
    valor = 5
    print('Lista:', ejemplo)
    print(f'El valor {valor} aparece en las posiciones:', buscar_elemento(ejemplo, valor))

