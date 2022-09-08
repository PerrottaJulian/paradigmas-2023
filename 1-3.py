#Escriba un programa que transforme todas las letras de una palabra en mayúsculas, minúsculas y la primera con minúsculas(capitalización).

#Variables
palab = str();

palab = "";

#Desarrollo
print("Ingresar una palabara, se le devolvera escrita con todo mayusculas, todo minusculas, y con solo la incicial mayuscula: ")
palab = str(input());

print(palab.upper(), palab.lower(), palab[0].upper() + palab[1:100].lower());