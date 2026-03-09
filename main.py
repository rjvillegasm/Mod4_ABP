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
    
    # Widget combobox para seleccionar tipo de clienete
    tipo_combo = ttk.Combobox(ventana,
                                textvariable=tipo_var, 
                                values=["Regular", "Premium", "Corporativo"])
    tipo_combo.bind("<<ComboboxSelected>>", seleccionar_tipo)
    tipo_combo.pack()
    
    # Widget para agregar clientes
    tk.Label(ventana, text="ID:").pack()
    entrada_id = tk.Entry(ventana)
    entrada_id.pack()
    
    tk.Label(ventana, text="Nombre:").pack()
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.pack()
    
    tk.Label(ventana, text="Email:").pack()
    entrada_email = tk.Entry(ventana)
    entrada_email.pack()
    
    tk.Label(ventana, text="Puntos:").pack()
    entrada_puntos = tk.Entry(ventana)
    entrada_puntos.pack()
    
    tk.Label(ventana, text="Membresía:").pack()
    entrada_membresia = tk.Entry(ventana)
    entrada_membresia.pack()
    
    tk.Label(ventana, text="Empresa:").pack()
    entrada_empresa = tk.Entry(ventana)
    entrada_empresa.pack()
    
    seleccionar_tipo(None)
    
    
    # Botones
    tk.Button(ventana, text="Agregar Cliente", command=agregar_cliente).pack()
    
    
    
    
    # Bucle de la app
    ventana.mainloop()
