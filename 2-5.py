## Analisis de Texto. El usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero. La frase finaliza con un punto, y las palabras están separadas por espacios únicamente. Se debe mostrar:
## a) Ver el porcentaje de vocales respecto del total de letras de la frase.
## b) La longitud promedio de las palabras.
## c) La longitud de la palabra mas larga del texto.
## d) Cantidad de palabras que comienzan con "ta".


#variables
frase = str();
acumulador_vocales = int();
porc_vocales = float();
espacio = int();
palabra = str();
suma_longitudes = int();
prom_longitudes = float();
palabra_mas_larga = int();
empiezan_con_ta = int();


frase = "";
acumulador_vocales = 0;
porc_vocales = 0.0;
espacio = 0;
palabra = "";
suma_longitudes = 0;
prom_longitudes = 0.0;
palabra_mas_larga = 0;
empiezan_con_ta = 0;

#desarrollo
frase = str(input("Ingrese una frase. La frase debe finalizar con un punto. Tambien, no puede tener longitud 0: "));

while (len(frase) == 0 or frase[len(frase)-1] != "." ):
    
    if (len(frase) == 0 ):
        frase = str(input("La frase tiene longitud 0. Pruebe devuelta: "));
    elif (frase[len(frase)-1] != "." ):
        frase = str(input("La frase no termina con un punto. Pruebe devuelta: "));

frase = frase.lower();
for i in range (len(frase)):
    if (frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u"):
        acumulador_vocales += 1;
    
porc_vocales = acumulador_vocales * len(frase) / 100;

print("Porcentaje de vocales: %", porc_vocales*10);

for i2 in range (len(frase)):

    espacio = frase.find(" ");
    palabra = frase[0 : espacio];

    suma_longitudes += len(palabra);
    frase = frase[espacio+1 : frase.find(".")+1];

    if (len(palabra) > palabra_mas_larga):
        palabra_mas_larga = len(palabra);


    if (palabra[0:2] == "ta"):
        empiezan_con_ta += 1


    if (espacio == -1):
        break;

prom_longitudes = suma_longitudes / (i2+1);
print("El longitud promedio de las palabras es:", prom_longitudes);

print ("La longitud de la palabra mas larga es:", palabra_mas_larga, "letras");

print("""palabras que empiezan con "ta":""", empiezan_con_ta);