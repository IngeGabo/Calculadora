import tkinter as tk
from tkinter import PhotoImage
import re
import os
import sys

# Iniciar la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo con Botones Detallados")
ventana.geometry("367x660")  # Ajusta el tamaño de la ventana como necesites
ventana.configure(bg="#D2D3DA")
ventana.resizable(False, False)

def resource_path(relative_path):
    """Obtener la ruta del recurso incluido en el ejecutable."""
    try:
        # PyInstaller crea un directorio temporal y almacena la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

ventana.title("Ejemplo con Botones Detallados")
delete_icon_path = resource_path("delete_icon.png")
print(delete_icon_path)  # Agrega esta línea para depurar
delete_icon = tk.PhotoImage(file=delete_icon_path)
# Crear el segundo label
label2 = tk.Label(ventana, anchor="e", font=("Zilla Slab", 24), bg="#D2D3DA")
label2.place(x=0, y=0, relwidth=1, relheight=0.2)

# Crear el primer label
label1 = tk.Label(ventana, anchor="e", font=("Zilla Slab", 42), bg="#D2D3DA")
label1.place(x=0, y=100, relwidth=1, relheight=0.2)

# Crear los botones
boton1 = tk.Button(ventana, text="CA", font=("Zilla Slab", 24), bg="#FFD600", bd=5, relief="groove")
boton1.place(x=10, y=250, width=160, height=72)

boton2 = tk.Button(ventana, image=delete_icon, bg="#FFD600", bd=5, relief="groove")
boton2.place(x=190, y=250, width=72, height=72)

boton3 = tk.Button(ventana, text="%", font=("Zilla Slab", 24), bg="#01833D", fg="white", bd=5, relief="groove")
boton3.place(x=282, y=250, width=72, height=72)

boton4 = tk.Button(ventana, text="1", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton4.place(x=10, y=330, width=72, height=72)

boton5 = tk.Button(ventana, text="2", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton5.place(x=100, y=330, width=72, height=72)

boton6 = tk.Button(ventana, text="3", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton6.place(x=190, y=330, width=72, height=72)

boton7 = tk.Button(ventana, text="*", font=("Zilla Slab", 24), bg="#01833D", fg="white", bd=5, relief="groove")
boton7.place(x=280, y=330, width=72, height=72)

boton8 = tk.Button(ventana, text="4", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton8.place(x=10, y=410, width=72, height=72)

boton9 = tk.Button(ventana, text="5", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton9.place(x=100, y=410, width=72, height=72)

boton10 = tk.Button(ventana, text="6", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton10.place(x=190, y=410, width=72, height=72)

boton11 = tk.Button(ventana, text="-", font=("Zilla Slab", 24), bg="#01833D", fg="white", bd=5, relief="groove")
boton11.place(x=280, y=410, width=72, height=72)

boton12 = tk.Button(ventana, text="7", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton12.place(x=10, y=490, width=72, height=72)

boton13 = tk.Button(ventana, text="8", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton13.place(x=100, y=490, width=72, height=72)

boton14 = tk.Button(ventana, text="9", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton14.place(x=190, y=490, width=72, height=72)

boton15 = tk.Button(ventana, text="+", font=("Zilla Slab", 24), bg="#01833D", fg="white", bd=5, relief="groove")
boton15.place(x=280, y=490, width=72, height=72)

boton16 = tk.Button(ventana, text="0", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton16.place(x=10, y=570, width=160, height=72)

boton17 = tk.Button(ventana, text=".", font=("Zilla Slab", 24), bg="#FFD600", bd=5, relief="groove")
boton17.place(x=190, y=570, width=72, height=72)

boton18 = tk.Button(ventana, text="=", font=("Zilla Slab", 24), bg="#01833D", fg="white", bd=5, relief="groove")
boton18.place(x=282, y=570, width=72, height=72)

boton2.image = delete_icon

# Función para manejar los eventos de los botones numéricos y el punto
def click_numero(numero):
    texto_actual = label1["text"]
    
    # Si el usuario intenta añadir un punto, necesitamos verificar el último número ingresado
    if numero == ".":
        # Separar la expresión en componentes basados en los operadores
        componentes = re.split(r'(\+|\-|\*|/)', texto_actual)
        if componentes and "." in componentes[-1]:  # Verificar si el último número ya contiene un punto
            return  # No hacer nada si el último número ya tiene un punto
    
    # Concatenar el número o punto seleccionado al texto actual
    nuevo_texto = texto_actual + numero
    # Actualizar el texto del label1
    label1["text"] = nuevo_texto

# Función para añadir un operador a la expresión
def click_operador(operador):
    texto_actual = label1["text"]
    # Prevenir más de un operador consecutivo o empezar con un operador (excepto "-")
    if not texto_actual or texto_actual[-1] in "+-*/%":
        return
    else:
        nuevo_texto = texto_actual + operador
        label1["text"] = nuevo_texto

# Función para manejar el evento del botón de igual
def click_igual():
    expresion = label1["text"]
    try:
        # Prevenir la división por cero
        if "/0" in expresion:
            raise ZeroDivisionError
        resultado = eval(expresion)
        label2["text"] = str(resultado)
    except ZeroDivisionError:
        label2["text"] = "Error: División por 0"
    except:
        label2["text"] = "Error"

# Función para manejar el evento del botón de borrar
def click_borrar():
    # Reiniciar el texto de los labels
    label1["text"] = ""
    label2["text"] = ""

# Asignar las funciones a los botones
boton1["command"] = click_borrar
boton2["command"] = lambda: label1.config(text=label1["text"][:-1])
boton3["command"] = lambda: click_operador("%")
boton4["command"] = lambda: click_numero("1")
boton5["command"] = lambda: click_numero("2")
boton6["command"] = lambda: click_numero("3")
boton7["command"] = lambda: click_operador("*")
boton8["command"] = lambda: click_numero("4")
boton9["command"] = lambda: click_numero("5")
boton10["command"] = lambda: click_numero("6")
boton11["command"] = lambda: click_operador("-")
boton12["command"] = lambda: click_numero("7")
boton13["command"] = lambda: click_numero("8")
boton14["command"] = lambda: click_numero("9")
boton15["command"] = lambda: click_operador("+")
boton16["command"] = lambda: click_numero("0")
boton17["command"] = lambda: click_numero(".")
boton18["command"] = click_igual

ventana.mainloop()
