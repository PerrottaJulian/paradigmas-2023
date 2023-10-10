"""
Dada la fracción P/Q, para P y Q naturales informar la mayor cantidad de simplificaciones. 
Desarrolle y utilice una función que reciba dos números naturales y retorne el menor factor común. 
Ej: 360/60 = 180/30 = 90/15 = 30/5 = 6/1 
"""
#2023

#modulos
def esDivisible(dividendo, divisor):
    if dividendo % divisor == 0:
        return True;
    else:
        return False;
    
def simplificar(fraccion):
    divisores = [2,3,4,5,6,7,8,9];
    for divisor in divisores:
        if (esDivisible(fraccion[0], divisor) == True and esDivisible(fraccion[1], divisor) == True):
            fraccion[0] //= divisor
            fraccion[1] //= divisor
            return fraccion
    return 0
#codigo principal
P = -1
Q = -1

seguir = True

print("Ingresar P/Q, siendo P y Q numeros naturales");
while P <= 0:
    try:
        P = int(input("P = "));
    except:
        continue

while Q <= 0:
    try:
        Q = int(input("Q = "));
    except:
        continue

mifraccion = [P,Q]

while mifraccion != 0:
    print(f"{mifraccion[0]}/{mifraccion[1]} ", end="= ")
    mifraccion = simplificar(mifraccion)
