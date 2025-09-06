# Analizador Léxico

Este proyecto implementa un analizador léxico en Python con interfaz gráfica utilizando **Tkinter**.  

---

## Manual de Usuario

### Requisitos previos
- **Python 3.8 o superior**  
  Verifique la instalación con:  
  ```bash
  python --version    # Windows
  python3 --version   # macOS/Linux
Tkinter

Incluido en instalaciones estándar de Python en Windows y macOS.

En algunas distribuciones Linux puede requerir instalación adicional:

bash
Copiar código
sudo apt install python3-tk
- Preparación del entorno
Cree una carpeta de trabajo (por ejemplo, tarea2tc).

Dentro de la carpeta, cree un archivo llamado Tarea2.py.

Copie y pegue en Tarea2.py el código fuente del analizador léxico provisto en el Anexo del informe.

Guarde los cambios.

- Ejecución de la aplicación
Opción A: IDE
Abra el proyecto en VS Code, PyCharm u otro IDE.

Ejecute Tarea2.py.

Opción B: Terminal/Consola
En Windows:

```bash
python Tarea2.py
```
En macOS/Linux:

```bash
python3 Tarea2.py
```
Si todo está correcto, se abrirá una ventana titulada "Analizador Léxico".

- Uso de la interfaz
En el cuadro de texto superior “Ingrese el código fuente:”, escriba o pegue el código a analizar.

Presione el botón Analizar.

En el cuadro de salida “Tokens reconocidos:” aparecerá, línea por línea, la lista de tokens detectados con el formato:

```makefile
TIPO: lexema
```
Si existe un carácter no reconocido, se mostrará un mensaje de error indicando el símbolo problemático.

- Solución de problemas
No se abre la ventana / error de Tkinter → Asegúrese de tener Tkinter instalado (python3-tk en Linux).

Comando python no encontrado → Use python3 o verifique la instalación de Python.

Errores por caracteres inesperados → Revise que el código de entrada use solo símbolos soportados por el analizador (palabras clave, identificadores, números, operadores y puntuación definidos en el informe).

- Limitaciones conocidas
El analizador omite espacios y saltos de línea, pero no procesa comentarios ni otras extensiones no especificadas; su presencia puede generar errores.

La clasificación de palabras reservadas e identificadores se basa en el conjunto definido en el informe; términos fuera de este conjunto se tratan como IDENTIFICADOR o error, según corresponda.

- Casos de prueba realizados
Positivos → Código con variables, ciclos y operadores correctos.

Negativos → Caracteres inválidos, operadores incompletos (= en lugar de ==).

Colisiones → Pruebas con == y =, >= y >.

Se verificó que los tokens fueran clasificados correctamente y que los errores generaran mensajes adecuados.
