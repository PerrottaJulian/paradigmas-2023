## Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

#carpetas
import time;

#variables
n1 = int();
n2 = int();
n3 = int();

n1 = 0;
n2 = 0;
n3 = 0;

#desarrollo
lista1 = [];
lista2 = [];
lista3 = [];

print("Ingresar 5 valores enteros para LISTA1");
for i in range (5):
    n1 = int(input("Numero: "));
    lista1.append(n1);

print("Ingresar 5 valores enteros para LISTA2");
for i2 in range (5):
    n2 = int(input("Numero: "));
    lista2.append(n2);



for i3 in range (len(lista1)):
    n3 = lista1[i3] + lista2[i3];
    lista3.append(n3);

print("Lista1:", lista1)
print("Lista2:", lista2)
print("Lista3:", lista3)