#librerias 
import json
import csv
from tabulate import tabulate


#menu
def MenuInicial():
    while True:
        print("----------------------------")
        print("     Bienvenido Usuario/a   ")
        print(" Restaurante los Pollos hermanos  ")
        print("Opciones.                         ")
        print("1. Ver Menu                       ")
        print("2. Hacer Pedido                   ")
        print("3. cancelar Pedido                ")
        print("4. Modificar Pedido               ")
        print("5. verificar Pedido               ")
        print("6. salir Del Programa             ")
        print("------------------------------")
        eleccion = int(input("cual opcion deseas elegir?"))
        if eleccion == 1:
            print("ingresaste a Ver Menu")
            VerMenu()
        elif eleccion ==2:
            print("Bienvenido ingresaste a hacer pedido que deseas comprar")
            PedidoCliente()
        
        elif eleccion ==3:
            print("")
            CancelarPedido()
        elif eleccion ==4:
            print("")
            modificar_pedido()
        elif eleccion ==5:
            print("")
            VerificarPedido()

        elif eleccion ==6:
            print("Saliendo del Programa......")
            break

#funciones de visualizacion
def VerMenu():
    menu_data = []

    with open("menuPollosHermanos.csv", mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            menu_data.append(row)

    print(tabulate(menu_data, headers="firstrow", tablefmt="grid"))
    
    while True:
        volver = int(input("si deseas volver oprime 0"))
        if volver == 0:
            break



def MenuDelPedido():
    menu_data = []

    with open("menuPollosHermanos.csv", mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            menu_data.append(row)

    print(tabulate(menu_data, headers="firstrow", tablefmt="grid"))

#funcion de hacer pedido 
def PedidoCliente():
    MenuDelPedido()
    carrito = []
    total = 0
    with open("menuPollosHermanos.csv", mode="r", newline="") as file:
        reader = csv.DictReader(file)
        menu = list(reader)
        

    while True:
        pedido = input("Ingrese el nombre del artículo que quiere ordenar (o escriba 'terminar' para finalizar): ").strip()    
        if pedido.lower() == "terminar":
            break

        encontrado = False

        for row in menu:
            if 'nombre' in row and row['nombre'].lower() == pedido.lower():
                precio = int(row['precio'])  # Convertir el precio a entero
                carrito.append({"nombre": row["nombre"], "precio": precio})
                total += precio
                encontrado = True
                break

        if not encontrado:
            print(f"El artículo '{pedido}' no está disponible en el menú.")
    
    pedido_data = {"pedido": carrito, "total": total}
    with open("pedido.json", "w") as json_file:
        json.dump(pedido_data, json_file, indent=4)
    
    print(f"Pedido guardado. Total a pagar: {total}")


#funcion cancelar pedido
def CancelarPedido():
    print("Haz ingresado a cancelar pedido. ¿Qué pedido deseas cancelar?")
    
    try:
        with open("pedido.json", "r") as file:
            data = json.load(file)
        
        carrito = data.get("pedido", [])
        total = data.get("total", 0)

        if not carrito:
            print("No hay pedidos por cancelar.")
            return

        for index, item in enumerate(carrito):
            print(f"{index + 1}. {item['nombre']}: ${item['precio']}")

        try:
            eliminar = int(input("Ingrese el número del artículo que desea eliminar: ")) - 1
            if 0 <= eliminar < len(carrito):
                item_eliminado = carrito.pop(eliminar)
                total -= item_eliminado['precio']
                print(f"Artículo '{item_eliminado['nombre']}' eliminado.")
            else:
                print("Número de artículo inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
        
        # Actualiza el archivo JSON con el pedido actualizado y el nuevo total
        pedido_actualizado = {"pedido": carrito, "total": total}
        with open("pedido.json", "w") as file:
            json.dump(pedido_actualizado, file, indent=4)

        print("El pedido ha sido actualizado.")

    except FileNotFoundError:
        print("El archivo JSON no está creado.")
    except json.JSONDecodeError:
        print("Archivo JSON corrompido.")
    


#verificar pedido
def VerificarPedido():
    print("Haz ingresado a cancelar pedido que pedido deseas cancelar")
    try:
        with open("pedido.json", "r") as file:
            data = json.load(file)
        
        if not data:
            print("no hay pedidos por Cancelar")
        else:
            for key, value in data.items():
                print(f"{key}:{value}")
    except FileNotFoundError:
        print("el archivo json no esta creado")
    except json.JSONDecodeError:
        print("archivo json corrompido")


#funcion modificar pedido
def modificar_pedido():
    archivo_pedidos = "pedido.json"

    try:
        with open(archivo_pedidos, 'r') as file:
            pedidos = json.load(file)
    except FileNotFoundError:
        print(f"Archivo '{archivo_pedidos}' no encontrado.")
        return
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON '{archivo_pedidos}'.")
        return

    if "pedido" not in pedidos or not pedidos["pedido"]:
        print("No hay pedidos para modificar.")
        return

    # Mostrar los pedidos numerados
    for idx, pedido in enumerate(pedidos["pedido"], start=1):
        print(f'{idx}. Nombre: {pedido["nombre"]}, Precio: {pedido["precio"]}')

    try:
        seleccion = int(input("Seleccione el número del pedido que desea modificar: ")) - 1
        if 0 <= seleccion < len(pedidos["pedido"]):
            nuevo_nombre = input("Ingrese el nuevo nombre del artículo: ")

            # Modificar el pedido seleccionado
            pedidos["pedido"][seleccion]["nombre"] = nuevo_nombre

            # Guardar los cambios en el archivo JSON
            with open(archivo_pedidos, 'w') as file:
                json.dump(pedidos, file, indent=4)
            print("Pedido modificado exitosamente.")
        else:
            print("Selección inválida.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número para seleccionar el pedido.")





#llamamos a la funcion madre
MenuInicial()