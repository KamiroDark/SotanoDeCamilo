package control;

import java.util.ArrayList;

import modelo.EmpleadoDAO;
import modelo.EmpleadoDTO;

public class Controlador {

    public void run() {
        
        EmpleadoDAO dao = new EmpleadoDAO();
        ArrayList<EmpleadoDTO> lista = dao.readALL();
        for (EmpleadoDTO emp : lista) {
            System.out.println("ID: " + emp.getId());
            System.out.println("Nombre: " + emp.getNombre());
            System.out.println("Apellido: " + emp.getApellido());
            System.out.println("Salario: " + emp.getSalario());
            System.out.println("Días: " + emp.getDias());
            System.out.println("-----------------------------");
        }
    }
}
