import tkinter as tk
from tkinter import ttk, messagebox
from src.base_datos import iniciar_db
from src.gestor import crear_cliente

# 1. Configuración inicial
iniciar_db() # Asegura que la DB exista al arrancar
ventana = tk.Tk()
ventana.title("GIC - Solution Tech")
ventana.geometry("400x350")

# 2. Campos de entrada
tk.Label(ventana, text="DNI del Cliente:").pack(pady=5)
entry_dni = tk.Entry(ventana)
entry_dni.pack()

tk.Label(ventana, text="Nombre Completo:").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Correo Electrónico:").pack(pady=5)
entry_email = tk.Entry(ventana)
entry_email.pack()

tk.Label(ventana, text="Tipo de Cliente:").pack(pady=5)
combo_tipo = ttk.Combobox(ventana, values=["Regular", "Premium", "Corporativo"])
combo_tipo.current(0) # Seleccionar el primero por defecto
combo_tipo.pack()

# 3. Función del Botón
def boton_guardar():
    rta = crear_cliente(
        entry_dni.get(), 
        entry_nombre.get(), 
        entry_email.get(), 
        combo_tipo.get()
    )
    messagebox.showinfo("Resultado", rta)

tk.Button(ventana, text="REGISTRAR CLIENTE", command=boton_guardar, bg="lightblue").pack(pady=20)

ventana.mainloop()