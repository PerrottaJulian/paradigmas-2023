## Comisión de vendedores. Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadas por sus vendedores, para ello les solicita un sistemita que le permita calcular dichos montos.
## Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores(1 a 4). Usted debe solicitar el ingreso de la categoría del vendedor y el total de la venta(el proceso termina cuando se ingrese una categoría igual a cero) y acumular las comisiones de las ventas rendidas por los vendedores de diferentes en base a los siguientes cálculos:
## Categoría1:cobra una comisión de 10%
## Categoría2: cobra una comisión de 25%
## Categoría3:cobra una comisión de 30%
## Categoría4:cobra una comisión de 40%
## Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada categoría de vendedor es que en el la empresa junto con el total general.


#constantes
cat1 = 10/100;
cat2 = 25/100;
cat3 = 30/100;
cat4 = 40/100;

#variables
categoria = int();
venta = int();
tot_cat1 = float();
tot_cat2 = float();
tot_cat3 = float();
tot_cat4 = float();
tot_general = int();

categoria = 0;
venta = 0;
tot_cat1 = 0.0;
tot_cat2 = 0.0;
tot_cat3 = 0.0;
tot_cat4 = 0.0;
tot_general = 0;

#desarrollo
categoria = int(input("Categoria del vendedor: "));
while (categoria < 0 or categoria > 4):
    categoria = int(input("Error. Ingrese devuelta la cateogira del vendedor: "));

while (categoria != 0):
    venta = int(input("Ingresar total de la venta del venderdor: "));

    if (categoria == 1):
        tot_cat1 += venta * cat1;

        tot_general += tot_cat1;

    if (categoria == 2):
        tot_cat2 += venta * cat2;

        tot_general += tot_cat2;

    if (categoria == 3):
        tot_cat3 += venta * cat3;

        tot_general += tot_cat3;

    if (categoria == 4):
        tot_cat4 += venta * cat4;

        tot_general += tot_cat4;


    categoria = int(input("Categoria del vendedor: "));
    while (categoria < 0 or categoria > 4):
        categoria= int(input("Error. Ingrese devuelta la cateogira del vendedor: "));


print("El total de comisiones a pagar de vendedores categoria 1 es:", tot_cat1);
print("El total de comisiones a pagar de vendedores categoria 2 es:", tot_cat2);
print("El total de comisiones a pagar de vendedores categoria 3 es:", tot_cat3);
print("El total de comisiones a pagar de vendedores categoria 4 es:", tot_cat4);

print("El total de comisiones a pagar es:", tot_general);





