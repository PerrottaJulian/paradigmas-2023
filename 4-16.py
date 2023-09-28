"""
Vamos a crear un programa que tenga el siguiente menú:
1.	Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
2.	Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
3.	Longitud de la lista: te muestra el número de elementos de la lista.
4.	Eliminar el último número: Muestra el último número de la lista y lo borra.
5.	Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
6.	Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
7.	Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
8.	Mostrar números: Muestra los números de la lista
9.	Salir
"""
import time

opcion_menu = 0
lista = []

while opcion_menu != 9:
    opcion_menu = 0
    print(
"""  *************************** MENU ***************************
1.	Añadir número a la lista
2.	Añadir número a la lista en una posición
3.	Longitud de la lista
4.	Eliminar el último número
5.	Eliminar un número
6.	Contar número
7.	Posiciones de un número
8.	Mostrar números
9.	Salir
""")
    while opcion_menu < 1 or opcion_menu> 9:
        try:
            opcion_menu = int(input("Que quiere hacer?: "))
        except:
            continue
    
    #proceso de cada opcion
    if opcion_menu == 1:
        try:
            agregar_n = float(input("Que numero quiere agregar a la lista?: "))
            lista.append(agregar_n)
        except:
            print("No se puedo agregar el numero")
            continue

    elif opcion_menu == 2:
        try:
            agregar_n_en = float(input("Que numero quiere agregar a la lista?: "))
            posicion = int(input("En que posicion?: "))
            lista.insert(posicion, agregar_n_en)
        except:
            print("No se puedo agregar el numero")
            continue

    elif opcion_menu == 3:
        print(f"La longitud de la lista es de: {len(lista)} numeros")

    elif opcion_menu == 4:
        continuar = ""
        print(f"Se eliminara el numero {lista[-1]}, que se encuentra en la ultima posicion de la lista.")

        while continuar != "y" and continuar != "n":
            continuar = str(input("Continuar? (y/n) ")).lower()
        if continuar == "y":
            lista.pop()
            print("Se elimino el numero")
    


    elif opcion_menu == 5:
        try:
            posicion = int(input("En que posicion quiere eliminar un numero : "))
            lista.pop(posicion)
        except:
            print("No se puedo eliminar el numero")
            continue

    elif opcion_menu == 6:
        contar_n = float(input("Que numero quiere contar sus apariciones en la lista?: "))
        print(lista.count(contar_n))
        
    elif opcion_menu == 7:
        pass


    elif opcion_menu == 8:
        print(f"Numeros: ", end="")
        for n in lista:
            print(n, end=", ")
        print("\n")
    time.sleep(1.5)



