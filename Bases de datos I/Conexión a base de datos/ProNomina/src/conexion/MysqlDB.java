
package conexion;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;


public class MysqlDB {

    private String url = "jdbc:mysql://localhost:3306/db_nomina";
    private String driver = "com.mysql.cj.jdbc.Driver";
    private String usuario = "root";
    private String clave = "";

    // Patron Singleton

    private static MysqlDB cnx = null;
    private Connection conn;

    private MysqlDB() {
        try {
            Class.forName(driver);
            conn = DriverManager.getConnection(url, usuario, clave);
        } catch (ClassNotFoundException ex) {
            System.out.println("error en cargar Driver" + ex.getMessage());
        } catch (SQLException ex) {
            System.out.println("Error en obtener conexión BD" + ex.getMessage());
        }
    }

    public static MysqlDB getConexion() {

        if (cnx == null) {
            cnx = new MysqlDB();
        }

        return cnx;
    }

    public Connection getConn() {
        return conn;
    }

    public void cerrarConn() {
        if (conn != null) {
            try {
                conn.close();
                System.out.println("Conexión cerrada.");
            } catch (SQLException ex) {
                System.err.println("Error al cerrar la conexión: " + ex.getMessage());
            }
        }
    }
}
