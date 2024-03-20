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
botonA = tk.Button(ventana, text="MR", font=("Zilla Slab", 24),
                   bg="#01833D", fg="white", bd=5, relief="groove")
botonA.place(x=10, y=250, width=72, height=72)

botonB = tk.Button(ventana, text="MC", font=("Zilla Slab", 24),
                   bg="#01833D", fg="white", bd=5, relief="groove")
botonB.place(x=100, y=250, width=72, height=72)

botonC = tk.Button(ventana, text="M-", font=("Zilla Slab", 24),
                   bg="#01833D", fg="white", bd=5, relief="groove")
botonC.place(x=190, y=250, width=72, height=72)

botonD = tk.Button(ventana, text="M+", font=("Zilla Slab", 24),
                   bg="#01833D", fg="white", bd=5, relief="groove")
botonD.place(x=282, y=250, width=72, height=72)

boton1 = tk.Button(ventana, text="CA", font=(
    "Zilla Slab", 24), bg="#FFD600", bd=5, relief="groove")
boton1.place(x=10, y=330, width=72, height=72)

botonE = tk.Button(ventana, text="(", bg="#FFD600", font=(
    "Zilla Slab", 24), bd=5, relief="groove")
botonE.place(x=100, y=330, width=72, height=72)

botonF = tk.Button(ventana, text=")", bg="#FFD600", font=(
    "Zilla Slab", 24), bd=5, relief="groove")
botonF.place(x=190, y=330, width=72, height=72)

boton3 = tk.Button(ventana, text="/", font=("Zilla Slab", 24),
                   bg="#01833D", fg="white", bd=5, relief="groove")
boton3.place(x=282, y=330, width=72, height=72)

boton4 = tk.Button(ventana, text="1", font=("Zilla Slab", 24),
                   bg="#2E2F38", fg="white", bd=5, relief="groove")
boton4.place(x=10, y=410, width=72, height=72)

boton5 = tk.Button(ventana, text="2", font=("Zilla Slab", 24),
                   bg="#2E2F38", fg="white", bd=5, relief="groove")
boton5.place(x=100, y=410, width=72, height=72)

boton6 = tk.Button(ventana, text="3", font=("Zilla Slab", 24),
                   bg="#2E2F38", fg="white", bd=5, relief="groove")
boton6.place(x=190, y=410, width=72, height=72)

boton7 = tk.Button(ventana, text="*", font=("Zilla Slab", 24),
                   bg="#01833D", fg="white", bd=5, relief="groove")
boton7.place(x=280, y=410, width=72, height=72)

boton8 = tk.Button(ventana, text="4", font=("Zilla Slab", 24),
                   bg="#2E2F38", fg="white", bd=5, relief="groove")
boton8.place(x=10, y=490, width=72, height=72)

boton9 = tk.Button(ventana, text="5", font=("Zilla Slab", 24),
                   bg="#2E2F38", fg="white", bd=5, relief="groove")
boton9.place(x=100, y=490, width=72, height=72)

boton10 = tk.Button(ventana, text="6", font=("Zilla Slab", 24),
                    bg="#2E2F38", fg="white", bd=5, relief="groove")
boton10.place(x=190, y=490, width=72, height=72)

boton11 = tk.Button(ventana, text="-", font=("Zilla Slab", 24),
                    bg="#01833D", fg="white", bd=5, relief="groove")
boton11.place(x=280, y=490, width=72, height=72)

boton12 = tk.Button(ventana, text="7", font=("Zilla Slab", 24),
                    bg="#2E2F38", fg="white", bd=5, relief="groove")
boton12.place(x=10, y=570, width=72, height=72)

boton13 = tk.Button(ventana, text="8", font=("Zilla Slab", 24),
                    bg="#2E2F38", fg="white", bd=5, relief="groove")
boton13.place(x=100, y=570, width=72, height=72)

boton14 = tk.Button(ventana, text="9", font=("Zilla Slab", 24),
                    bg="#2E2F38", fg="white", bd=5, relief="groove")
boton14.place(x=190, y=570, width=72, height=72)

boton15 = tk.Button(ventana, text="+", font=("Zilla Slab", 24),
                    bg="#01833D", fg="white", bd=5, relief="groove")
boton15.place(x=280, y=570, width=72, height=72)

boton16 = tk.Button(ventana, text="0", font=("Zilla Slab", 24),
                    bg="#2E2F38", fg="white", bd=5, relief="groove")
boton16.place(x=10, y=650, width=72, height=72)

boton17 = tk.Button(ventana, text=".", font=(
    "Zilla Slab", 24), bg="#FFD600", bd=5, relief="groove")
boton17.place(x=100, y=650, width=72, height=72)

boton2 = tk.Button(ventana, image=delete_icon,
                   bg="#FFD600", bd=5, relief="groove")
boton2.place(x=190, y=650, width=72, height=72)

boton18 = tk.Button(ventana, text="=", font=("Zilla Slab", 24),
                    bg="#01833D", fg="white", bd=5, relief="groove")
boton18.place(x=282, y=650, width=72, height=72)

boton2.image = delete_icon

# Función para manejar los eventos de los botones numéricos y el punto


def click_numero(numero):
    texto_actual = label1["text"]

    # Verificar si el usuario intenta añadir un punto decimal
    if numero == ".":
        # Permitir el punto decimal si es el comienzo de un nuevo número decimal
        if texto_actual == "0" or not texto_actual or re.search(r'(\+|\-|\*|\/)$', texto_actual):
            texto_actual += "."
        else:
            # Separar la expresión en componentes basados en los operadores matemáticos
            componentes = re.split(r'(\+|\-|\*|\/)', texto_actual)
            if componentes:
                # Obtener el último componente para verificar si es un número que ya contiene un punto
                ultimo_numero = componentes[-1]
                if '.' in ultimo_numero:
                    # Si el último número ya contiene un punto, no añadir otro y retornar
                    return
            # Si el último número no contiene un punto, añadir el punto decimal
            texto_actual += "."
    else:
        # Si se introduce cualquier número
        if texto_actual == "0":
            # Si el único carácter es '0', reemplazarlo con el número introducido a menos que sea otro '0'
            texto_actual = numero if numero != "0" else "0"
        else:
            # En cualquier otro caso, añadir el número al final
            texto_actual += numero

    # Actualizar el texto en la etiqueta
    label1["text"] = texto_actual
# Función para añadir un operador a la expresión


def click_operador(operador):
    texto_actual = label1["text"]
    if not texto_actual and operador in '-':
        # Permitir un signo negativo si es el primer carácter
        label1["text"] += operador
    elif texto_actual:
        ultimo_caracter = texto_actual[-1]
        if ultimo_caracter in '0123456789)':
            # Si el último carácter es un número o un paréntesis cerrado, añadir el operador
            label1["text"] += operador
        elif ultimo_caracter in '+-*/' and operador in '-':
            # Permitir un signo negativo después de un operador (para números negativos)
            label1["text"] += operador
        elif ultimo_caracter in '+-*/' and operador not in '-':
            # Reemplazar el último operador si se introduce un nuevo operador diferente a menos
            label1["text"] = label1["text"][:-1] + operador
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
        # Determinar la cantidad de dígitos después del punto decimal para redondear, basado en la longitud del número
        if "." in str(resultado):
            # Convertir el resultado a notación científica si es muy grande
            if abs(resultado) > 1e10:
                resultado = format(resultado, '.2e')
            elif abs(resultado) < 1e-4 and resultado != 0:
                resultado = format(resultado, '.2e')
            else:
                # Para números decimales que no requieren notación científica, redondear a un número fijo de decimales
                # Este es un lugar donde puedes ajustar la lógica según tus necesidades
                resultado = round(resultado, 10 - len(str(int(resultado)))) if len(str(int(resultado))) <= 10 else round(resultado, 4)
        else:
            # Para enteros, simplemente limita la longitud total del número
            resultado = resultado if len(str(resultado)) <= 10 else format(resultado, '.2e')

        label2["text"] = str(expresion)
        label1["text"] = str(resultado)
    except ZeroDivisionError:
        label2["text"] = "Error: División por 0"
    except ValueError:
        label2["text"] = "Error: Expresión inválida"
    except SyntaxError:
        label2["text"] = "Error: Expresión inválida"
    except Exception as e:
        label2["text"] = "Error: " + str(e)

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
    # Buscar todas las divisiones en la expresión
    divisiones = re.finditer(r'(/-?\d*\.?\d+)', expresion)
    for match in divisiones:
        # Extraer el divisor, excluyendo el símbolo de división '/'
        divisor = match.group(1)[1:]
        try:
            if float(divisor) == 0:
                return True  # Se encontró una división por cero
        except ValueError:
            pass  # Si el divisor no es un número, ignóralo
    return False  # No se encontró división por cero

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


def key_input(event):
    """Manejar la entrada del teclado."""
    if event.char in '0123456789':
        click_numero(event.char)
    elif event.char == '.':
        click_numero(event.char)
    elif event.keysym == 'Return':
        click_igual()
    elif event.keysym == 'BackSpace':
        label1.config(text=label1["text"][:-1])
    elif event.char == '+':
        click_operador('+')
    elif event.char == '-':
        click_operador('-')
    elif event.char == '*':
        click_operador('*')
    elif event.char == '/':
        click_operador('/')
    elif event.char == '(':
        click_operador('(')
    elif event.char == ')':
        click_operador(')')
    elif event.keysym == 'Escape':
        click_borrar()
    # Añadir aquí más teclas si es necesario


# Vincular el evento de teclado a la ventana principal
ventana.bind('<Key>', key_input)

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
