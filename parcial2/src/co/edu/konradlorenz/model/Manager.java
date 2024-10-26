package co.edu.konradlorenz.model;

public class Manager extends Persona {
	
	private String direccion;
    private String telefono;
    
	public Manager(long cedula, String nombre, String direccion, String telefono) {
		super(cedula, nombre);
		this.direccion = direccion;
		this.telefono = telefono;
	}

	public Manager() {
	}

	public Manager(long cedula, String nombre) {
		super(cedula, nombre);
	}

	public String getDireccion() {
		return direccion;
	}

	public void setDireccion(String direccion) {
		this.direccion = direccion;
	}

	public String getTelefono() {
		return telefono;
	}

	public void setTelefono(String telefono) {
		this.telefono = telefono;
	}

	@Override
	public String toString() {
		return "Manager [direccion=" + direccion + ", telefono=" + telefono + "]";
	}

	@Override
	public String mostrarInformacion() {
		return "Nombre: " + nombre + ", Cedula: " + cedula + ", telefono: " + telefono + ", Dirección: " + direccion;
	}
    
    
	
}
