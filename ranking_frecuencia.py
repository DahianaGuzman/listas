# ARCHIVO: ranking_frecuencias.py
"""
Versión simple: contar cuántas veces aparece cada palabra
y mostrar el ranking sin usar funciones.
"""

partitura=["Do","Re","Mi","Do","Fa","Re","Sol","Si","Re","La","Si","Sol","Si"]
lista_aux=[]
#lista_final=[]

print(f"Las notas de la canción son: \n")

try:
    for i in partitura:
        if i not in lista_aux:#agrega solo los que no estan duplicados
            lista_aux.append(i)
            print(f"{i}, esta {partitura.count(i)} veces")
            #lista_final.append(a)

    #lista_final.sort()#ordena
    #print(f"Tu lista final sin repeticiones es: {lista_final}")
except Exception as e:
    print(f"Ocurrió un error al procesar la partitura: {e}")
