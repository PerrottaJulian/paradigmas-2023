## Dada la fracción P/Q, para P y Q naturales informar la mayor cantidad de simplificaciones. Desarrolle y utilice una función que reciba dos números naturales y retorne el menor factor común. 
## Ej: 360/60 = 180/30 = 90/15 = 30/5 = 6/1


#modulos
def esDivisible(dividendo, divisor):
    if dividendo % divisor == 0:
        return True;
    else:
        return False;
    
def simplificar(num, deno):
    fraccion = [num, deno]
    divisores = [2,3,4,5,6,7,8,9];
    for divisor in divisores:
        while (esDivisible(num, divisor) == True and esDivisible(deno, divisor) == True):
            num //= divisor;
            deno //= divisor;

    return str(num) + "/" + str(deno)

#codigo principal
print("Ingresar P/Q, siendo P y Q numeros naturales");

P = int(input("P = "));
while P < 0:
    print("Numero invalido.");
    P = int(input("P = "));


Q = int(input("Q = "));
while Q < 0:
    print("Numero invalido.");
    Q = int(input("Q = "));


print(simplificar(P, Q));
    