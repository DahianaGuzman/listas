# ARCHIVO: rotar_lista.py
"""
Rotar una lista n posiciones a la derecha o a la izquierda, sin funciones.
"""

lista_planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

try:
    print("¿Hacia que dirección deseas rotar los elementos?\n\n MENÚ: \n 1.Derecha \n 2.Izquierda")
    direccion=int(input("Ingrese el número del menu: "))

    print("¿Cuantas posiciones deseas rotar los elementos?")
    posiciones=int(input("Ingrese el número de posiciones: "))

    print(f"Lista original: {lista_planetas}")

    if direccion == 1:
      planetas_rotados=lista_planetas[-posiciones:]#segun posición se quitan x elementos del final de la lista (lista [-n:])
      planetas_rotados+= lista_planetas[:-posiciones]#segun posición se añaden x elementos al inicio de la lista (lista [:-n])
      print(f"Lista rotada {posiciones} posiciones a la derecha: {planetas_rotados}")
    elif direccion == 2:
      planetas_rotados=lista_planetas[posiciones:]#segun posición se quitan x elementos del inicio de la lista (lista [:n])
      planetas_rotados+=lista_planetas[:posiciones]#segun posición se añaden x elementos al final de la lista  (lista [n:])
      print(f"Lista rotada {posiciones} posiciones a la izquierda: {planetas_rotados}")
    else:
        print("Dirección no válida. Por favor, ingresa 1 para derecha o 2 para izquierda.")

except ValueError:
    print("Entrada no válida. Por favor, ingresa números enteros para la dirección y las posiciones.")
