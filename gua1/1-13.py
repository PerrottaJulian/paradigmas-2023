##Crear un conversor de pies y pulgadas a centímetros.


#constantes
unpie = 30.48;
unapulg = 2.54;

#variables
preg = int();
pies = float();
centipies = float();
pulg = float();
centipulg = float();

preg = 0;
pies = 0.0;
centipies = 0.0;
pulg = 0.0;
centipulg = 0.0;

#desarrollo
preg = int(input("Conversor a centimetros. Ingrese 1 para convertir pies o ingrese 2 para convertir pulgadas: "));

if (preg == 1):
    pies = float(input("pies: "));
    centipies = pies * unpie;
    print("centimetros:", centipies);

elif (preg == 2):
    pulg = float(input("pulgadas: "));
    centipulg = pulg * unapulg;
    print("centimetros:", centipulg);

