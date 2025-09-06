import re
import tkinter as tk

# PARTE 1: FORMAS DE IDENTIFICACION DE TOKEN
token_s = [
    ('PALABRA_RESERVADA',   r'\b(?:if|else|while|for|return|int|float|char)\b'),    # Palabras clave
    ('IDENTIFICADOR',       r'\b[A-Za-z_]\w*\b'),                                   # Identificador (variable, función, etc.)
    ('NUM',                 r'\b\d+(\.\d+)?\b'),                                    # Número entero o decimal
    ('INCREMENTO',          r'\+\+'),                                               # Operador de incremento "++"
    ('DECREMENTO',          r'--'),                                                 # Operador de decremento "--"
    ('O_RELACIONAL',        r'(?:>=|<=|==|!=|>|<)'),                                # Operadores relacionales
    ('O_LOGICO',            r'(?:&&|\|\||!)'),                                      # Operadores lógicos (&&, ||, !)
    ('O_ASIGNACION',        r'(?:\+=|-=|\*=|/=|%=|=)'),                             # Operadores de asignación (incluyendo compuestos)
    ('O_ARITMETICO',        r'[+\-*/%]'),                                           # Operadores aritméticos (+, -, *, /, %)
    ('O_TERNARIO',          r'[\?:]'),                                              # Operador ternario ? y :
    ('PUNTUACION',          r'[\(\)\[\]\{\},;]'),                                   # Delimitadores y puntuación
    ('IGNORAR',             r'[ \t\n]+'),                                           # Espacios en blanco (ignorados)
    ('ERROR',               r'.')                                                   # Cualquier otro carácter (error)
]       

#PARTE 2: COMPILACION DE EXPRESION CON TODAS LAS SUB-EXPRESIONES
tok_regex = '|'.join(f'(?P<{name}>{pattern})' for (name, pattern) in token_s)
regex_compilado = re.compile(tok_regex)


#PARTE 3: LECTURA DEL CONTENIDO, DEVUELVE LA LISTA DE TOKENS IDENTIFICADOS
def token(code):
    tokens = []
    for mo in regex_compilado.finditer(code):
        tipo = mo.lastgroup    # Grupo
        valor = mo.group(tipo) # Texto identificado en ese grupo.
        if tipo == 'IGNORAR':
            continue           # espacios no se consideran
        if tipo == 'ERROR':
            raise RuntimeError(f"Se encontro '{valor}' en la entrada, inesperado")
        tokens.append((tipo, valor))
    return tokens




#PARTE 4: Interfaz
root = tk.Tk()
root.title("Analizador Léxico")

# Widgets
label_entrada = tk.Label(root, text="CODIGO A EVALUAR:")
text_entrada = tk.Text(root, width=80, height=15)
boton_analizar = tk.Button(root, text="ANALISIS ()")
label_resultado = tk.Label(root, text="TOKENS IDENTIFICADOS:")
text_salida = tk.Text(root, width=80, height=15, state='disabled')



def realizar_analisis():
    codigo = text_entrada.get("1.0", tk.END)
    try:
        lista_tokens = token(codigo)
        text_salida.config(state=tk.NORMAL)
        text_salida.delete("1.0", tk.END) 
        for tipo, valor in lista_tokens:
            text_salida.insert(tk.END, f"{tipo}: {valor}\n")
        text_salida.config(state=tk.DISABLED)
    except RuntimeError as e:
        text_salida.config(state=tk.NORMAL)
        text_salida.delete("1.0", tk.END)
        text_salida.insert(tk.END, str(e))
        text_salida.config(state=tk.DISABLED)

boton_analizar.config(command=realizar_analisis)  # Asociar la función al botón


label_entrada.pack(anchor='w')
text_entrada.pack(padx=5, pady=5)
boton_analizar.pack(pady=5)
label_resultado.pack(anchor='w')
text_salida.pack(padx=5, pady=5)


root.mainloop()