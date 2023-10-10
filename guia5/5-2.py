<<<<<<< Updated upstream:guia5/5-2.py
## Sólo menores que 7. Desarrollar un programa de Phyton que permita cargar por teclado un secuencia de números, uno por uno. Siempre se supone que el usuario cargará un 0(cero) para indicar el final del proceso de carga. El cero no debe considerarse un dato a procesar. El programa debe:
## a) Determinar el porcentaje que cantidad de números pares representa en la cantidad total de números ingresados.
## b) Determinar cuántos de los números ingresados tenían su último dígito igual a 4 o igual a 5.
## c) Determinar el menor de los números ingresados que sean divisibles por 3.
## d) Determinar si la secuencia estaba formada sólo por números.


#variables
c_numeros = int();
c_pares = int();
iguales_4 = int();
iguales_5 = int();
menor_divisiblepor3 = int();


c_numeros = 0;
c_pares = 0;
iguales_4 = 0;
iguales_5 = 0;
menor_divisiblepor3 = 999999;

#modulos
def esPar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def porcentaje (parte, total):
    return parte*100/total

def ultimoDigito(numero):
    numero = str(numero);
    ultimo_digito = numero[len(numero)-1];
    ultimo_digito = int(ultimo_digito);
    return ultimo_digito

def IgualA(numero, numero_buscado):
    if (numero == numero_buscado):
        return True;
    else:
        return False;

def divisiblePor(numero, divisor):
    if numero % divisor == 0:
        return True;
    else:
        return False;

#codigo principal
print("Debera ingresar una serie de numeros, para terminar la carga ingresar 0.")
n = int(input("Ingrese un numero: "));

while n != 0:
    c_numeros += 1;

    if esPar(n) == True:
        c_pares += 1;

    if IgualA(ultimoDigito(n), 4) == True:
        iguales_4 += 1;
    
    if IgualA(ultimoDigito(n), 5) == True:
        iguales_5 += 1;
    
    if divisiblePor(n, 3) == True:
        if n < menor_divisiblepor3:
            menor_divisiblepor3 = n;


    n = int(input("Ingrese un numero: "));



print("Porcentaje de numeros pares:", porcentaje(c_pares, c_numeros), "%");

print("Numero con ultimo digito igual a 4:", iguales_4);
print("Numero con ultimo digito igual a 5:", iguales_5);

print("El menor de los numeros divisibles por 3 es:", menor_divisiblepor3);

=======
"""
Sólo menores que 7. Desarrollar un programa de Phyton que permita cargar por teclado un secuencia de números, uno por uno.
Siempre se supone que el usuario cargará un 0(cero) para indicar el final del proceso de carga. El cero no debe considerarse un dato a procesar. El programa debe:
a) Determinar el porcentaje que cantidad de números pares representa en la cantidad total de números ingresados.
b) Determinar cuántos de los números ingresados tenían su último dígito igual a 4 o igual a 5.
c) Determinar el menor de los números ingresados que sean divisibles por 3.
d) Determinar si la secuencia estaba formada sólo por números.
"""

#modulos
def esPar(numero):
    if numero % 2 == 0:
        return 1
    else:
        return 0

def porcentaje (parte, total):
    return parte*100/total

def ultimoDigito(numero):
    numero = str(numero)
    ultimo_digito = numero[len(numero)-1]
    ultimo_digito = int(ultimo_digito)
    return ultimo_digito
    

def IgualA(numero, numero_buscado):
    if (numero == numero_buscado):
        return 1
    else:
        return 0

def divisiblePor(numero, divisor):
    if numero % divisor == 0:
        return True
    else:
        return False

def encontrarMenor(menor_actual, nuevo):
    if nuevo < menor_actual:
        return nuevo
    else:
        return menor_actual
    

def principal(lista_numeros):
    bandera = True
    c_pares = 0
    iguales_4 = 0
    iguales_5 = 0
    menor_divisiblepor3 = 999999
    solo_numeros = True

    for n in lista_numeros:
        c_pares += esPar(n)
        iguales_4 += IgualA(ultimoDigito(n),4)
        iguales_5 += IgualA(ultimoDigito(n),5)

        if bandera:
            menor_divisiblepor3 = bandera = False
        elif divisiblePor(n, 3):
            menor_divisiblepor3 = encontrarMenor(menor_divisiblepor3, n)
            
        if str(n).isdigit() is False:
            solo_numeros = False

    print(f"El porcentaje de numeros pares es: {porcentaje(c_pares, len(lista_numeros))}")
    print(f"Numeros con el ultimo digito igual a 4: {iguales_4}")
    print(f"Numeros con el ultimo digito igual a 5: {iguales_5}")

    print("Solo nuemros:",solo_numeros)
    if solo_numeros:
        print("La secuencia estaba formada solo por numeros")
    else:
        print("La secuencia NO estaba formada solo por numeros")
        

#codigo principal
print("Debera ingresar una serie de numeros, para terminar la carga ingresar 0.")
numeros = []

n=""
while n != "0":
  n = input("Ingrese un numero: ")
  if n != "0":
    numeros.append(n)
       

principal(numeros)
>>>>>>> Stashed changes:5-2.py
