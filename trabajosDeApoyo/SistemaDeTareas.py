print("buenas me puedes decir tu nombre?")
nombre=input(" ")
print(f"hola como estas {nombre} en que te puedo ayudar ")
lista_de_tareas = []
while True:
    print("1. guardar tareas pendientes")
    print("2. verificar tareas pendientes")
    print("3. eliminar tareas pendientes")
    respuesta = int(input("cual deseas de las 2 "))
    if respuesta == 1:
        print("elegiste guardar tareas pendientes")
        tarea = input("agrega una tarea para la lista")
        lista_de_tareas.append(tarea)
        print("Tarea agregada a la lista.")

    elif respuesta == 2:
        print("elegiste verificar tareas pendientes")
        if not lista_de_tareas:
            print("No hay tareas pendientes")
        else:
            print("Tareas pendientes:")
            for i, tarea in enumerate(lista_de_tareas,start=1):
                print(f"{i} {tarea}")
    elif respuesta == 3:
        print("haz elegido eleminar tarea")
        if not lista_de_tareas:
            print("no hay tareas por eliminar")
        else:
            for i, tarea in enumerate(lista_de_tareas, start=1):
                print(f"{i}{tarea}")
            eliminar = int(input("que tarea deseas eliminar si deseas cancelar escribe 0 "))
            if eliminar == 0:
                break
            elif 1 <=  eliminar <= len(lista_de_tareas):
                lista_de_tareas.pop(eliminar -1)
                print("tarea eliminada")
        

