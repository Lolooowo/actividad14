def OrdenarNombre(lista):
    if len(lista) <= 0:
        return lista
    else:
        pivote = lista[0]
        mayores = [x for x in lista[1:] if x["dorsal"]["nombre"] > pivote]
        iguales = [x for x in lista if x["dorsal"]["nombre"] == pivote]
        menores = [x for x in lista[1:] if x["dorsal"]["nombre"] < pivote]
        return OrdenarNombre(menores) + iguales + OrdenarNombre(mayores)
def OrdenarEdad(lista):
    if len(lista) <= 0:
        return lista
    else:
        pivote = lista[0]
        mayores = [x for x in lista[1:] if x[dorsal]["edad"] > pivote]
        iguales = [x for x in lista if x[dorsal]["edad"] == pivote]
        menores = [x for x in lista[1:] if x[dorsal]["edad"] < pivote]
        return OrdenarNombre(menores) + iguales + OrdenarNombre(mayores)
Participante ={}
Participantes = []
while True:
    print("1. Agregar participantes.")
    print("2. Mostrar participantes por nombre.")
    print("3. Mostrar participantes por edad.")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion"))
    match opcion:
        case 1:
            numParticipantes = int(input("Ingrese la cantidad de participantes"))
            for i in range(numParticipantes):
                dorsal = int(input("Ingrese el dorsal"))
                nombre = input("Ingrese nombre")
                edad = int(input("Ingrese edad"))
                categoria = input("Ingrese categoria (juvenil, adulto, máster)")
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
            for participante in OrdenadosNombre:
                print(f"{participante['nombre']}: con la edad de: {participante["edad"]} está en la categoría: {participante['categoria']}")
        case 3:
            print("Lista ordenada por edad de los participantes")
            OrdenadosEdad = OrdenarEdad(Participantes)
            for participante in OrdenadosEdad:
                print(f"{participante['nombre']}: con la edad de: {participante["edad"]} está en la categoría: {participante['categoria']}")
        case 4:
            print("Saliendo del programa....")
            break
        case 5:
            print("Ingrese una opcion válida")
    if opcion != 4:
        print("Presione ENTER para continuar")