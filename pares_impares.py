from typing import List, Tuple


def separar_pares_impares(lst: List[int]) -> Tuple[List[int], List[int]]:

    pares: List[int] = []
    impares: List[int] = []
    for x in lst:
        if not isinstance(x, int):
            raise TypeError('Todos los elementos deben ser enteros')
        if x % 2 == 0:
            pares.append(x)
        else:
            impares.append(x)
    return pares, impares


if __name__ == '__main__':
    ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares, impares = separar_pares_impares(ejemplo)
    print('Lista original:', ejemplo)
    print('Pares:', pares)
    print('Impares:', impares)
