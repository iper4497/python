/** Esto se compila de la siguiente forma g++ -o hola arduino.cpp **/
#include <iostream>
#include <fstream>
using namespace std;

//definimos variables para datos a enviar
//y donde enviarlos
char cadena[17];
ofstream arduino;
char puerto[] = "/dev/ttyUSB0";

int main () {
	//abrimos el puerto usb como un fichero
	//y lo configuramos como salida
	arduino.open (puerto, ios::out);
	
	//obtenemos la cadena  por la entrada
	//estandar y la enviamos por la 
	//salida que hemos configurado
	cout << "Mensaje a enviar: ";
	cin >> cadena;
	arduino << cadena;
	
	//cerramos el usb y sanseacabo
	arduino.close();
	return 0;
}

