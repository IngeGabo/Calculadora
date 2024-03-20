# Calculadora

Este proyecto consiste en una calculadora implementada en varias versiones, cada una expandiendo funcionalidades y mejorando la interfaz de usuario.

## Versión 1 (V1)

La V1 es una calculadora básica implementada en Python que realiza operaciones de suma, resta, multiplicación y división. Acepta entrada del usuario a través de la consola y maneja errores como división por cero.

![Diagrama V1](https://github.com/IngeGabo/Calculadora/assets/72628195/f1bb7d74-7b4b-4f62-a80b-4bfd479aa61d)


### Cambios de la V1

- Funciones básicas de una calculadora en consola.
- Manejo de excepciones para errores de entrada y matemáticos.

## Versión 2 (V2)

La V2 introduce una interfaz gráfica usando Tkinter, mejora la experiencia del usuario con botones interactivos y muestra el cálculo en tiempo real.

![Diagrama V2](https://github.com/IngeGabo/Calculadora/assets/72628195/651f5aeb-ab8f-4bce-a34c-e1e3f75787fe)


### Cambios de la V2

- Transición de consola a interfaz gráfica.
- Uso de Tkinter para crear la interfaz de usuario.

## Versión 3 (V3)

La V3 añade funcionalidades de memoria como MR, MC, M+, y M-, permitiendo al usuario almacenar y recuperar números durante los cálculos.

![Diagrama V3](https://github.com/IngeGabo/Calculadora/assets/72628195/4f65e135-fcf6-488a-bb65-68ae19383215)

### Cambios de la V3

- Implementación de botones de memoria.
- Mejoras en la gestión del estado interno de la calculadora.
- Ademas de la correccion de errores encontrados durante las pruebas.

## Versión 4 (V4)

La V4 introduce la capacidad de manejar entradas de teclado, facilitando un flujo de trabajo más rápido y eficiente para el usuario.

![Diagrama V4](https://github.com/IngeGabo/Calculadora/assets/72628195/c23fd809-d14d-4300-afad-1ffe17466e49)

### Cambios de la V4

- Manejo de eventos de teclado para todas las operaciones de la calculadora.
- Optimización del flujo de trabajo y la interacción del usuario.
- Ademas de la correccion de errores encontrados durante las pruebas.

## Sección Técnica

### Tecnologías Utilizadas

- Python 3
- Tkinter para la interfaz gráfica
- `re` para el manejo de expresiones regulares
- `os` y `sys` para la interacción con el sistema operativo

### Instalación y Ejecución

#### Para usuarios de Windows:

Se proporcionan archivos `.exe` para cada versión de la calculadora, los cuales pueden ejecutarse directamente sin necesidad de un intérprete de Python. Estos archivos están disponibles en la sección de lanzamientos del repositorio.

Para ejecutar la calculadora:

1. Descargar el último archivo `.exe` del lanzamiento del repositorio.
2. Hacer doble clic en el archivo `.exe` descargado correspondiente a la versión deseada.

#### Para desarrolladores y usuarios de sistemas basados en Unix:

Para ejecutar el código fuente directamente, se requiere tener Python y las dependencias necesarias instaladas.

1. Clonar el repositorio:

   git clone https://github.com/IngeGabo/Calculadora

#### Navegar al directorio de la versión deseada:
cd Calculadora/v1   (Cambiar v1 por la versión que se desea ejecutar)

#### Ejecutar la aplicación:
python Calculadora.py (Cambiar el nombre por el de la version que se desea ejecutar)
