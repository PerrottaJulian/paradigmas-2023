##Desarrollar un programa que permita ingresar, para los 3 parados más votados: fórmula (presidente + vice) y cantidad de votos obtenidos. Luego determinar: Qué fórmula obtuvo el mayor porcentaje. Si la fórmula resulta elegida o se requiere segunda vuelta. En este caso, indicar también quienes parƟcipan de la segunda vuelta.


#constante
votos_necesa = 0.45;


#variables
presi1 = str();
vice1 = str();
formula1 = str();
formula1_votos = int();

presi2 = str();
vice2 = str();
formula2 = str(); 
formula2_votos = int();

presi3 = str();
vice3 = str();
formula3 = str();
formula3_votos = int();

votos_tot = int();


presi1 = "";
vice1 = "";
formula1 = "";
formula1_votos = 0;

presi2 = "";
vice2 = "";
formula2 = "";
formula2_votos = 0;

presi3 = "";
vice3 = "";
formula3 = "";
formula3_votos = 0;

votos_tot = 0

#desarrollo
print("Elecciones presidenciales. Ingrese la primera formula: ");
presi1 = str(input("Candidato a Presidente: "));
presi1 = presi1.lower();
vice1 = str(input("Candidato a Vicepresidente: "));
vice1= vice1.lower();
formula1 = presi1.capitalize() + "-" + vice1.capitalize();
print("cantidad de votos obtenidos por", formula1, end=": ");
formula1_votos = int(input(""));

print("Segunda formula: ");
presi2 = str(input("Candidato a Presidente: "));
presi2 = presi2.lower();
vice2 = str(input("Candidato a Vicepresidente: "));
vice2= vice2.lower();
formula2 = presi2.capitalize() + "-" + vice2.capitalize();
print("cantidad de votos obtenidos por", formula2, end=": ");
formula2_votos = int(input(""));

print("Tercer formula: ");
presi3 = str(input("Candidato a Presidente: "));
presi3 = presi3.lower();
vice3 = str(input("Candidato a Vicepresidente: "));
vice3= vice3.lower();
formula3 = presi3.capitalize() + "-" + vice3.capitalize();
print("cantidad de votos obtenidos por", formula3, end=": ");
formula3_votos = int(input(""));

votos_tot = formula1_votos + formula2_votos + formula3_votos

if (formula1_votos > votos_tot * votos_necesa):
    print(presi1.capitalize(), "es el nuevo presidente de la nacion");
elif(formula2_votos > votos_tot * votos_necesa):
    print(presi2.capitalize(), "es el nuevo presidente de la nacion");
elif(formula3_votos > votos_tot * votos_necesa):
    print(presi3.capitalize(), "es el nuevo presidente de la nacion");

else:
    if (formula1_votos > formula2_votos and formula1_votos > formula3_votos):
        if (formula2_votos > formula3_votos):
            print("Hay balotagge entre", formula1, "(primeros) y", formula2, "(segundos)");
        elif (formula3_votos > formula2_votos):
            print("Hay balotagge entre", formula1, "(primeros) y", formula3, "(segundos)");
    

    elif (formula2_votos > formula1_votos and formula2_votos > formula3_votos):
        if (formula1_votos > formula3_votos):
            print("Hay balotagge entre", formula2, "(primeros) y", formula1, "(segundos)");
        elif (formula3_votos > formula1_votos):
            print("Hay balotagge entre", formula2, "(primeros) y", formula3, "(segundos)");


    elif (formula3_votos > formula1_votos and formula3_votos > formula2_votos):
        if (formula1_votos > formula2_votos):
            print("Hay balotagge entre", formula3, "(primeros) y", formula1, "(segundos)");
        elif (formula2_votos > formula1_votos):
            print("Hay balotagge entre", formula3, "(primeros) y", formula2, "(segundos)");

