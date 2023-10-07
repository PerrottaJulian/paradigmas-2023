#Escribir un programa que pregunte un nombre de usuario, y que después muestre por pantalla si su cantidad de letras es par o impar.

#variables
nom = str();

nom = "";
#desarrollo
nom = str(input("Ingresar nombre de usuario: "));
if (len(nom) % 2 == 0):
    print("La cantidad de letras del nombre es par (", len(nom), ")");
else:
    print("La cantidad de letras del nombre es impar (", len(nom), ")");
