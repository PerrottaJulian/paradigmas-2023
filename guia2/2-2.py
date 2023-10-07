##Secuencia de impares. Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre ellos, en forma ascendente y descendente.

#variables
a = int();
b = int();

a = 0;
b = 0;

i = 0;
#desarrollo
print("debera ingresar dos numeros a y b. Se devolveran todos los numeros impares entre ambos numeros");

a = int(input("a = "));
b = int(input("b = "));

for i in range(a+1, b):
    if (i % 2 != 0):
        print(i, end=", ");

print("")
i = 0
for i in range(b-1, a, -1):
    if (i % 2 != 0):
        print(i, end=", ");



