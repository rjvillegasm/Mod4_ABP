# Sistema de gestión de clientes desarrollado en python.

Permite crear, listar, buscar y eliminar clientes de tres tipos: Regular, Premium y Corporativo. Implementa persistencia de datos en archivo CSV, interfaz gráfica con tkinter y manejo de errores mediante excepciones.

## Tecnologías utilizadas:

- Python
- POO
- Tkinter
- CSV

## Funcionalidades:

CRUD completo: Crear, leer, actualizar y eliminar clientes

Búsqueda individual: Buscar clientes por ID

Descuentos: Cada tipo de cliente tiene su propio cálculo de descuento

Persistencia: Los datos se guardan automáticamente en archivo CSV

Interfaz intuitiva: Formulario dinámico que muestra campos según el tipo de cliente

Manejo de errores: Validaciones y excepciones para entradas incorrectas


## Estructura:

├── main.py                          # Interfaz gráfica con tkinter
├── modulos/                         # Paquete de módulos
│   ├── __init__.py                  # Inicializador del paquete
│   ├── cliente.py                    # Clase base Cliente
│   ├── gestor_clientes.py            # Lógica de negocio y persistencia CSV
│   └── tipos_cliente.py              # Clases derivadas (Regular, Premium, Corporativo)
├── diagramas/                        # Diagramas del proyecto
│   └── clientes_uml.drawio           # Diagrama UML
├── clientes.csv                      # Archivo de datos (se genera automáticamente)
└── README.md                         # Documentación del proyecto

## Cómo ejecutar
```bash
python main.py