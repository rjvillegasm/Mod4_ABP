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
        
def listar_clientes():
    
    for item in tree.get_children():
        tree.delete(item)
    
    for cliente in gestor.obtener_todos():
        tipo = type(cliente).__name__.replace('Cliente', '')
        
        # Determinar detalle según tipo
        if tipo == "Regular":
            detalle = f"Puntos: {cliente.get_puntos()}"
        elif tipo == "Premium":
            detalle = f"Membresía: {cliente.get_membresia()}"
        elif tipo == "Corporativo":  
            detalle = f"Empresa: {cliente.get_empresa()}"
        
        
        tree.insert("", "end", values=(
            cliente.get_id(),
            cliente.get_nombre(), 
            cliente.get_email(),
            tipo,
            detalle
        )) 

def borrar_cliente():
    seleccionar_cliente= tree.selection()
    if seleccionar_cliente:
        item=tree.item(seleccionar_cliente[0])
        cliente_id= item['values'][0]
        gestor.eliminar(cliente_id)
        listar_clientes()

def busqueda_individual():
    try:
        id_cliente = int(entrada_buscar_id.get())
        cliente = gestor.obtener_cliente_individual(id_cliente)
        
        if cliente:
            tipo = type(cliente).__name__.replace('Cliente', '')
            if tipo == "Regular":
                detalle = f"Puntos: {cliente.get_puntos()}"
            elif tipo == "Premium":
                detalle = f"Membresía: {cliente.get_membresia()}"
            else:
                detalle = f"Empresa: {cliente.get_empresa()}"
            
            resultado_label.config(
                text=f"ID: {cliente.get_id()} | Nombre: {cliente.get_nombre()} | Email: {cliente.get_email()} | Tipo: {tipo} | {detalle}"
            )
        else:
            resultado_label.config(text="Cliente no encontrado", fg="red")
            
        entrada_buscar_id.delete(0, tk.END)
    except ValueError:
        resultado_label.config(text="ID inválido", fg="red")
    
    
# Inicialización
if __name__=="__main__":
    
    
    
    # Ventana principal
    ventana=tk.Tk()
    ventana.title("Gestor de clientes")
    ventana.geometry("900x1000")
    
    # Variables
    gestor=GestorClientes()
    tipo_var=tk.StringVar()
    
    #Widgets
    
    # Widget combobox para seleccionar tipo de cliente
    
    #título del formulario
    tk.Label(ventana, text="Crear clientes ", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10, sticky="w")
    
    tk.Label(ventana, text="Tipo Cliente:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    tipo_combo = ttk.Combobox(ventana, textvariable=tipo_var, values=["Regular", "Premium", "Corporativo"])
    tipo_combo.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    tipo_combo.bind("<<ComboboxSelected>>", seleccionar_tipo)

    # Widgets para agregar clientes
    tk.Label(ventana, text="ID:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entrada_id = tk.Entry(ventana)
    entrada_id.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Nombre:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Email:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    entrada_email = tk.Entry(ventana)
    entrada_email.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Puntos:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
    entrada_puntos = tk.Entry(ventana)
    entrada_puntos.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Membresía:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
    entrada_membresia = tk.Entry(ventana)
    entrada_membresia.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Empresa:").grid(row=7, column=0, padx=5, pady=5, sticky="e")
    entrada_empresa = tk.Entry(ventana)
    entrada_empresa.grid(row=7, column=1, padx=5, pady=5, sticky="w")
    
    seleccionar_tipo(None)
    
    # Boton agregar cliente
    tk.Button(ventana, text="Agregar Cliente", command=agregar_cliente).grid(row=8, column=1, columnspan=2, pady=10, sticky="w")
    
    # título del Treeview 
    
    tk.Label(ventana, text="Lista de clientes", font=("Arial", 12, "bold")).grid(row=9, column=0, columnspan=2, pady=10, sticky="w")
    

    # Frame para el treeview y scrollbar
    frame_tree = tk.Frame(ventana)
    frame_tree.grid(row=10, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    # Scrollbar 
    scrollbar = tk.Scrollbar(frame_tree)
    scrollbar.pack(side="right", fill="y")

    # Treeview
    tree = ttk.Treeview(frame_tree, 
                        columns=("ID", "Nombre", "Email", "Tipo", "Detalle"), 
                        show="headings",
                        yscrollcommand=scrollbar.set,
                        height=8)

    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Email", text="Email")
    tree.heading("Tipo", text="Tipo")
    tree.heading("Detalle", text = "Detalle")

    tree.column("ID", width=80)
    tree.column("Nombre", width=150)
    tree.column("Email", width=200)
    tree.column("Tipo", width=100)
    tree.column("Detalle", width=100)

    tree.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=tree.yview)
        
    # Boton listar_clientes
    
    tk.Button(ventana, text="Actualizar Lista", command=listar_clientes).grid(row=11, column=0, columnspan=2, pady=15, sticky="w")
    # Boton eliminar cliente 
    tk.Button(ventana, text="Eliminar Cliente", command=borrar_cliente).grid(row=11, column=1, columnspan=2, pady=15, sticky="e")
    
    # Widget para buscar clientes individualmente
    
    tk.Label(ventana, text="Busqueda individual", font=("Arial", 12, "bold")).grid(row=12, column=0, columnspan=2, pady=10, sticky="w")
    
    tk.Label(ventana, text="Buscar por ID:").grid(row=13, column=0, padx=5, pady=5, sticky="w")
    entrada_buscar_id = tk.Entry(ventana)
    entrada_buscar_id.grid(row=13, column=1, padx=5, pady=5)
    
    # Boton buscar
    
    tk.Button(ventana, text="Buscar Cliente", command=busqueda_individual).grid(row=13, column=2, padx=5, pady=5, sticky="e")
    
    # Label para mostar resultado
    
    resultado_label = tk.Label(ventana, text="", fg="blue")
    resultado_label.grid(row=14, column=0, columnspan=3, pady=5)
    
    # Bucle de la app
    ventana.mainloop()
