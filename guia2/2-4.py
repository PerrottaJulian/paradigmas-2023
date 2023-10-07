## Decimal a Hexadecimal: Generar n números aleatorios entre el rango de 5000 y 450000, por cada uno de ellos mostrar y generar el numero hexadecimal.


#carpetas
from random import randint

#variables
n = int();
num_random = int();
cociente = int();
resto = int();
num_hexa = str();

n = 0;
num_random = 0;
cociente = 0;
resto = 0;
num_hexa = "";

#desarrollo
print("Debera ingresar la cantidad de numeros aleatorios que quiere que el programa genere, los mismos estaran entre 5000 y 450000. Luego se dara el equivalente en sistema hexadecimal");
n = int(input("cuantos numeros aleatorios desea generar?: "));

for i in range (n):
    num_random = randint(5000, 450000);
    print("numero decimal", i+1, ":", num_random);
    resto = num_random % 16;
    cociente = num_random // 16;
    
    if (resto == 10):
        resto = "A";
    elif (resto == 11):
        resto = "B";
    elif (resto == 12):
        resto = "C";
    elif (resto == 13):
        resto = "D";
    elif (resto == 14):
        resto = "E";
    elif (resto == 15):
        resto = "F";

    num_hexa = str(resto)
    
    while (cociente > 16):
        resto = cociente % 16;
        cociente = cociente // 16;
        
        if (resto == 10):
            resto = "A";
        elif (resto == 11):
            resto = "B";
        elif (resto == 12):
            resto = "C";
        elif (resto == 13):
            resto = "D";
        elif (resto == 14):
            resto = "E";
        elif (resto == 15):
            resto = "F";

        num_hexa = str(resto) + num_hexa
        
    if (cociente < 16):
        num_hexa = str(cociente) + num_hexa

    print("Numero hexadecimal:", num_hexa)


