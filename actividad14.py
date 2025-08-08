def OrdenarNombre(lista):
    if len(lista) <= 0:
        return lista
    else:
        pivote = lista[0]
        mayores = [x for x in lista[1:] if x[dorsal]["nombre"] > pivote[dorsal]["nombre"]]
        iguales = [x for x in lista if x[dorsal]["nombre"] == pivote[dorsal]["nombre"]]
        menores = [x for x in lista[1:] if x[dorsal]["nombre"] < pivote[dorsal]["nombre"]]
        return OrdenarNombre(menores) + iguales + OrdenarNombre(mayores)
def OrdenarEdad(lista):
    if len(lista) <= 0:
        return lista
    else:
        pivote = lista[0]
        mayores = [x for x in lista[1:] if x[dorsal]["edad"] > pivote[dorsal]["edad"]]
        iguales = [x for x in lista if x[dorsal]["edad"] == pivote[dorsal]["edad"]]
        menores = [x for x in lista[1:] if x[dorsal]["edad"] < pivote[dorsal]["edad"]]
        return OrdenarNombre(menores) + iguales + OrdenarNombre(mayores)
Participante ={}
Participantes = []
while True:
    print("1. Agregar participantes.")
    print("2. Mostrar participantes por nombre.")
    print("3. Mostrar participantes por edad.")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion: "))
    match opcion:
        case 1:
            numParticipantes = int(input("Ingrese la cantidad de participantes: "))
            for i in range(numParticipantes):
                dorsal = int(input("Ingrese el dorsal: "))
                nombre = input("Ingrese nombre: ")
                edad = int(input("Ingrese edad: "))
                categoria = input("Ingrese categoria (juvenil, adulto, máster): ")
                Participante[dorsal] = {
                    "nombre": nombre,
                    "edad": edad,
                    "categoria": categoria,
                }
                Participantes.append(Participante)
                print("Participante agregada exitosamente")

        case 2:
            print("Lista ordenada por nombre de los participantes")
            OrdenadosNombre = OrdenarNombre(Participantes)
            for corredor in OrdenadosNombre:
                for clave, value in corredor.items():
                    print(f"Dorsal: {clave} Nombre: {value["nombre"]} edad: {value['edad']} Categoria: {value['categoria']}")
        case 3:
            print("Lista ordenada por edad de los participantes")
            OrdenadosEdad = OrdenarEdad(Participantes)
            for corredor in OrdenadosEdad:
                for clave, value in corredor.items():
                    print(f"Dorsal: {clave} Nombre: {value["nombre"]} edad: {value['edad']} Categoria: {value['categoria']}")
        case 4:
            print("Saliendo del programa....")
            break
        case 5:
            print("Ingrese una opcion válida")
    if opcion != 4:
        print("Presione ENTER para continuar")