## Ventas por sucursal. Ingresar una serie de números por teclado que representan la cantidad de ventas realizadas en las diferentes sucursales de un país de una determinada empresa. Los requerimientos del programa son: 
## Informar la cantidad de ventas ingresadas. Total de ventas. Cantidad de ventas cuyo valores estén comprendidos entre 100 y 300 unidades. Cantidad de ventas con 400,500 y 600 unidades. Indicar si hubo una cantidad de ventas inferior a 50 unidades. Usted deberá ingresar cantidad es de ventas hasta que se ingrese un valor negativo.


#variables
venta = int();
i_ventas_ingresadas = int();
total_ventas = int();
i_entre100y300 = int();
i_400 = int();
i_500 = int();
i_600 = int();
menor_50 = bool();

venta = 0;
i_ventas_ingresadas = 0;
total_ventas = 0;
i_entre100y300 = 0;
i_400 = 0;
i_500 = 0;
i_600 = 0;
menor_50 = False;

#desarrollo

venta = int(input("Cantidad de unidades vendidas en la sucursal: "));
while (venta >= 0):
    i_ventas_ingresadas += 1;
    total_ventas += venta;

    if (venta >= 100 and venta <= 300):
        i_entre100y300 += 1;

    if (venta == 400):
        i_400 += 1;

    if (venta == 500):
        i_500 += 1;

    if (venta == 600):
        i_600 += 1;

    if (venta < 50):
        menor_50 = True;

    venta = int(input("Cantidad de unidades vendidas en la sucursal: "));
    
    
print("Cantidad de ventas ingresadas:", i_ventas_ingresadas);
print("Total de unidades vendidas:", total_ventas);
print("Cantidad de ventas comprendidads entre 100 y 300 unidades:", i_entre100y300);
print("Cantidad de ventas de 400 unidades:", i_400);
print("Cantidad de ventas de 500 unidades:", i_500);
print("Cantidad de ventas de 600 unidades:", i_600);

if (menor_50 == True):
    print("Hubo por lo menos una venta menor a 50 unidades");
elif (menor_50 == False):
    print("No hubo ventas menores a 50 unidades");