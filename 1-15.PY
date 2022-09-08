##Suma - División - Potencia. Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.

#variables
a = int();
b = int();
c = int();
sum = int();
res_fin = int();

a = 0;
b = 0;
c = 0;
sum = 0;
res_fin = 0;

#desarrollo
print("Debera ingesar 3 numeros. Se realizara la suma de estos. Si el resultado es mayor a 10 se lo dividira por 2, sino se lo potenciara al cubo");

a = int(input("a: "));
b = int(input("b: "));
c = int(input("c: "));

sum =  a + b + c;

if (sum > 10):
    res_fin = sum // 2;
    print ("resultado:", res_fin, " (", sum, ")"   );
else:
    res_fin = sum ** 3;
    print ("resultado:", res_fin, " (", sum, ")");




