
import csv
from modulos.tipos_cliente import ClienteRegular, ClientePremium, ClienteCorporativo

class GestorClientes:
    def __init__(self):
        self.__clientes=[]    
        self.cargar_desde_archivo()
        
        
    #Función para agregar clientes
    #Valida que el no esté vacío y el ID no se repita 
    def agregar(self, cliente):
        if cliente is None:
            raise ValueError("No se puede agregar un cliente vacío")
        if self.buscar(cliente.get_id()):
            raise ValueError("Ya existe cliente con ese ID")
        
        self.__clientes.append(cliente)
        self.guardar_en_archivo()
    
    #Función que lista los clienters registrados
    #Valida que no esten vacíos y utiliza método especial __str__    
    def listar(self):
        if not self.__clientes:
            raise ValueError("No hay clientes registrados")
        
        for cliente in self.__clientes:
            print(f"{cliente} - Descuento: {cliente.calcular_descuento()}")

    # Función para buscar un cliente por su ID
    # Valida que ID sea entero y no negativo
    def buscar(self, id_cliente):
        if not isinstance(id_cliente, int):
            raise TypeError("El id a buscar debe ser entero")
        if id_cliente<=0:
            raise ValueError("El ID deber ser un valor posistivo")
        
        for cliente in self.__clientes:
            if cliente.get_id()== id_cliente:
                return cliente
        return None
    
    # Función para eliminar clientes
    # Valida que ID sea entero y no negativo
    def eliminar(self, id_cliente):
        
        if not isinstance(id_cliente, int):
            raise TypeError("El id a eliminar debe ser entero")
        if id_cliente<=0:
            raise ValueError("El ID deber ser un valor positivo")
        cliente = self.buscar(id_cliente)
        
        if cliente is None:
            raise ValueError("Cliente no encontrado")
        
        nueva_lista= []
        for cliente in self.__clientes:
            if cliente.get_id() != id_cliente:
                nueva_lista.append(cliente)
                
        self.__clientes=nueva_lista
        self.guardar_en_archivo()
    
    # Función para buscar indivualmente clientes
    def obtener_cliente_individual(self, id_cliente):
        cliente = self.buscar(id_cliente)
        
        if cliente:
            print(f"{cliente} - Descuento: {cliente.calcular_descuento()}")
            return cliente
        else:
            print(f"No se encontró el cliente con ID {id_cliente}")
            return None
        
        
    # Función para obtener todos los clientes
    # utilizado en la interfaz
    def obtener_todos(self):
        return self.__clientes
    
        # Función para cargar clientes desde csv
    def cargar_desde_archivo( self , archivo = 'clientes.csv'):
        try:
            with open(archivo, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    id_cliente = int(row['id'])
                    nombre = row['nombre']
                    email = row['email']
                    tipo = row['tipo']
                
                    if tipo == "Regular":
                        puntos = int(row['puntos']) if row['puntos'] else 0
                        cliente = ClienteRegular(id_cliente, nombre, email, puntos)
                    elif tipo == "Premium":
                        membresia = row['membresia']
                        cliente = ClientePremium(id_cliente, nombre, email, membresia)
                    elif tipo == "Corporativo":
                        empresa = row['empresa']
                        cliente = ClienteCorporativo(id_cliente, nombre, email, empresa)
                
                    self.__clientes.append(cliente)
                    
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error al cargar: {e}")
    
    # Función para guardar clientes en  csv        
    def guardar_en_archivo(self, archivo="clientes.csv"):
        with open(archivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            writer.writerow(['id', 'nombre', 'email', 'tipo', 'puntos', 'membresia', 'empresa'])
        
            for cliente in self.__clientes:
                tipo = type(cliente).__name__.replace('Cliente', '')
                
                # valor por defecto
                puntos = ''
                membresia = ''
                empresa = ''
                
                # tipos
                if tipo == "Regular":
                    puntos = cliente.get_puntos()
                elif tipo == "Premium":
                    membresia = cliente.get_membresia()
                elif tipo == "Corporativo":
                    empresa = cliente.get_empresa()
                
                writer.writerow([
                    cliente.get_id(),
                    cliente.get_nombre(),
                    cliente.get_email(),
                    tipo,
                    puntos,
                    membresia,
                    empresa
                ])           