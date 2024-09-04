package co.edu.konradlorenz.modul;

public class Rectangulo extends Forma {
	
	protected double lado1;
	protected double lado2;
	
	public Rectangulo(Ubicacion c, double x, double y, double lado1, double lado2) {
		super(c, x, y);
		this.lado1 = lado1;
		this.lado2 = lado2;
	}

	public Rectangulo() {
		
	}

	public Rectangulo(Ubicacion c, double x, double y) {
		super(c, x, y);
		
	}

	public double getLado1() {
		return lado1;
	}

	public void setLado1(double lado1) {
		this.lado1 = lado1;
	}

	public double getLado2() {
		return lado2;
	}

	public void setLado2(double lado2) {
		this.lado2 = lado2;
	}

	@Override
	public String toString() {
		return "Rectangulo [lado1=" + lado1 + ", lado2=" + lado2 + "]";
	}
	
	
	
	
	
}
