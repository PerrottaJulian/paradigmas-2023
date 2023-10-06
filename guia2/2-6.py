## Mostrar por pantalla el promedio de los números ingresados por teclado. Se deja de pedir que el usuario agregue números una vez ingrese 0 (cero).

# variables
n = float();
sum = float();
i = int();
prom = float();

n = 0.0;
sum = 0.0;
i = 0;
prom = 0.0;

# desarrollo
print("Debera ingresar la cantidad de numeros que se desee y se hara el promedio de ellos. Para finalizar tiene que ingresar 0")
n = float(input("Ingrese un numero: "));

while (n != 0):
    sum += n;
    n = float(input("Ingrese un numero: "));
    i += 1;

prom = sum/i;

print("El promedio es:", prom);