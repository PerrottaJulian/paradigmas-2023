#Cuadrado de un binomio. Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores 𝑎 y 𝑏, que: Un binomio al cuadrado (suma) es igual al cuadrado del primer término, más el doble producto del primero por el segundo más el cuadrado del segundo.

#variables
a = int();
b = int();
bin = int();

a = 0;
b = 0;
bin = 0;

#desarrollo
print("Ingrese dos numeros. Se realizara el cuadrado de la suma de los numeros (cuadrado de un binomio)");

a = int(input("a = "));
b = int(input("b = "));

bin = a**2 + 2*a*b + b**2;

print("El resultado es:", bin);