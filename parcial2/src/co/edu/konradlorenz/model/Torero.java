package co.edu.konradlorenz.model;

public class Torero extends Persona {
	
	private String apodo;
	private String fecha;
	private Torero padrino;
	
	public Torero(long cedula, String nombre, String apodo, String fecha, Torero padrino) {
		super(cedula, nombre);
		this.apodo = apodo;
		this.fecha = fecha;
		this.padrino = padrino;
	}
	
	public Torero() {
	}
	
	public Torero(long cedula, String nombre) {
		super(cedula, nombre);
	}

	public String getApodo() {
		return apodo;
	}

	public void setApodo(String apodo) {
		this.apodo = apodo;
	}

	public String getFecha() {
		return fecha;
	}

	public void setFecha(String fecha) {
		this.fecha = fecha;
	}

	public Torero getPadrino() {
		return padrino;
	}

	public void setPadrino(Torero padrino) {
		this.padrino = padrino;
	}

	@Override
	public String toString() {
		return "Torero [apodo=" + apodo + ", fecha=" + fecha + ", padrino=" + padrino + "]";
	}

	@Override
	public String mostrarInformacion() {
		
		return "Nombre: " + nombre + ", Cedula: " + cedula + ", Apodo: " + apodo + ", Fecha: " + fecha + ", Padrino: " + padrino ;
	}
	
	
}
