## Sílaba "de" en la primera mitad: Desarrollar un programa en Python que permita cargar por teclado un texto completo. Siempre se supone que el usuario cargará un punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:
## a) Determinar cuántas palabras tenían al menos un caracter que era en realidad un dígito (un caracter entre '0' y '9').
## b) Determinar cuántas palabras tenían 3 o menos letras, cuántas tenían 4 y hasta 6 letras, y cuántas tenían más de 6 letras.
## c) Determinar la longitud de la palabra más larga del t
## d) Determinar cuántas palabras contuvieron la expresión "de", pero en la primera mitad de la palabra



#variables
texto = str();
palabra = str();
palabras_condigito = int();
tiene_4letras = int();
tiene_5letras = int();
tiene_3omenos_letras = int();
tiene_6omas_letras = int();
mitad_palabra = str();
contiene_de = int();

texto = "";
palabra = "";
palabras_condigito = 0;
tiene_4letras = 0;
tiene_5letras = 0;
tiene_3omenos_letras = 0;
tiene_6omas_letras = 0;
mitad_palabra = "";
contiene_de = 0;

#modulos
def cortarString(string, inicio, final):
    return string[inicio : final];

def separarPalabra(string):
    espacio = string.find(" ");
    palabra = string[0:espacio];
    return palabra


def tieneDigito(string):
    es_digito = bool();

    for caracter in string:
        if caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter =="7" or caracter == "8" or caracter == "9":
            es_digito = True;
            break
        else:
            es_digito = False;
    return es_digito
    
def longitudX(string, longitud):
    if len(string) == longitud:
        return True;
    else:
        return False;

def longitudMenorIgualX(string, longitud):
    if len(string) <= longitud:
        return True;
    else:
        return False;

def longitudMayorIgualX(string, longitud):
    if len(string) >= longitud:
        return True;
    else:
        return False;

def mitadString(string):
    return string[0 : round(len(string)/2 + 0.1)];

def contieneDe(string):
    if string.find("de") != -1:
        return True;
    else:
        return False;


#codigo principal
texto = str(input("Ingresar texto, debe terminar con un punto: "));
while len(texto) == 0 or texto[len(texto) - 1] != ".":
    texto = str(input("Error. Volver a ingresar texto: "));

texto = texto + " ";
while (texto.find(" ") != -1):
    palabra = separarPalabra(texto);
    texto = cortarString(texto, len(palabra)+1, len(texto));

    if palabra[len(palabra) - 1] == ".": #La ultima palabra siempre quedaba con un punto, esto sirve para sacarselo.
        palabra = cortarString(palabra, 0 , len(palabra)-1);
        
    if tieneDigito(palabra) == True:
        palabras_condigito += 1;

    if longitudX(palabra, 4) == True:
        tiene_4letras += 1;
    elif longitudX(palabra, 5):
        tiene_5letras += 1;
    elif longitudMenorIgualX(palabra, 3):
        tiene_3omenos_letras += 1;
    elif longitudMayorIgualX(palabra, 6):
        tiene_6omas_letras += 1;

    if contieneDe(mitadString(palabra)) == True:
        contiene_de += 1;


print(f"Palabras que tenian al menos un digito como caracter: {palabras_condigito}");
print(f"Palabras con 3 o menos letras: {tiene_3omenos_letras}");
print(f"Palabras con 4 letras: {tiene_4letras}");
print(f"Palabras con 5 letras: {tiene_5letras}");
print(f"Palabras con 6 o mas letras: {tiene_6omas_letras}");

print(f"""Palabras que contienen la expresion "de" en su primera mitad: {contiene_de}""")

