#Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual.

#carpetas
import time

#variables
valdol = float();
res = int();
dolares = float();
pesos = float();

valdol = 0.0;
res = 0;
dolares = 0.0;
pesos = 0.0;

#desarrollo
valdol = float(input("Ingresar el valor actual del dolar: "));
opc = int(input("Si desea convertir de dolares a pesos ingrese 1. Si desea convertir de pesos a dolares ingrese 2: "));

while (opc < 1 or opc > 2):
    print("Error, debe ingresar 1 o 2.");
    opc = int(input("Intente devuelta: "));

if (opc == 1):
    time.sleep(1.2);
    dolares = float(input("dolares: ",));
    pesos = dolares * valdol;
    print("pesos = $", pesos);
    
elif (opc == 2):
    time.sleep(1.2);
    pesos = float(input("pesos: "));
    dolares = pesos / valdol;
    print("dolares = $", dolares)
    
