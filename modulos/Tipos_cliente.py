from modulos.cliente import Cliente

class ClienteRegular(Cliente):
    def __init__(self, cliente_id, nombre, email, puntos):
        super().__init__(cliente_id,nombre, email)
        if not isinstance( puntos, (int, float)):
            raise TypeError("Los puntos deben ser numéricos")
        if puntos <0:
            raise ValueError(" los puntos no pueden ser negativos")
                    
        self.__puntos=puntos
    

    def __str__(self):
        return super().__str__() + f" - Puntos: {self.__puntos}"

    # El max descuento de un cliente regular es 5%
    def calcular_descuento(self):
        descuento= self.__puntos* 0.001
        return min(descuento, 0.05)
    
    
class ClientePremium(Cliente):
    
    def __init__(self, cliente_id, nombre, email, membresia):
        super().__init__(cliente_id,nombre, email)
        self.__membresia=membresia
    
    def __str__(self):
        return super().__str__() + f"- Membresía: {self.__membresia}"
    
    def calcular_descuento(self):
        return 0.1
    
class ClienteCorporativo(Cliente):

    def __init__(self, cliente_id, nombre, email, empresa):
        super().__init__(cliente_id,nombre, email)
        if not isinstance(empresa, str):
            raise TypeError("El nombre de la empresa debe ser una cadena")
        if not empresa.strip():
            raise ValueError("El nombre de la empresa no puede estar vacío")
        
        self.__empresa=empresa
        
    def __str__(self):
        return super().__str__() + f"- Empresa: {self.__empresa}"    
    
    def calcular_descuento(self):
        return 0.15
