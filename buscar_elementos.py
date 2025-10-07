# ARCHIVO: buscar_elemento.py
"""
Buscar un valor y devolver las posiciones (índices) en que aparece.
"""
lista_b=[1,2,1,5,12,32,34,4,9,1,7,4,1,7,3,12,11,2,32,3,6,8,8,9]
posicion=[]

try:
    buscar= int(input("Ingrese el número que desea buscar: "))

    for i in range (len(lista_b)): #elemento por elemto hasta ==longitud de lista
      if lista_b[i] == buscar: #busque en lista_b el elemento que se encuentra en el índice i
        posicion.append(i+1) #no establezca la posición 0

    if posicion:
        print(f"El número que buscas esta en las posiciones:{posicion} ")
    else:
        print(f"El número {buscar} no se encuentra en la lista.")

except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")
except Exception as e:
    print(f"Ocurrió un error al buscar el elemento: {e}")