#Conversión de medidas. Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en: yardas pulgadas centimetros metros 
#Sabiendo que: 1 pie = 12 pulgadas 1 yarda = 3 pies 1 pulgada = 2.54 centímetros 1 metro =1000

#variables
pies = int();
pulg = int();
yar = float();
cent = float();
met = float();

pies = 0;
pulg = 0;
yar = 0.0;
cent = 0.0;
met = 0.0;

#desarrollo
pies = int(input("Ingresar una medida, en pies. Se le devolvera sus equivalencias en otros sistemas de medicion: "));

pulg = 12 * pies;
yar = pies/3;
cent = pulg * 2.54;
met = cent/1000;

print("pulgadas:", pulg, "yardas:", yar, "centimetros:", cent, "metros", met);