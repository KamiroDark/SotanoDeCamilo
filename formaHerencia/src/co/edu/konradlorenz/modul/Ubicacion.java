package co.edu.konradlorenz.modul;

public class Ubicacion {
	
	private double x  = 0;
	private double y = 0;
	
	public Ubicacion(double x, double y) {
		this.setX(x);
		this.y = y;
	}

	
	public Ubicacion() {
		
	}


	public double getX() {
		return x;
	}

	public void setX(double x) {
		this.x = x;
	}

	public double getY() {
		return y;
	}

	public void setY(double y) {
		this.y = y;
	}
	
	
}
