import tkinter as tk
from tkinter import PhotoImage
import re
import os
import sys

# Iniciar la ventana principal
ventana = tk.Tk()
ventana.geometry("367x730")  # Ajusta el tamaño de la ventana como necesites
ventana.configure(bg="#D2D3DA")
ventana.resizable(False, False)
ventana.title("Calculadora v3") 
memoria = 0


def resource_path(relative_path):
    """Obtener la ruta del recurso incluido en el ejecutable."""
    try:
        # PyInstaller crea un directorio temporal y almacena la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

delete_icon_path = resource_path("delete_icon.png")
print(delete_icon_path)  # Agrega esta línea para depurar
delete_icon = tk.PhotoImage(file=delete_icon_path)

# Crear los labels
# Crear el segundo label
label2 = tk.Label(ventana, anchor="e", font=("Zilla Slab", 24), bg="#D2D3DA")
label2.place(x=0, y=0, relwidth=1, relheight=0.2)

# Crear el primer label
label1 = tk.Label(ventana, anchor="e", font=("Zilla Slab", 42), bg="#D2D3DA")
label1.place(x=0, y=100, relwidth=1, relheight=0.2)

# Crear los botones 
botonA = tk.Button(ventana, text="MR", font=("Zilla Slab", 24), bg="#01833D", fg="white", bd=5, relief="groove")
botonA.place(x=10, y=250, width=72, height=72)

botonB = tk.Button(ventana, text="MC", font=("Zilla Slab", 24), bg="#01833D", fg="white", bd=5, relief="groove")
botonB.place(x=100, y=250, width=72, height=72)

botonC = tk.Button(ventana, text="M-", font=("Zilla Slab", 24), bg="#01833D", fg="white", bd=5, relief="groove")
botonC.place(x=190, y=250, width=72, height=72)

botonD = tk.Button(ventana, text="M+", font=("Zilla Slab", 24), bg="#01833D", fg="white", bd=5, relief="groove")
botonD.place(x=282, y=250, width=72, height=72)

boton1 = tk.Button(ventana, text="CA", font=("Zilla Slab", 24), bg="#FFD600", bd=5, relief="groove")
boton1.place(x=10, y=330, width=72, height=72)

botonE = tk.Button(ventana, text="(", bg="#FFD600", font=("Zilla Slab", 24), bd=5, relief="groove")
botonE.place(x=100, y=330, width=72, height=72)

botonF = tk.Button(ventana, text=")", bg="#FFD600", font=("Zilla Slab", 24), bd=5, relief="groove")
botonF.place(x=190, y=330, width=72, height=72)

boton3 = tk.Button(ventana, text="/", font=("Zilla Slab", 24), bg="#01833D", fg="white", bd=5, relief="groove")
boton3.place(x=282, y=330, width=72, height=72)

boton4 = tk.Button(ventana, text="1", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton4.place(x=10, y=410, width=72, height=72)

boton5 = tk.Button(ventana, text="2", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton5.place(x=100, y=410, width=72, height=72)

boton6 = tk.Button(ventana, text="3", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton6.place(x=190, y=410, width=72, height=72)

boton7 = tk.Button(ventana, text="*", font=("Zilla Slab", 24), bg="#01833D", fg="white", bd=5, relief="groove")
boton7.place(x=280, y=410, width=72, height=72)

boton8 = tk.Button(ventana, text="4", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton8.place(x=10, y=490, width=72, height=72)

boton9 = tk.Button(ventana, text="5", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton9.place(x=100, y=490, width=72, height=72)

boton10 = tk.Button(ventana, text="6", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton10.place(x=190, y=490, width=72, height=72)

boton11 = tk.Button(ventana, text="-", font=("Zilla Slab", 24), bg="#01833D", fg="white", bd=5, relief="groove")
boton11.place(x=280, y=490, width=72, height=72)

boton12 = tk.Button(ventana, text="7", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton12.place(x=10, y=570, width=72, height=72)

boton13 = tk.Button(ventana, text="8", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton13.place(x=100, y=570, width=72, height=72)

boton14 = tk.Button(ventana, text="9", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton14.place(x=190, y=570, width=72, height=72)

boton15 = tk.Button(ventana, text="+", font=("Zilla Slab", 24), bg="#01833D", fg="white", bd=5, relief="groove")
boton15.place(x=280, y=570, width=72, height=72)

boton16 = tk.Button(ventana, text="0", font=("Zilla Slab", 24), bg="#2E2F38", fg="white", bd=5, relief="groove")
boton16.place(x=10, y=650, width=72, height=72)

boton17 = tk.Button(ventana, text=".", font=("Zilla Slab", 24), bg="#FFD600", bd=5, relief="groove")
boton17.place(x=100, y=650, width=72, height=72)

boton2 = tk.Button(ventana, image=delete_icon, bg="#FFD600", bd=5, relief="groove")
boton2.place(x=190, y=650, width=72, height=72)

boton18 = tk.Button(ventana, text="=", font=("Zilla Slab", 24), bg="#01833D", fg="white", bd=5, relief="groove")
boton18.place(x=282, y=650, width=72, height=72)

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
    
    # Si el texto actual termina en un número seguido por un cero no significativo,
    # o si es solo un "0", y estamos añadiendo otro número, reemplazar el cero.
    if texto_actual == "0" or (re.search(r'(\D|^)0+$', texto_actual) and numero != "."):
        # Si el último carácter es un cero no precedido por un punto decimal,
        # reemplazarlo por el número, a menos que estemos añadiendo un punto decimal.
        texto_nuevo = re.sub(r'0+$', '', texto_actual)
        texto_nuevo += numero
        label1["text"] = texto_nuevo
    else:
        # Concatenar el número o punto seleccionado al texto actual
        label1["text"] += numero

# Función para añadir un operador a la expresión
def click_operador(operador):
    texto_actual = label1["text"]
    # Permitir paréntesis si no hay texto o el último carácter es un operador (incluido el paréntesis abierto)
    # y también permitir el paréntesis cerrado si hay un paréntesis abierto sin cerrar.
    if not texto_actual or texto_actual[-1] in "+-*/%(" or (operador == ")" and texto_actual.count("(") > texto_actual.count(")")):
        # Evitar agregar paréntesis cerrado como primer carácter
        if operador == ")" and not texto_actual:
            return
        nuevo_texto = texto_actual + operador
        label1["text"] = nuevo_texto
    elif texto_actual[-1].isdigit() or texto_actual[-1] == ")":  # Si el último carácter es un número o paréntesis cerrado
        # Manejar multiplicación implícita (por ejemplo, 2(3) o (2)(3))
        if operador == "(" or texto_actual[-1] == ")":
            nuevo_texto = texto_actual + "*" + operador  # Añadir * implícitamente
        else:
            nuevo_texto = texto_actual + operador
        label1["text"] = nuevo_texto

# Función para manejar el evento del botón de igual
def click_igual():
    expresion = label1["text"]
    try:
        # Prevenir la división por cero
        if verifica_division_por_cero(expresion):
            raise ZeroDivisionError
        # Verificar si la expresión es válida
        if not es_expresion_valida(expresion):
            raise ValueError
        resultado = eval(expresion)
        resultado = round(resultado, 8)  # Redondear el resultado a 10 decimales
        label2["text"] = str(expresion)
        label1["text"] = str(resultado)
    except ZeroDivisionError:
        label2["text"] = "Error: División por 0"
    except ValueError:
        label2["text"] = "Error: Expresión inválida"
    except:
        label2["text"] = "Error"

# Función para verificar si la expresión es válida
def es_expresion_valida(expresion):
    # Verificar paréntesis balanceados
    balance = 0
    for char in expresion:
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1
        if balance < 0:  # Más paréntesis cerrados que abiertos en cualquier punto
            return False
    if balance != 0:  # Paréntesis no balanceados al final
        return False
    return True

# Función para verificar la división por cero
def verifica_division_por_cero(expresion):
    componentes = re.split('(\D)', expresion)  # Dividir la expresión en números y no números
    for i, componente in enumerate(componentes):
        if componente == '/' and i + 1 < len(componentes):
            siguiente = componentes[i + 1]
            # Intentar convertir el siguiente componente en un número flotante y verificar si es cero
            try:
                if float(siguiente) == 0:
                    return True
            except ValueError:
                pass  # Si el siguiente componente no es un número, ignóralo
    return False

# Función para manejar el evento del botón de borrar
def click_borrar():
    # Reiniciar el texto de los labels
    label1["text"] = ""
    label2["text"] = ""

# Funciones de los botones de memoria
# Funciones para cada operación de memoria
def mr():
    # Usa el valor de memoria para mostrarlo en label1
    global memoria
    label1["text"] = str(memoria)

def mc():
    # Limpia el valor en memoria
    global memoria
    memoria = 0
    mr()

def m_minus():
    # Resta el valor mostrado en la pantalla del valor en memoria
    global memoria
    try:
        memoria -= float(label1["text"])
    except ValueError:
        pass

def m_plus():
    # Suma el valor mostrado en la pantalla al valor en memoria
    global memoria
    try:
        memoria += float(label1["text"])
    except ValueError:
        pass

# Asignar las funciones a los botones
botonA["command"] = lambda: mr()
botonB["command"] = lambda: mc()
botonC["command"] = lambda: m_minus()
botonD["command"] = lambda: m_plus()
botonE["command"] = lambda: click_operador("(")
botonF["command"] = lambda: click_operador(")")
boton1["command"] = click_borrar
boton2["command"] = lambda: label1.config(text=label1["text"][:-1])
boton3["command"] = lambda: click_operador("/")
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
