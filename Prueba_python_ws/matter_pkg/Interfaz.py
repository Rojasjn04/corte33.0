import tkinter as tk

def explorar_entorno():
    print("Iniciando exploración del entorno...")
    estado_actual.set("Explorando")

def cambiar_categoria():
    print("Cambiando categoría de objetos...")
    estado_actual.set("Cambiando categoría")

def soltar_objeto():
    print("Objeto soltado...")
    estado_actual.set("Objeto soltado")

def mover_objeto():
    print("Objeto movido...")
    estado_actual.set("Moviendo objeto")

def no_llega_objeto():
    print("No se llegó a la posición del objeto...")
    estado_actual.set("No llega objeto")

def parada_emergencia():
    print("Se activó la parada de emergencia...")
    estado_actual.set("Parada de emergencia")

def continuar():
    print("Se presionó el botón de continuar...")
    estado_actual.set("Continuar")

def start():
    print("Se presionó el botón de start...")
    estado_actual.set("Start")

def llegar_contenedor():
    print("Se llegó a la posición del contenedor...")
    estado_actual.set("Llegar al contenedor")

def cambio_categoria_lata_botella():
    print("Se cambió la categoría de lata a botella...")
    estado_actual.set("Cambio de categoría (Lata a Botella)")

def no_objetos_reciclables():
    print("No hay más objetos reciclables...")
    estado_actual.set("No hay objetos reciclables")

def camara_desconectada():
    print("La cámara se desconectó...")
    estado_actual.set("Cámara desconectada")

def no_agarra_objeto():
    print("El robot no logra agarrar el objeto...")
    estado_actual.set("No se pudo agarrar el objeto")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz de Robot Manipulador")
ventana.geometry("400x400")

# Variable para almacenar el estado actual del robot
estado_actual = tk.StringVar()
estado_actual.set("Idle")

# Crear el frame principal
frame_principal = tk.Frame(ventana, bg="#F0F0F0")
frame_principal.pack(pady=20)

# Crear el frame de exploración
frame_exploracion = tk.Frame(frame_principal, bg="#E8F6FF")
frame_exploracion.pack(pady=10)

lbl_explorar = tk.Label(frame_exploracion, text="Explorar Entorno", font=("Arial", 14), bg="#E8F6FF")
lbl_explorar.pack(pady=5)

btn_explorar = tk.Button(frame_exploracion, text="Explorar", font=("Arial", 10), bg="#FFD700", fg="#FFFFFF", relief=tk.RAISED, width=10, command=explorar_entorno)
btn_explorar.pack(pady=5)

# Crear el frame de cambio de categoría
frame_cambio_categoria = tk.Frame(frame_principal, bg="#FFF9E5")
frame_cambio_categoria.pack(pady=10)

lbl_cambiar_categoria = tk.Label(frame_cambio_categoria, text="Cambiar Categoría de Objetos", font=("Arial", 14), bg="#FFF9E5")
lbl_cambiar_categoria.pack(pady=5)

btn_cambiar_categoria = tk.Button(frame_cambio_categoria, text="Cambiar Categoría", font=("Arial", 10), bg="#FF7F50", fg="#FFFFFF", relief=tk.RAISED, width=10, command=cambiar_categoria)
btn_cambiar_categoria.pack(pady=5)

# Crear el frame de simulación de eventos
frame_simulacion = tk.Frame(frame_principal, bg="#E0FFFF")
frame_simulacion.pack(pady=10)

lbl_simulacion = tk.Label(frame_simulacion, text="Simulación de Eventos", font=("Arial", 14), bg="#E0FFFF")
lbl_simulacion.pack(pady=5)

btn_soltar_objeto = tk.Button(frame_simulacion, text="Soltar Objeto", font=("Arial", 10), bg="#90EE90", relief=tk.RAISED, width=10, command=soltar_objeto)
btn_soltar_objeto.pack(pady=2)

btn_mover_objeto = tk.Button(frame_simulacion, text="Mover Objeto", font=("Arial", 10), bg="#FFA07A", relief=tk.RAISED, width=10, command=mover_objeto)
btn_mover_objeto.pack(pady=2)

btn_no_llega_objeto = tk.Button(frame_simulacion, text="No Llega Objeto", font=("Arial", 10), bg="#FF4500", relief=tk.RAISED, width=10, command=no_llega_objeto)
btn_no_llega_objeto.pack(pady=2)

btn_parada_emergencia = tk.Button(frame_simulacion, text="Parada de Emergencia", font=("Arial", 10), bg="#DC143C", relief=tk.RAISED, width=10, command=parada_emergencia)
btn_parada_emergencia.pack(pady=2)

btn_continuar = tk.Button(frame_simulacion, text="Continuar", font=("Arial", 10), bg="#4682B4", relief=tk.RAISED, width=10, command=continuar)
btn_continuar.pack(pady=2)

btn_start = tk.Button(frame_simulacion, text="Start", font=("Arial", 10), bg="#3CB371", relief=tk.RAISED, width=10, command=start)
btn_start.pack(pady=2)

btn_llegar_contenedor = tk.Button(frame_simulacion, text="Llegar al Contenedor", font=("Arial", 10), bg="#1E90FF", relief=tk.RAISED, width=10, command=llegar_contenedor)
btn_llegar_contenedor.pack(pady=2)

btn_cambio_categoria_lata_botella = tk.Button(frame_simulacion, text="Cambio Categoría (Lata a Botella)", font=("Arial", 10), bg="#9932CC", relief=tk.RAISED, width=10, command=cambio_categoria_lata_botella)
btn_cambio_categoria_lata_botella.pack(pady=2)

btn_no_objetos_reciclables = tk.Button(frame_simulacion, text="No hay Objetos Reciclables", font=("Arial", 10), bg="#FF8C00", relief=tk.RAISED, width=10, command=no_objetos_reciclables)
btn_no_objetos_reciclables.pack(pady=2)

btn_camara_desconectada = tk.Button(frame_simulacion, text="Cámara Desconectada", font=("Arial", 10), bg="#FF1493", relief=tk.RAISED, width=10, command=camara_desconectada)
btn_camara_desconectada.pack(pady=2)

btn_no_agarra_objeto = tk.Button(frame_simulacion, text="No se Agarra Objeto", font=("Arial", 10), bg="#8B0000", relief=tk.RAISED, width=10, command=no_agarra_objeto)
btn_no_agarra_objeto.pack(pady=2)

# Crear el frame de estado actual
frame_estado_actual = tk.Frame(frame_principal, bg="#FFFACD")
frame_estado_actual.pack(pady=10)

lbl_estado_actual = tk.Label(frame_estado_actual, text="Estado Actual del Robot", font=("Arial", 14), bg="#FFFACD")
lbl_estado_actual.pack(pady=5)

lbl_estado = tk.Label(frame_estado_actual, textvariable=estado_actual, font=("Arial", 12), bg="#FFFACD")
lbl_estado.pack(pady=5)

# Ejecutar el bucle principal de la interfaz
ventana.mainloop()

