#Últimos dígitos ¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número entero? ¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue un número entero por teclado, y muestre el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado).

#variables
a = int();

a = 0;
#desarrollo
a = int(input("ingrese un numero entero. Se le devolvera el ultimo digito y los dos ultimos: "));
ultdig = a % 10;
ultdosdig = a % 100;

print("el ultimo digito es:", ultdig);
print("los ultimos dos digitos son:", ultdosdig);