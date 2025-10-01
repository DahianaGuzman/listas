from typing import List, Tuple


def ranking_frecuencias(palabras: List[str]) -> List[Tuple[str, int]]:
    
    
    pares: List[Tuple[str, int]] = []
    
    for p in palabras:
        encontrado = False
        for i, (pal, cnt) in enumerate(pares):
            if pal == p:
                
                pares[i] = (pal, cnt + 1)
                encontrado = True
                break
       
        if not encontrado:
            pares.append((p, 1))
            
    pares.sort(key=lambda x: x[1], reverse=True)
    
    return pares


if __name__ == '__main__':
    ejemplo = ['manzana', 'pera', 'manzana', 'naranja', 'pera', 'manzana']
    print('Lista de palabras:', ejemplo)
    print('Ranking de frecuencias:', ranking_frecuencias(ejemplo))
