package co.edu.konradlorenz.controller;

import co.edu.konradlorenz.modul.Forma;
import co.edu.konradlorenz.view.Ventana;

public class Control {
	protected Forma objForma = new Forma();
	protected Ventana objVentana = new Ventana();

	public void run() {
		String menu = "----------Bienvenid@----------\n" + "-----¿Qué figura desea seleccionar?-----\n" + "1. Círculo\n"
				+ "2. Rectángulo\n" + "3. Salir\n";
		int op;

		do {
			objVentana.mostrarMensaje(menu);
			op = Ventana.pedirInt("");
			switch (op) {
			
			case 1: {
				double posicionX = Ventana.pedirDouble("Ingrese la posicion en X");
				double posicionY = Ventana.pedirDouble("Ingrese la posicion en Y");
				double radio = Ventana.pedirDouble("Ingrese el radio del circulo, por favor:");
				double area = objForma.area(radio);
				double perimetro = objForma.perimetro(radio);

				objVentana.mostrarMensaje("Figura: Círculo");
				objVentana.mostrarMensaje("Ubicación: (" + posicionX + ", " + posicionY + ")");
				objVentana.mostrarMensaje("Área: " + area);
				objVentana.mostrarMensaje("Perímetro: " + perimetro);

				break;
			}
			case 2: {
				double posicionX = Ventana.pedirDouble("Ingrese la posicion en X");
				double posicionY = Ventana.pedirDouble("Ingrese la posicion en Y");
				double lado1 = Ventana.pedirDouble("Ingrese el lado 1 del rectangulo, por favor");
				double lado2 = Ventana.pedirDouble("Ingrese el lado 2 del rectangulo, por favor");
				double area = objForma.area(lado1, lado2);
				double perimetro = objForma.perimetro(lado1, lado2);
				
				objVentana.mostrarMensaje("Figura: Rectángulo");
                objVentana.mostrarMensaje("Ubicación: (" + posicionX + ", " + posicionY + ")");
                objVentana.mostrarMensaje("Área: " + area);
                objVentana.mostrarMensaje("Perímetro: " + perimetro);
				break;
			}
			case 3: {
				objVentana.mostrarMensaje("Gracias! Saliendo del programa...");
				break;
			}
			default:
				objVentana.mostrarMensaje("Opción no válida. Intente de nuevo.");
			}
		} while (op != 3);
	}
}
