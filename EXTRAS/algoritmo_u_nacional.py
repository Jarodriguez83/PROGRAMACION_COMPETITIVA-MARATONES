#UNIVERSIDAD NACIONAL - ALGORITMO PARA CALCULAR EL NUMERO DE LIBROS QUE SE PUEDEN PRESTAR
inventario = [
    {
        "nombre_libro": "CIEN AÑOS DE SOLEDAD",
        "estado": "BIBLIOTECA",
        "codigo_estudiante": "",
        "nombre_estudiante": ""
    },

    {
        "nombre_libro": "ALGORITMOS Y DISEÑO DE PROGRAMAS",
        "estado": "BIBLIOTECA",
        "codigo_estudiante": "",
        "nombre_estudiante": ""
    },

    {
        "nombre_libro": "ALGEBRA LINEAL",
        "estado": "BIBLIOTECA",
        "codigo_estudiante": "",
        "nombre_estudiante": ""
    },

    {
        "nombre_libro": "LA SOMBRA DEL VIENTO",
        "estado": "PRESTADO",
        "codigo_estudiante": "",
        "nombre_estudiante": ""
    }
]
# DÍA 1 -> FUNCIÓN PARA PRESTAR LIBROS
def prestar_libro(inventario):
    print("\n FUNCIÓN PRESTAR LIBRO")
    codigo = input("- CÓDIGO DEL ESTUDIANTE: ")
    nombre = input("- NOMBRE DEL ESTUDIANTE: ")
    libro_buscar = input("- NOMBRE DEL LIBRO: ")
    encontrado = False
    # Recorrer inventario
    for libro in inventario:
        # Verificar si el libro existe
        if libro["nombre_libro"].lower() == libro_buscar.lower():
            encontrado = True
            # Verificar si está disponible
            if libro["estado"] == "BIBLIOTECA":
                libro["estado"] = "PRESTADO"
                libro["codigo_estudiante"] = codigo
                libro["nombre_estudiante"] = nombre
                print("\nLibro prestado correctamente.")
                print("Libro:", libro["nombre_libro"])
                print("Estudiante:", nombre)
            else:
                print("\n EL LIBRO YA HA SIDO PRESTADO.")
    # Si nunca encontró el libro
    if encontrado == False:
        print("\n EL LIBRO NO EXISTE.")
# DÍA 4 -> FUNCIÓN PARA DEVOLVER LIBROS
def devolver_libro(inventario):
    print("\n DEVOLVER LIBRO ")
    libro_buscar = input("- NOMBRE DEL LIBRO: ")
    encontrado = False
    for libro in inventario:
        if libro["nombre_libro"].lower() == libro_buscar.lower():
            encontrado = True
            # Verificar si realmente estaba prestado
            if libro["estado"] == "PRESTADO":
                libro["estado"] = "BIBLIOTECA"
                libro["codigo_estudiante"] = ""
                libro["nombre_estudiante"] = ""
                print("\n EL LIBRO HA SIDO DEVUELTO, CORRECTAMENTE.")
            else:
                print("\n EL LIBRO YA SE ENCONTRABA EN LA BIBLIOTECA.")
    if encontrado == False:
        print("\n EL LIBRO NO EXISTE.")


# SEMANA 2 -> CONSULTAR INVENTARIO
def consultar_inventario(inventario):
    print("\n INVENTARIO ")
    for libro in inventario:
        print("\nNombre libro:", libro["nombre_libro"])
        print("Estado:", libro["estado"])
        # Mostrar datos del estudiante solo si está prestado
        if libro["estado"] == "PRESTADO":
            print("Código estudiante:", libro["codigo_estudiante"])
            print("Nombre estudiante:", libro["nombre_estudiante"])
# MES 1 -> SISTEMA COMPLETO
def SistemaBiblioteca():
    opcion = 0
    while opcion != 4:
        print("      SISTEMA DE BIBLIOTECA")
        print("1. PRESTAR LIBRO")
        print("2. DEVOLVER LIBRO")
        print("3. CONSULTAR INVENTARIO")
        print("4. SALIR")
        opcion = int(input(" SELECCIONE UNA OPCIÓN: "))
        # OPCIÓN 1
        if opcion == 1:
            prestar_libro(inventario)
        # OPCIÓN 2
        elif opcion == 2:
            devolver_libro(inventario)
        # OPCIÓN 3
        elif opcion == 3:
            consultar_inventario(inventario)
        # OPCIÓN 4
        elif opcion == 4:
            print("\n HA SALIDO DEL SISTEMA DE BIBLIOTECA.")
        # OPCIÓN INVÁLIDA
        else:
            print("\n OPCIÓN NO VALIDA.")
# INICIO DEL PROGRAMA
SistemaBiblioteca()