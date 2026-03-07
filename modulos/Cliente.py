class Cliente:
    def __init__(self, cliente_id, nombre, email):
        
        # Validamos que el ID sea entero y postivo
        if not isinstance(cliente_id, int):
            raise TypeError("El ID debe ser un entero")
        if cliente_id<=0:
            raise ValueError("El ID deber ser un valor posistivo")
        
        # Validamos que el nombre sea un string y no esté vacío
        if not isinstance( nombre, str):
            raise TypeError("El nombre debe ser una cadena del tipo string")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        
        # Validamos el email, debe ser una cadena y contener '@'
        if not isinstance (email, str):
            raise TypeError("El email debe ser una cadena")
        if '@' not in email:
            raise ValueError("Email no válido")        
        
        # Instanciamos atributos privados
        self.__id= cliente_id
        self.__email=email
        self.__nombre=nombre
    
    # Método especial para mejorar legibilidad
    def __str__(self):
        return f"Cliente: {self.__nombre} (ID: {self.__id}) - {self.__email}"
    
    # Función para obtener ID
    def get_id(self):
        return self.__id
    
    # Función para obtener nombre
    def get_nombre(self):
        return self.__nombre
    
    # Función para establecer nombre
    # Valida que sea una cadena y no esté vacío
    def set_nombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        
        self.__nombre=nombre
    
    # Función para calcular descuento
    # Será sobrescrita en las clases hijas
    def calcular_descuento(self):
        return 0
    