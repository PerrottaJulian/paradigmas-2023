## Análisis de texto: Se solicita crear un programa que permita ingresar un texto, las palabras se encontrarán separadas únicamente por espacios en blanco y el mismo debe finalizar con un punto. En base a ese texto determinar:
## a) La cantidad de palabras que comienzan y terminan en vocal
## b) La cantidad de palabras que comienzan con la misma letra que terminó la palabra anterior
## c) El porcentaje que representa el punto a) sobre el total de palabras del texto.


#variables 
texto = str();
espacio = int();
palabra = str();
empiezaytermina_vocal = int();
ultima_letra_anterior = str();
empieza_como_termina = int();
total_palabras = int();

texto = " ";
espacio = 0;
palabra = " ";
empiezaytermina_vocal = 0;
ultima_letra_anterior = " ";
empieza_como_termina = 0;
total_palabras = 0;

#desarrollo
print("Debera ingresar un texto, cuyas palabras solo pueden estar separas por espacion en blanco y debe finalizar con un punto");
texto = str(input("Texto: "));

while (texto[len(texto) - 1] != "."):
    print("El texto debe terminar con un punto");
    texto = str(input("Pruebe devuelta: "));


for i in range (len(texto)):
    espacio = texto.find(" ");
    
    palabra = texto[0 : espacio];
    total_palabras += 1;

    texto = texto[espacio+1 : texto.find(".")+1];

    if (palabra[0] == "a" or palabra[0] == "e" or palabra[0] == "i" or palabra[0] == "o" or palabra[0] == "u"):
        if (palabra[len(palabra)-1] == "a" or palabra[len(palabra)-1] == "e" or palabra[len(palabra)-1] == "i" or palabra[len(palabra)-1] == "o" or palabra[len(palabra)-1] == "u"):
            empiezaytermina_vocal += 1;
    

    if (palabra[0] == ultima_letra_anterior):
        empieza_como_termina += 1;

    ultima_letra_anterior = palabra[len(palabra)-1];

    if (espacio == -1):
        break;


print("Palabras que terminan y empiezan en vocal:", empiezaytermina_vocal);
print("Palabras que comienzan con la misma letra que terminó la palabra anterior:", empieza_como_termina);
print("Porcentaje que representan las palabras que empiezan y terminan en vocal sobre el total de palabras: %", empiezaytermina_vocal*100/total_palabras)






