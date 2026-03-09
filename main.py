from modulos.cliente import Cliente
from modulos.gestor_clientes import GestorClientes
from modulos.tipos_cliente import ClienteRegular, ClientePremium, ClienteCorporativo

import tkinter as tk
from tkinter import messagebox, ttk

# Métodos

def agregar_cliente():
    id= entrada_id.get()
    nombre = entrada_nombre.get()
    email = entrada_email.get()
    tipo = tipo_var.get()
    puntos=entrada_puntos.get()
    membresia=entrada_membresia.get()
    empresa=entrada_empresa.get()     
    
    if tipo == "Regular":
        cliente = ClienteRegular(id, nombre, email, puntos)
    elif tipo == "Premium":
        cliente = ClientePremium(id, nombre, email, membresia)
    elif tipo =="Corporativo":  
        cliente = ClienteCorporativo(id, nombre, email, empresa)
    
    gestor.agregar(cliente)
    
    entrada_id.delete(0,tk.END)
    entrada_nombre.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_puntos.delete(0, tk.END)
    entrada_membresia.delete(0, tk.END)
    entrada_empresa.delete(0, tk.END)

def seleccionar_tipo(tipo_cliente):
    tipo = tipo_var.get()
        
    entrada_puntos.config(state="disabled")
    entrada_membresia.config(state="disabled")
    entrada_empresa.config(state="disabled")
    
    
    if tipo == "Regular":
        entrada_puntos.config(state="normal")
    elif tipo == "Premium":
        entrada_membresia.config(state="normal")
    elif tipo == "Corporativo":
        entrada_empresa.config(state="normal")

# Inicialización
if __name__=="__main__":
    
    
    
    # Ventana principal
    ventana=tk.Tk()
    ventana.title("Gestor de clientes")
    ventana.geometry("500x700")
    
    # Variables
    gestor=GestorClientes()
    tipo_var=tk.StringVar()
    
    #Widgets
    
    # Widget combobox para seleccionar tipo de cliente
    tk.Label(ventana, text="Tipo Cliente:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    tipo_combo = ttk.Combobox(ventana, textvariable=tipo_var, values=["Regular", "Premium", "Corporativo"])
    tipo_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    tipo_combo.bind("<<ComboboxSelected>>", seleccionar_tipo)

    # Widgets para agregar clientes
    tk.Label(ventana, text="ID:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entrada_id = tk.Entry(ventana)
    entrada_id.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Nombre:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Email:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    entrada_email = tk.Entry(ventana)
    entrada_email.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Puntos:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    entrada_puntos = tk.Entry(ventana)
    entrada_puntos.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Membresía:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
    entrada_membresia = tk.Entry(ventana)
    entrada_membresia.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Empresa:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
    entrada_empresa = tk.Entry(ventana)
    entrada_empresa.grid(row=6, column=1, padx=5, pady=5, sticky="w")
    
    seleccionar_tipo(None)
    
    
    # Botones
    tk.Button(ventana, text="Agregar Cliente", command=agregar_cliente).grid(row=7, column=1, columnspan=2, pady=10)
    
    
    
    
    # Bucle de la app
    ventana.mainloop()
