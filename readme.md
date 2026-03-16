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

├── main.py
├── modulos/
│   ├── __init__.py
│   ├── cliente.py
│   ├── gestor_clientes.py
│   └── tipos_cliente.py
├── diagramas/
│   └── clientes_uml.drawio
├── clientes.csv
└── README.md

## Cómo ejecutar
```bash
python main.py
