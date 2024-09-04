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
	
	 public double area() {
	        return 0;
	    }

	    public double perimetro() {
	        return 0;
	    }

}
