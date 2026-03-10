class GestorClientes:
    def __init__(self):
        self.__clientes=[]    
    
    #Función para agregar clientes
    #Valida que el no esté vacío y el ID no se repita 
    def agregar(self, cliente):
        if cliente is None:
            raise ValueError("No se puede agregar un cliente vacío")
        if self.buscar(cliente.get_id()):
            raise ValueError("Ya existe cliente con ese ID")
        
        self.__clientes.append(cliente)
    
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