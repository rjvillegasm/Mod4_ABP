from modulos.cliente import Cliente
from modulos.gestor_clientes import GestorClientes
from modulos.tipos_cliente import ClienteRegular, ClientePremium, ClienteCorporativo

#import tkinter as tk
#from tkinter import messagebox, ttk

def main():
    gestor=GestorClientes()
    
    try:
    
        cliente_uno= ClienteRegular(1, "Ana", "ana@gmail.com",100)
        cliente_dos= ClientePremium(2, "luis", "luis@gmail.com", "Vip")
        cliente_tres=ClienteCorporativo(3, "Tesla","empresat@gmail.com", "Tesla Corp. S.A.")

        gestor.agregar(cliente_uno)
        gestor.agregar(cliente_dos)
        gestor.agregar(cliente_tres)
        
        print("\n-- Lista de clientes--")
        gestor.listar()
        
        print("\n-- Eliminando cliente--")
        gestor.eliminar(1)
        
        print("\n-- Lista actualizada--")
        gestor.listar()
        
        print("\n-- buscar cliente--")
        gestor.obtener_cliente_individual(3)
        #gestor.obtener_cliente_individual(-1)
        gestor.obtener_cliente_individual(0)
                
    except(TypeError, ValueError) as e:
        print(f"Error: {e}")

if __name__=="__main__":
    main()
