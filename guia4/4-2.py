## Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

#variables
cadenas_lista = [];
cadenas_inversa = [];

cadena = str();
cadena = "";


#desarrollo
print("Debera ingresar 5 cadenas de caracteres");

for i in range(5):
    cadena = str(input("Escribir cadena de caracteres: "));
    cadenas_lista.append(cadena);

for i2 in range (5, 0, -1):
    cadenas_inversa.append(cadenas_lista[i2-1]);

print(cadenas_inversa);



