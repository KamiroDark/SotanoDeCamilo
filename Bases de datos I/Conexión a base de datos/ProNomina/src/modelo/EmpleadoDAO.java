package modelo;

import conexion.MysqlDB;
import java.sql.*;
import java.util.ArrayList;

public class EmpleadoDAO {

    private MysqlDB con = MysqlDB.getConexion(); // Obtenemos la instancia del Singleton
    private final String SQLREAD_ALL = "SELECT * FROM tb_empleados";

    public ArrayList<EmpleadoDTO> readALL() {
        ArrayList<EmpleadoDTO> lista = new ArrayList<>();
        PreparedStatement ps = null;
        ResultSet rs = null;

        try {
            ps = con.getConn().prepareStatement(SQLREAD_ALL);
            rs = ps.executeQuery();

            while (rs.next()) {
                EmpleadoDTO emp = new EmpleadoDTO();
                emp.setId(rs.getInt("id_empleado"));
                emp.setNombre(rs.getString("nombre"));
                emp.setApellido(rs.getString("apellido"));
                emp.setDias(rs.getInt("Dias"));
                emp.setSalario(rs.getDouble("sueldo"));
                lista.add(emp);
            }

        } catch (SQLException ex) {
            System.err.println("Error al leer empleados: " + ex.getMessage());
        } finally {
            try {
                if (rs != null) rs.close();
                if (ps != null) ps.close();
            } catch (SQLException ex) {
                System.err.println("Error al cerrar recursos: " + ex.getMessage());
            }
        }

        return lista;
    }
}
