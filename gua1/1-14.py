##Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas:

##Componer la dirección de correo de la siguiente manera: @ Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= umet.edu.ar la dirección de mail sería: fsteffolani@umet.edu.ar.

##Pero si la primera primera letra del nombre y la primera letra del apellido son la misma entonces uƟlizar: .@ Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería: soledad.steffolani@umet.edu.ar

#variables
nombre = str();
apellido = str();
dominio = str();

nombre = "";
apellido = "";
dominio = "";

#desarrollo
print("Debera ingresar su nombre, apellido y dominio deseado, y se le dara propondra una direccion de correo electronico automatico")
nombre = str(input("nombre: "));
apellido = str(input("apellido: "));
dominio = str(input("dominio: "));

nombre = nombre.lower();
apellido = apellido.lower();
dominio = dominio.lower();

if (nombre[0] == apellido[0]):
    print("Direccion de correo nueva:");
    print(nombre + "." + apellido + "@" + dominio);
else :
    print("Direccion de correo nueva:");

    print(nombre[0] + apellido + "@" + dominio);



