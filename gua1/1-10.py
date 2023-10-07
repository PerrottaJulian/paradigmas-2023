#Escribir un programa que pida dos números y muestre como resultado su división, cociente y resto.

#variables
a = int();
b = int();
coc = int();
res = int();

a = 0;
b = 0;
coc = 0;
res = 0;

#desarrollo
print("Ingrese dos numeros a y b. Se le dara el resultado de su division, con cociente y resto");
a = int(input("a = "));
b = int(input("b = "));

coc = a // b;
res = a % b;

print("El resultado de la division es", coc, "con resto", res);
