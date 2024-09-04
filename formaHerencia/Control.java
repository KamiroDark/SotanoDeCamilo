package co.edu.konradlorenz.controller;

import co.edu.konradlorenz.modul.Circulo;
import co.edu.konradlorenz.modul.Forma;
import co.edu.konradlorenz.modul.Rectangulo;
import co.edu.konradlorenz.modul.Ubicacion;
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
				double posicionX = Ventana.pedirDouble("Ingrese la posición en X:");
                double posicionY = Ventana.pedirDouble("Ingrese la posición en Y:");
                double radio = Ventana.pedirDouble("Ingrese el radio del círculo, por favor:");
                Circulo circulo = new Circulo(new Ubicacion(posicionX, posicionY), posicionX, posicionY, radio);

                objVentana.mostrarMensaje(circulo.toString());
                objVentana.mostrarMensaje("Área: " + circulo.area());
                objVentana.mostrarMensaje("Perímetro: " + circulo.perimetro());
				break;
			}
			case 2: {
				 double posicionX = Ventana.pedirDouble("Ingrese la posición en X:");
                 double posicionY = Ventana.pedirDouble("Ingrese la posición en Y:");
                 double lado1 = Ventana.pedirDouble("Ingrese el lado 1 del rectángulo, por favor:");
                 double lado2 = Ventana.pedirDouble("Ingrese el lado 2 del rectángulo, por favor:");
                 Rectangulo rectangulo = new Rectangulo(new Ubicacion(posicionX, posicionY), posicionX, posicionY, lado1, lado2);

                 objVentana.mostrarMensaje(rectangulo.toString());
                 objVentana.mostrarMensaje("Área: " + rectangulo.area());
                 objVentana.mostrarMensaje("Perímetro: " + rectangulo.perimetro());
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
