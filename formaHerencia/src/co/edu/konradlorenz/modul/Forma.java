package co.edu.konradlorenz.modul;

public class Forma {
	
	public Ubicacion c = new Ubicacion();
	public double x = c.getX();
	public double y = c.getY();

	public Forma(Ubicacion c, double x, double y) {
		this.c = c;
		this.x = x;
		this.y = y;
	}


	public Forma() {
		
	}


	@Override
	public String toString() {
		return "Forma [c=" + c + "]";
	}
	
	 public double area(double lado1, double lado2) {
	        return lado1 * lado2;
	    }
	
	 public double area(double radio) {
	        return Math.PI * Math.pow(radio, 2);
	    }
	 
	 public double perimetro(double lado1, double lado2) {
	        return 2 * (lado1 + lado2);
	    }
	 
	 public double perimetro(double radio) {
	        return 2 * Math.PI * radio;
	    }
}
