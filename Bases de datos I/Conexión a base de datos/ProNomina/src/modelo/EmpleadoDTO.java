/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package modelo;

import java.io.Serializable;
import java.util.Objects;

/**
 *
 * @author Usuario
 */
public class EmpleadoDTO implements Serializable{
    private int id;
    private String nombre;
    private String apellido;
    private double salario;
    private int dias;

    public EmpleadoDTO() {
    }
    
    //Para cuando necesite crear un objeto y solo tenga el id
    public EmpleadoDTO(int id) {
        this.id = id;
    }
    
    //Guarda el resultado de la consulta el registro de la base de datos
    public EmpleadoDTO(int id, String nombre, String apellido, double salario, int dias) {
        this.id = id;
        this.nombre = nombre;
        this.salario = salario;
        this.dias = dias;
    }
    
    //Para la creación de un objeto desde un formulario
    public EmpleadoDTO(String nombre, double salario, int dias) {
        this.nombre = nombre;
        this.salario = salario;
        this.dias = dias;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public int getDias() {
        return dias;
    }

    public void setDias(int dias) {
        this.dias = dias;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }
    
    @Override
    public int hashCode() {
        int hash = 5;
        hash = 67 * hash + this.id;
        hash = 67 * hash + Objects.hashCode(this.nombre);
        hash = 67 * hash + (int) (Double.doubleToLongBits(this.salario) ^ (Double.doubleToLongBits(this.salario) >>> 32));
        hash = 67 * hash + this.dias;
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final EmpleadoDTO other = (EmpleadoDTO) obj;
        if (this.id != other.id) {
            return false;
        }
        if (Double.doubleToLongBits(this.salario) != Double.doubleToLongBits(other.salario)) {
            return false;
        }
        if (this.dias != other.dias) {
            return false;
        }
        return Objects.equals(this.nombre, other.nombre);
    }

    @Override
    public String toString() {
        return "EmpleadoDTO{" + "id=" + id + ", nombre=" + nombre + ", salario=" + salario + ", dias=" + dias + '}';
    }
    
    
}
