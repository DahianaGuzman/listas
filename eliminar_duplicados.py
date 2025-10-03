"""
Eliminar duplicados conservando el orden de primera aparición.
"""
if __name__ == '__main__':
    ejemplo = [1, 2, 2, 3, 1]
    print('Entrada:', ejemplo)

    vistos = set()
    resultado = []
    for x in ejemplo:
        if x not in vistos:
            vistos.add(x)
            resultado.append(x)

    print('Salida:', resultado)
