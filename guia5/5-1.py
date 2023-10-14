## Sílaba "de" en la primera mitad: Desarrollar un programa en Python que permita cargar por teclado un texto completo. Siempre se supone que el usuario cargará un punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:
## a) Determinar cuántas palabras tenían al menos un caracter que era en realidad un dígito (un caracter entre '0' y '9').
## b) Determinar cuántas palabras tenían 3 o menos letras, cuántas tenían 4 y hasta 6 letras, y cuántas tenían más de 6 letras.
## c) Determinar la longitud de la palabra más larga del t
## d) Determinar cuántas palabras contuvieron la expresión "de", pero en la primera mitad de la palabra
# 2023

#variables
texto = str();
texto = "";
#modulos
def tieneDigito(string): #a)
    for caracter in string:
        if caracter.isdigit():
            return 1
        else:
            continue
    return 0

def lenMenorIgual3(string):#b)
    if len(string) <= 3:
        return 1
    else:
        return 0
def lenEntre4y6(string):
    if len(string) >= 4 and len(string) <= 6:
       return 1
    else:
        return 0   
def lenMayor6(string):
    if len(string) > 6:
        return 1
    else:
        return 0  


def contieneDe(string): #d)
    if string.find("de") != -1:
        return 1;
    else:
        return 0;
def mitadString(string):
    return string[0 : round(len(string)/2 + 0.1)]


def encontrarMayor(mayor_actual,nuevo):#c)
    if nuevo > mayor_actual:
        return nuevo
    else:
        return mayor_actual

def principal(texto):
    len_mayor = -1
    palabras_con_digito = 0
    palabras_3omenos= 0
    palabras_entre4y6 = 0
    palabras_masde6 = 0
    palabras_primeramitad_contienen_de = 0;

    palabras = texto.split(" ")

    for palabra in palabras:
        palabras_con_digito += tieneDigito(palabra)#a

        palabras_3omenos += lenMenorIgual3(palabra)#b
        palabras_entre4y6 += lenEntre4y6(palabra)
        palabras_masde6 += lenMayor6(palabra)

        len_mayor = encontrarMayor(len_mayor, len(palabra))#c

        palabras_primeramitad_contienen_de += contieneDe(mitadString(palabra))#d


    print(f"Palabras que tenian al menos un digito como caracter: {palabras_con_digito}");

    print(f"Palabras con 3 o menos letras: {palabras_3omenos}");
    print(f"Palabras con entre 4 y 6 letras: {palabras_entre4y6}");
    print(f"Palabras con mas de 6 letras: {palabras_masde6}")

    print(f"La longitud de la palabra mas larga es: {len_mayor} letras")

    print(f"Palabras que contienen la expresion 'de' en su primera mitad: {palabras_primeramitad_contienen_de}")

#codigo principal
mitexto = str(input("Ingresar texto, debe terminar con un punto: "));
while len(mitexto) == 0 or mitexto[len(mitexto) - 1] != ".":
    mitexto = str(input("Error. Volver a ingresar texto: "));
mitexto = mitexto[:len(mitexto)-1]

principal(mitexto)
