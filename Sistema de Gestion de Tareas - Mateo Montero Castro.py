tareas = []
contadorTareas = 1

def registrarTarea():
    global contadorTareas
    nombre = input("Ingrese el nombre de la tarea: ")
    responsable = input("Ingrese el nombre del responsable: ")
    prioridad = input("Ingrese la prioridad (Alta, Media, Baja): ")
    estado = "Pendiente"
    tarea = [contadorTareas, nombre, responsable, prioridad, estado]
    tareas.append(tarea)
    contadorTareas += 1
    print("Tarea registrada exitosamente.\n")

def actualizarEstado():
    idTarea = int(input("Ingrese el ID de la tarea a actualizar: "))
    for tarea in tareas:
        if tarea[0] == idTarea:
            nuevoEstado = input("Ingrese el nuevo estado (Pendiente, En progreso, Completada): ")
            tarea[4] = nuevoEstado
            print("Estado actualizado correctamente.\n")
            return
    print("Tarea no encontrada.\n")

def listarTareas():
    print("Listado de Tareas:")
    for tarea in tareas:
        print("ID:", tarea[0], "Nombre:", tarea[1], "Responsable:", tarea[2], "Prioridad:", tarea[3], "Estado:", tarea[4])
    print()

def listarPorPrioridad():
    prioridad = input("Ingrese la prioridad a filtrar (Alta, Media, Baja): ")
    print("Tareas con prioridad", prioridad, ":")
    for tarea in tareas:
        if tarea[3] == prioridad:
            print("ID:", tarea[0], "Nombre:", tarea[1], "Responsable:", tarea[2], "Estado:", tarea[4])
    print()

def listarPorResponsable():
    responsable = input("Ingrese el nombre del responsable: ")
    print("Tareas asignadas a", responsable, ":")
    for tarea in tareas:
        if tarea[2] == responsable:
            print("ID:", tarea[0], "Nombre:", tarea[1], "Prioridad:", tarea[3], "Estado:", tarea[4])
    print()

def generarReportes():
    completadas = sum(1 for tarea in tareas if tarea[4].strip().lower() == "completada")
    print("Total de tareas completadas:", completadas, "\n")
    print("Tareas de alta prioridad pendientes:")
    for tarea in tareas:
        if tarea[3].strip().lower() == "alta" and tarea[4].strip().lower() != "completada":
            print("ID:", tarea[0], "Nombre:", tarea[1], "Responsable:", tarea[2], "Estado:", tarea[4])
    print()

def menu():
    while True:
        print("Menú de Gestión de Tareas:")
        print("1. Registrar tarea")
        print("2. Actualizar estado de tarea")
        print("3. Listar todas las tareas")
        print("4. Listar tareas por prioridad")
        print("5. Listar tareas por responsable")
        print("6. Generar reportes")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrarTarea()
        elif opcion == "2":
            actualizarEstado()
        elif opcion == "3":
            listarTareas()
        elif opcion == "4":
            listarPorPrioridad()
        elif opcion == "5":
            listarPorResponsable()
        elif opcion == "6":
            generarReportes()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

menu()
