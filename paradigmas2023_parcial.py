"""
Crear un programa de torneo de futbol todos contra todos 10 equipos. Se debe ingresar numero de equipo y 
resultado deel partido. 
Luego, dar la siguiente informacion
1- tabla con numero de equipo y puntaje
2- equipos con menor puntaje
3- promedio de algo
4- menu
"""

def ingreso_de_datos (lista_equipos, dict_equipos):
    for equipo in lista_equipos:
        resultados = []
        n_equipo = equipos.index(equipo) + 1

        for rival in lista_equipos:
            if  equipo != rival:
                result = input(f"resultado de {equipo} vs {rival}: ")
                resultados.append(result)
        dict_equipos[n_equipo] = resultados

def valor_resultado(resultado):
    resultado = resultado.lower()
    if resultado == "g":
        return 3
    elif resultado == "e":
        return 1
    else:
        return 0

def puntajes(dict_equipos):
    equipos_puntos = dict()
    for n_equipo, resultados in dict_equipos.items():
        lista_puntos = []

        for resultado in resultados:
            puntos = valor_resultado(resultado)
            lista_puntos.append(puntos)
        equipos_puntos[n_equipo] = sum(lista_puntos)

    return equipos_puntos

def tabla(dict_equipos):
    tabla = ""
    for equipo, puntaje in dict_equipos.items():
        tabla += f"Equipo {equipo}: {puntaje} puntos\n" 
    return tabla

def menores_puntajes (dict_equipos):
    menores = []
    bandera = True

    for equipo, puntaje in dict_equipos.items():
        
        if bandera:
            menor_puntaje = puntaje
            bandera = False
        if puntaje == menor_puntaje:
            menores.append(equipo)
        elif puntaje < menor_puntaje:
            menor_puntaje = puntaje
            menores = [equipo]
    
    return menores

        
def menu(opcion, dict_equipos):
    equipos_con_puntajes = puntajes(dict_equipos)
    if opcion == 1:
        print(tabla(equipos_con_puntajes))

    elif opcion == 2:
        lista_menores = menores_puntajes(equipos_con_puntajes)
        if len(lista_menores) == 1:
            print(f"El equipo con el menor puntaje es el Equipo {lista_menores[0]}")
        else:
            print(f"Los equipo con el menor puntaje son:", end="")
            for equipo in lista_menores:
                print(f"Equipo {equipo},", end="")
            print("")

    elif opcion ==3:
        pass

        


equipos = ["arg", "brasil", "uru", "chile"]#, "par", "bol", "col", "ven", "mexico", "usa"]
equipos_resultados = dict()

ingreso_de_datos(equipos, equipos_resultados)
print(equipos_resultados)

opc_menu = -1
while opc_menu != 4:
    print("******* MENU *******\n1- tabla de puntos\n2- equipos con menor puntaje\n3- promedio de algo\n4-Salir")
    opc_menu = int(input("Que opcion elige? "))
    menu(opc_menu, equipos_resultados)


"""equipos_con_puntajes = puntajes(equipos_resultados )
print( tabla(equipos_con_puntajes) ) 

print(f"Los equipos con el menor puntaje son {menores_puntajes(equipos_con_puntajes)}")   
"""