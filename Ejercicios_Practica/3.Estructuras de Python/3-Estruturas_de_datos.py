#ESTRUCTURAS DE DATOS PRIMITIVAS EN PYTHON

#Listas

my_list=["Kamiro", "Kira", "Cami"]
print(my_list)
my_list.append("Wewe") #.append es para agregar a la lista [Insersión]
print(my_list)
my_list.remove("Kamiro")
print(my_list) #.remove es para eliminar en la lista [Borrar]
print(my_list[1]) # Acceder
my_list[2]= "Juanito" #Actualizar
print(my_list)
my_list.sort() #Organizar de manera alfabetica o numerica la misma lista
print(my_list)

# Tuplas (Son inmutables, es segura)
my_tuple = ("Camilo", "Prieto", "@KamiroDark", "21")
print(my_tuple[2]) #Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) #sorted organiza y crea una lista nueva [Ordenación]
print(type(my_tuple))
print(my_tuple)

#Sets (Evita duplicados pero no tiene un orden o posición de sus objetos)
my_set = {"Camilo", "Prieto", "@KamiroDark", "21"}
print(my_set)
my_set.add("prietocamilo21@gmail.com") # Inserción no permite duplicados
my_set.add("prietocamilo21@gmail.com")
print(my_set)
my_set.remove("Prieto") # Eliminacion
print(my_set)
my_set = set(sorted(my_set)) #No se puede ordenar
print(my_set)
print(type(my_set))

#Diccionario
my_dict: dict = {
                 "name":"Camilo", 
                 "lastname":"Prieto", 
                 "user":"@Kamiro", 
                 "age":"21"
                 }
print(my_dict)
print(my_dict["name"])#Acesso
my_dict["email"] = "prietocamilo21@gmail.com"#Inserción
print(my_dict["email"])
my_dict["name"]= "Kamiro" #Actualización
print(my_dict)
del my_dict["lastname"] #Eliminación
print(my_dict)
my_dict=dict(sorted(my_dict.items())) #Ordenación
print(my_dict)
print(type(my_dict))