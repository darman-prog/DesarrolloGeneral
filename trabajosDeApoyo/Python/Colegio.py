import tkinter as tk
from tkinter import messagebox , simpledialog
from tkinter import ttk
import json

#creacion del main
# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Gestión Escolar")
root.geometry("700x400")

# Título de la ventana
titulo_label = tk.Label(root, text="Sistema de Gestión Escolar", font=("Helvetica", 16))
titulo_label.pack(pady=20)


# Funciones para los diferentes apartados
#funcion para registrar estudiante
def mostrar_registro_estudiantes():
    label.config(text="Registro de Estudiantes")
    limpiar_area_contenido()
    # Contenedor Frame para los inputs
    global contenedor_frame
    contenedor_frame = tk.Frame(area_contenido)
    contenedor_frame.pack(pady=20)

    # Etiquetas y campos de entrada dentro del Frame
    nombre_label = tk.Label(contenedor_frame, text="Nombre del Estudiante:")
    nombre_label.pack(pady=5)
    global nombre_entry
    nombre_entry = tk.Entry(contenedor_frame)
    nombre_entry.pack(pady=5)

    edad_label = tk.Label(contenedor_frame, text="Edad del Estudiante:")
    edad_label.pack(pady=5)
    global edad_entry
    edad_entry = tk.Entry(contenedor_frame)
    edad_entry.pack(pady=5)

    grado_label = tk.Label(contenedor_frame, text="Grado del Estudiante:")
    grado_label.pack(pady=5)
    global grado_entry
    grado_entry = tk.Entry(contenedor_frame)
    grado_entry.pack(pady=5)

    # Botón para agregar estudiante
    agregar_button = tk.Button(contenedor_frame, text="Agregar Estudiante", command= agregar_estudiante)
    agregar_button.pack(pady=10)

    # Etiqueta para mostrar mensajes
    global mensaje_label
    mensaje_label = tk.Label(contenedor_frame, text="")
    mensaje_label.pack(pady=10)


#Logica de Registro de estudiante
def agregar_estudiante():
    nombre = nombre_entry.get()
    edad = int(edad_entry.get())
    grado = int(grado_entry.get())

    # Leer el archivo JSON existente
    try:
        with open("estudiantes2.json", "r") as file:
            estudiantes = json.load(file)
    except FileNotFoundError:
        estudiantes = []

    # Crear un diccionario con la información del nuevo estudiante
    nuevo_estudiante = {
        "nombre": nombre,
        "edad": edad,
        "grado": grado
    }

    # Agregar el nuevo estudiante a la lista
    estudiantes.append(nuevo_estudiante)

    # Escribir la lista actualizada de estudiantes en el archivo JSON
    with open("estudiantes2.json", "w") as file:
        json.dump(estudiantes, file, indent=4)

    # Limpiar los campos de entrada después de agregar
    nombre_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    grado_entry.delete(0, tk.END)

    # Mostrar mensaje de confirmación
    mensaje_label.config(text=f"Estudiante {nombre} agregado correctamente.")


#registrar profesores
def mostrar_registro_profesores():
    label.config(text="Registro de Profesores")
    limpiar_area_contenido()
    # Contenedor Frame para los inputs
    global contenedor_frame_profesores
    contenedor_frame_profesores = tk.Frame(area_contenido)
    contenedor_frame_profesores.pack(pady=20)

    # Etiquetas y campos de entrada dentro del Frame
    nombre_profesor_label = tk.Label(contenedor_frame_profesores, text="Nombre del Profesor:")
    nombre_profesor_label.pack(pady=5)
    global nombre_profesor_entry
    nombre_profesor_entry = tk.Entry(contenedor_frame_profesores)
    nombre_profesor_entry.pack(pady=5)

    materia_profesor_label = tk.Label(contenedor_frame_profesores, text=" Asignatura del Profesor: ")
    materia_profesor_label.pack(pady=5)
    global materia_profesor_entry
    materia_profesor_entry = tk.Entry(contenedor_frame_profesores)
    materia_profesor_entry.pack(pady=5)

    salon_profesor_label = tk.Label(contenedor_frame_profesores, text=" Grado del profesor: ")
    salon_profesor_label.pack(pady=5)
    global salon_profesor_entry
    salon_profesor_entry = tk.Entry(contenedor_frame_profesores)
    salon_profesor_entry.pack(pady=5)

    # Botón para agregar profesor
    agregar_profesor_button = tk.Button(contenedor_frame_profesores, text="Agregar Profesor", command= agregar_profesor)
    agregar_profesor_button.pack(pady=10)

    # Etiqueta para mostrar mensajes
    global mensaje_profesor_label
    mensaje_profesor_label = tk.Label(contenedor_frame_profesores, text="")
    mensaje_profesor_label.pack(pady=10)

#logica para registrar profesores
def agregar_profesor():
    nombre = nombre_profesor_entry.get()
    materia = materia_profesor_entry.get()
    salon = salon_profesor_entry.get()
    # Grado = int(grado_profesor_entry.get())

    # Leer el archivo JSON existente
    try:
        with open("profesores.json", "r") as file:
            profesores = json.load(file)
    except FileNotFoundError:
        profesores = []

    # Crear un diccionario con la información del nuevo profesor
    nuevo_profesor = {
        "nombre": nombre,
        "materia": materia,
        "salon": salon
    }

    # Agregar el nuevo profesor a la lista
    profesores.append(nuevo_profesor)

    # Escribir la lista actualizada de profesores en el archivo JSON
    with open("profesores.json", "w") as file:
        json.dump(profesores, file, indent=4)

    # Limpiar los campos de entrada después de agregar
    nombre_profesor_entry.delete(0, tk.END)
    materia_profesor_entry.delete(0, tk.END)
    salon_profesor_entry.delete(0, tk.END)

    # Mostrar mensaje de confirmación
    mensaje_profesor_label.config(text=f"Profesor {nombre} agregado correctamente.")


# Función para cargar profesores desde el archivo JSON
def cargar_profesores():
    with open('profesores.json', 'r') as f:
        return json.load(f)
#mostrar_profesores
def Listado_Profesores():
    profesores = cargar_profesores()
    
    # Crear la ventana de listado de profesores
    ventana_profesores = tk.Toplevel(root)
    ventana_profesores.title("Listado de Profesores")
    ventana_profesores.geometry("600x400")
    
    # Crear un frame contenedor con scroll
    contenedor_scroll = tk.Frame(ventana_profesores)
    contenedor_scroll.pack(fill=tk.BOTH, expand=True)
    
    canvas = tk.Canvas(contenedor_scroll)
    scrollbar = tk.Scrollbar(contenedor_scroll, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    cursos = {f"Grado {i}": [] for i in range(1, 12)}
    
    for profesor in profesores:
        cursos[profesor['salon']].append(profesor)
    
    for curso, profesores in cursos.items():
        frame_curso = tk.Frame(scrollable_frame)
        frame_curso.pack(pady=10, anchor="w")
        
        titulo_curso = tk.Label(frame_curso, text=f"{curso}", font=("Helvetica", 14))
        titulo_curso.pack(anchor="w")
        
        texto_profesores = tk.Text(frame_curso, height=5, width=50, state=tk.NORMAL)
        for profesor in profesores:
            texto_profesores.insert(tk.END, f"Nombre: {profesor['nombre']}, Materia: {profesor['materia']}\n")
        texto_profesores.config(state=tk.DISABLED)
        texto_profesores.pack(anchor="w")

#limpiar contenido de la ventana
def limpiar_area_contenido():
    for widget in area_contenido.winfo_children():
        widget.destroy()

#mostrar cursos
def mostrar_cursos():
    label.config(text="Estudiantes")
    limpiar_area_contenido()
    # Crear un nuevo canvas y scrollbar
    global canvas, scrollbar
    canvas = tk.Canvas(area_contenido)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(area_contenido, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")
    canvas.config(yscrollcommand=scrollbar.set)

    # Abrir el archivo JSON y cargar los estudiantes
    with open("estudiantes2.json", "r") as file:
        estudiantes = json.load(file)

    # Crear un diccionario para agrupar estudiantes por grado
    estudiantes_por_grado = {grado: [] for grado in range(1, 12)}
    for estudiante in estudiantes:
        estudiantes_por_grado[estudiante["grado"]].append(estudiante)
    
    # Crear un Frame dentro del canvas para agregar los estudiantes
    frame_interno = tk.Frame(canvas)
    frame_interno.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=frame_interno, anchor='nw')

    # Mostrar los estudiantes por grado
    for grado in range(1, 12):
        frame_grado = tk.Frame(frame_interno)
        frame_grado.pack(pady=10, anchor="w")
        titulo_grado = tk.Label(frame_grado, text=f"grado {grado}", font=("Helvetica", 14))
        titulo_grado.pack(anchor="w")
        texto_estudiantes = tk.Text(frame_grado, height=5, width=50, state=tk.NORMAL)
        for estudiante in estudiantes_por_grado[grado]:
            texto_estudiantes.insert(tk.END, f"nombre: {estudiante['nombre']}, edad: {estudiante['edad']}, grado: {estudiante['grado']}\n")
        texto_estudiantes.config(state=tk.DISABLED)
        texto_estudiantes.pack(anchor="w")


def cargar_estudiantes():
    with open('estudiantes.json', 'r') as f:
        return json.load(f)

# Función para mostrar las notas del estudiante
def mostrar_estudiante(estudiante_nombre, estudiantes):
    estudiante = next((s for s in estudiantes if s['nombre'] == estudiante_nombre), None)
    if estudiante:
        grades_message = '\n'.join([f"{subject}: {grade}" for subject, grade in estudiante['notas'].items()])
        messagebox.showinfo("Notas del Estudiante", f"Nombre: {estudiante['nombre']}\nEdad: {estudiante['edad']}\nGrado: {estudiante['grado']}\n\nNotas:\n{grades_message}")
    else:
        messagebox.showerror("Error", "Estudiante no encontrado")

# Función para solicitar el nombre del estudiante
def nuevo_estudiante(estudiantes):
    estudiante_nombre = simpledialog.askstring("Entrada de Nombre", "Ingrese el nombre del estudiante:")
    if estudiante_nombre:
        mostrar_estudiante(estudiante_nombre, estudiantes)

# Función para mostrar calificaciones en la ventana de calificaciones
def mostrar_calificaciones():
    estudiantes = cargar_estudiantes()
    
    ventana_calificaciones = tk.Toplevel(root)
    ventana_calificaciones.title("Gestión de Calificaciones")
    ventana_calificaciones.geometry("800x600")
    
    label = tk.Label(ventana_calificaciones, text="Gestión de Calificaciones")
    label.pack(pady=10)
    
    # Crear un frame contenedor con scroll
    contenedor_scroll = tk.Frame(ventana_calificaciones)
    contenedor_scroll.pack(fill=tk.BOTH, expand=True)
    
    canvas = tk.Canvas(contenedor_scroll)
    scrollbar = tk.Scrollbar(contenedor_scroll, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    cursos = {grado: [] for grado in range(1, 12)}
    
    for estudiante in estudiantes:
        cursos[estudiante['grado']].append(estudiante)
    
    for grado, estudiantes_en_grado in cursos.items():
        frame_grado = tk.Frame(scrollable_frame)
        frame_grado.pack(pady=10, anchor="w")
        titulo_grado = tk.Label(frame_grado, text=f"Grado {grado}", font=("Helvetica", 14))
        titulo_grado.pack(anchor="w")
        texto_estudiantes = tk.Text(frame_grado, height=10, width=70, state=tk.NORMAL)
        for estudiante in estudiantes_en_grado:
            texto_estudiantes.insert(tk.END, f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}\n")
            for materia, nota in estudiante['notas'].items():
                texto_estudiantes.insert(tk.END, f"  {materia}: {nota}\n")
        texto_estudiantes.config(state=tk.DISABLED)
        texto_estudiantes.pack(anchor="w")
    
    # Botón para ingresar el nombre del estudiante
    btn_prompt_name = tk.Button(ventana_calificaciones, text="Mostrar Notas del Estudiante", command=lambda: nuevo_estudiante(estudiantes))
    btn_prompt_name.pack(pady=20)    

# Área de contenido dinámico
area_contenido = tk.Frame(root)
area_contenido.pack(pady=10, fill=tk.BOTH, expand=True)

#para verificar lo seleccionado
label = tk.Label(root, text="", font=("Helvetica", 12))
label.pack(pady=20 )

# Menú
menu_bar = tk.Menu(root)

# Menú Estudiantes
estudiantes_menu = tk.Menu(menu_bar, tearoff=0)
estudiantes_menu.add_command(label="Registro de Estudiantes", command=mostrar_registro_estudiantes)
menu_bar.add_cascade(label="Estudiantes", menu=estudiantes_menu)


# Menú Profesores
profesores_menu = tk.Menu(menu_bar, tearoff=0)
profesores_menu.add_command(label="Registro de Profesores", command=mostrar_registro_profesores)
menu_bar.add_cascade(label="Profesores", menu=profesores_menu)

# Menú Cursos
cursos_menu = tk.Menu(menu_bar, tearoff=0)
cursos_menu.add_command(label="Estudiantes Activos", command=mostrar_cursos)
menu_bar.add_cascade(label="Cursos", menu=cursos_menu)

# Menú Calificaciones
calificaciones_menu = tk.Menu(menu_bar, tearoff=0)
calificaciones_menu.add_command(label="Gestión de Calificaciones", command=mostrar_calificaciones)
menu_bar.add_cascade(label="Calificaciones", menu=calificaciones_menu)

#Listado de profesores
Listado_profesores = tk.Menu(menu_bar, tearoff=0)
Listado_profesores.add_command(label="Listado de profesores activos", command=Listado_Profesores)
menu_bar.add_cascade(label="Profesores",menu=Listado_profesores)

# Configurar el menú en la ventana principal
root.config(menu=menu_bar)

# Etiqueta para mostrar el apartado seleccionado
label = tk.Label(root, text="", font=("Helvetica", 12))
label.pack(pady=20)

# Iniciar el bucle principal de la ventana
root.mainloop()



