lista=[]
try:
    
    print("Crear Lista \n\n\nPara salir escriba 'FIN'")
    
    while True:
        numero=input("Ingrese números a la lista: ")
        
        #if numero=='FIN' or numero=='Fin' or numero=='fin':
        if numero.lower() == 'fin': #uso método .lower() para optimizar.
            print(f"Tu lista es: {lista}")
            break
        else:
            lista.append(float(numero)) #añadir nuevo número a la lista
        
except ValueError:

        print("Entrada no válida. Por favor, introduce un número o 'fin'.")
        #Si la entrada no es un número o dato valido
