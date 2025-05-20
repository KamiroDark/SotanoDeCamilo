--Taller_2 Consultas basicas SCRIPTS
--Juan Camilo Prieto Mestizo - 506232717

CREATE DATABASE TALLER_2;

USE TALLER_2;

--Tabla empleados
create table emple(emp_no INTEGER PRIMARY KEY, 
apellido VARCHAR(50) NOT NULL, 
oficio VARCHAR(30), 
dir INTEGER, 
fecha_alt DATE, 
salario INTEGER, 
comision INTEGER, 
dept_no INTEGER);

DESCRIBE emple;

--Tabla departamentos
create table depart( 
dept_no INTEGER PRIMARY KEY, 
dnombre VARCHAR(30), 
loc VARCHAR(30)); 

DESCRIBE depart;

---Llave foreanea
ALTER TABLE emple ADD CONSTRAINT fk_dept_no FOREIGN KEY (dept_no) REFERENCES depart(dept_no);

--Datos insertados en la tabla empleados
INSERT INTO emple VALUES (7369,'SÁNCHEZ','EMPLEADO',7902,'1990/12/17', 
1040,NULL,20); 
INSERT INTO emple VALUES (7499,'ARROYO','VENDEDOR',7698,'1990/02/20', 
1500,390,30); 
INSERT INTO emple VALUES (7521,'SALA','VENDEDOR',7698,'1991/02/22', 
1625,650,30); 
INSERT INTO emple VALUES (7566,'JIMÉNEZ','DIRECTOR',7839,'1991/04/02', 
2900,NULL,20); 
INSERT INTO emple VALUES (7654,'MARTÍN','VENDEDOR',7698,'1991/09/29', 
1600,1020,30); 
INSERT INTO emple VALUES (7698,'NEGRO','DIRECTOR',7839,'1991/05/01', 
3005,NULL,30); 
INSERT INTO emple VALUES (7782,'CEREZO','DIRECTOR',7839,'1991/06/09', 
2885,NULL,10); 
INSERT INTO emple VALUES (7788,'GIL','ANALISTA',7566,'1991/11/09', 
3000,NULL,20); 
INSERT INTO emple VALUES (7839,'REY','PRESIDENTE',NULL,'1991/11/17', 
4100,NULL,10); 
INSERT INTO emple VALUES (7844,'TOVAR','VENDEDOR',7698,'1991/09/08', 
1350,0,30); 
INSERT INTO emple VALUES (7876,'ALONSO','EMPLEADO',7788,'1991/09/23', 
1430,NULL,20); 
INSERT INTO emple VALUES (7900,'JIMENO','EMPLEADO',7698,'1991/12/03', 
1335,NULL,30); 
INSERT INTO emple VALUES (7902,'FERNÁNDEZ','ANALISTA',7566,'1991/12/03', 
3000,NULL,20); 
INSERT INTO emple VALUES (7934,'MUÑOZ','EMPLEADO',7782,'1992/01/23', 
1690,NULL,10);

--Datos insertados en la tabla departamentos
INSERT INTO depart VALUES (10,'CONTABILIDAD','SEVILLA'); 
INSERT INTO depart VALUES (20,'INVESTIGACIÓN','MADRID'); 
INSERT INTO depart VALUES (30,'VENTAS','BARCELONA'); 
INSERT INTO depart VALUES (40,'PRODUCCIÓN','BILBAO'); 

--1. Mostrar el apellido, oficio y número de departamento de cada empleado. 
SELECT apellido, oficio, dept_no 
FROM emple;

--2. Mostrar el número, nombre y localización de cada departamento.
SELECT dept_no, dnombre, loc 
FROM depart;

--3. Mostrar todos los datos de todos los empleados.
SELECT * 
FROM emple;

--4. Datos de los empleados ordenados por apellidos.
SELECT * 
FROM emple 
ORDER BY apellido ASC;

--5. Datos de los empleados ordenados por número de departamento descendentemente.
SELECT * 
FROM emple 
ORDER BY dept_no DESC;

--6. Datos de los empleados ordenados por número de departamento descendentemente y dentro de cada departamento ordenados por apellido ascendentemente.
SELECT * 
FROM emple 
ORDER BY dept_no DESC, apellido ASC;

--7. Mostrar los datos de los empleados cuyo salario sea mayor que 2000.
SELECT * 
FROM emple 
WHERE salario > 2000;

--8.Mostrar los datos de los empleados cuyo oficio sea ANALISTA.
SELECT * 
FROM emple 
WHERE oficio = 'ANALISTA';

--9. Seleccionar el apellido y oficio de los empleados del departamento número 20.
SELECT apellido, oficio 
FROM emple 
WHERE dept_no = 20;

--10. Mostrar todos los datos de los empleados ordenados por apellido.
SELECT * 
FROM emple 
ORDER BY apellido ASC;
