## Solamente 'a' Desarrollar un programa que permita ingresar por teclado, con palabras separadas por un espacio y terminado en punto. En base al texto ingresado, determinar: 
## a) Cuál es la longitud de la palabra más larga. 
## b) Cuántas palabras tienen la a como única vocal 
## c) Qué porcentaje representan las que sólo tienen la vocal a sobre el total de palabras. 
## Ejemplo: "el agua clara salta por las piedras." La longitud de la palabra más larga es 7 letras. Las palabras cuya única vocal es la a son: 3 El porcentaje de estas palabras sobre el total es 43 %


#variables
texto = str();
palabra = str();
palabra_maslarga = str();
a_unicavocal = int();
total_palabras = int();

bandera = bool;


texto = "";
palabra = "";
palabra_maslarga = "";
a_unicavocal = 0;
total_palabras = 0;

bandera = True;

#modulos
def cortarString(string, inicio, final):
    return string[inicio:final];

def separarPalabra(string):
    espacio = string.find(" ");
    palabra = string[0:espacio];
    return palabra


def tieneA(palabra): #b
    for letra in palabra:
        if letra == "a":
            tiene_a = True;
            break   
        else:
            tiene_a = False;
    return tiene_a;

def tieneVocal(palabra):
    for letra in palabra:
        if letra == "e" or letra == "i" or letra == "o" or letra == "u":
            tiene_vocal = True;
            break
        else:
            tiene_vocal = False;
    return tiene_vocal;

def aUnicaVocal(palabra):
    if tieneA(palabra) == True:
        if tieneVocal(palabra) == False:
            return True;
        else:
            return False;
    else:
        return False;


def porcentaje (parte, total):
    return parte*100/total

#codigo principal
texto = str(input("texto: "));
while len(texto) == 0 or texto[len(texto) - 1] != ".":
    texto = str(input("Error. Volver a ingresar texto: "));


texto = texto + " ";
while (texto.find(" ") != -1):
    palabra = separarPalabra(texto);

    total_palabras += 1;
    texto = cortarString(texto, len(palabra)+1, len(texto));
    
    if bandera == True: #a
        palabra_maslarga = palabra;
        bandera = False;
    
    if len(palabra) > len(palabra_maslarga):
        palabra_maslarga = palabra;


    if aUnicaVocal(palabra) == True: #b
        a_unicavocal += 1;





if palabra_maslarga[len(palabra_maslarga) - 1] == ".":
    print("La logitud de la palabra mas larga es:", len(palabra_maslarga)-1 , "(", palabra_maslarga, ")"); #-1 porque la ultima palabra queda con un "." al final y le suma 1 a la longitud
else:
    print("La logitud de la palabra mas larga es:", len(palabra_maslarga), "(", palabra_maslarga, ")");

print("""Palabras con la "a" como unica vocal:""", a_unicavocal);

print("Porcentanje de dichas palabras sobre el total de palabras: %", porcentaje(a_unicavocal, total_palabras) ); #c
