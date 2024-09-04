package co.edu.konradlorenz.modul;

public class Circulo extends Forma{
	
	protected double radio;

	public Circulo(Ubicacion c, double x, double y, double radio) {
		super(c, x, y);
		this.radio = radio;
	}

	public Circulo() {
		
	}

	public Circulo(Ubicacion c, double x, double y) {
		super(c, x, y);
	}

	public double getRadio() {
		return radio;
	}

	public void setRadio(double radio) {
		this.radio = radio;
	}
	
	@Override
    public double area() {
        return Math.PI * Math.pow(radio, 2);
    }

    @Override
    public double perimetro() {
        return 2 * Math.PI * radio;
    }
    
	@Override
	public String toString() {
		return "Circulo [radio=" + radio + "]";
	}

	

	
	
	
}
