#Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar.

#variables
n = int();
a = int();
b = int();
c = int();
fibo = int();

n = 0;
a = 0;
b = 0;
c = 0;
fibo = 0;
#desarrollo
n = int(input("Ingresar un numero: "));

a = 0;
b = 1;
print(a, ",", b, end="");
for c in range (n - 2):
    fibo = a + b;
    print(",", fibo, end="");
    a = b;
    b = fibo;