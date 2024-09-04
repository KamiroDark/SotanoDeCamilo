package co.edu.konradlorenz.view;

import java.util.Scanner;

public class Ventana {
	
	public static Scanner sc = new Scanner(System.in);
	
	public static double pedirDouble(String dato) {
		System.out.println(dato);
		double opcion = sc.nextDouble();
		return opcion;
	}
	
	public static int pedirInt(String dato) {
		System.out.println(dato);
		int opcion = sc.nextInt();
		return opcion;
	}
	
	public void mostrarMensaje(String mensaje) {
		System.out.println(mensaje);
	}
}
