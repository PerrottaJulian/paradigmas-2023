## Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.


#variables
n_mes = int();
n_mes = 0;

#desarrollo
meses = ["Enero", "Febrero", "Marzo","Abril", "Mayo", "Junio", "Julio","Agosto","Septiembre", "Octubre","Noviembre", "Diciembre"];
dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

n_mes = int(input("Ingresar numero de mes: "));

while (n_mes > len(meses)):
    print("Error, no existe mes", n_mes);
    n_mes = int(input("Ingresar numero de mes: "));

print("Nombre:", meses[n_mes - 1]);
print("Dias:", dias_meses[n_mes - 1]);

