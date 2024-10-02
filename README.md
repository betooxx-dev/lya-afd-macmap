# MacMap - Reconocedor de Direcciones MAC

## Descripción del Proyecto

MacMap es una aplicación de escritorio desarrollada en Python que permite reconocer y validar direcciones MAC en diversos tipos de archivos. El proyecto incluye tres implementaciones diferentes para el reconocimiento de direcciones MAC:

1. Utilizando un Autómata Finito Determinista con estructuras condicionales (AFD-V1)
2. Utilizando un Autómata Finito Determinista con diccionarios (AFD-V2)
3. Utilizando una Expresión Regular

Todas las implementaciones ofrecen una interfaz gráfica de usuario (GUI) para facilitar su uso.

## Características

- Reconocimiento de direcciones MAC válidas en diferentes formatos (separadas por dos puntos, guiones o espacios)
- Soporte para múltiples tipos de archivos:
  - Excel (.xlsx)
  - CSV (.csv)
  - Word (.docx)
  - HTML (.html)
  - Texto plano (.txt)
- Interfaz gráfica de usuario
- Visualización de resultados en la aplicación
- Exportación de resultados a un archivo CSV

## Requisitos

- Python 3.6 o superior
- Bibliotecas requeridas:
  - tkinter
  - openpyxl
  - python-docx
  - beautifulsoup4

Puedes instalar las bibliotecas necesarias con el siguiente comando:

```
pip install tkinter openpyxl python-docx beautifulsoup4
```

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/betooxx-dev/lya-macmap.git
   ```
2. Navega al directorio del proyecto:
   ```
   cd lya-macmap
   ```

## Uso

### Versión AFD-V1 (con estructuras condicionales)

Para ejecutar la versión que utiliza el Autómata Finito Determinista con estructuras condicionales:

```
python afd_v1.py
```

### Versión AFD-V2 (con diccionarios)

Para ejecutar la versión que utiliza el Autómata Finito Determinista con diccionarios:

```
python afd_v2.py
```

### Versión Expresión Regular

Para ejecutar la versión que utiliza la Expresión Regular:

```
python er.py
```

### Instrucciones de uso:

1. Ejecuta el programa deseado.
2. Haz clic en "Examinar" para seleccionar el archivo que deseas analizar.
3. Haz clic en "Empezar Análisis" para iniciar el proceso de reconocimiento.
4. Los resultados se mostrarán en la interfaz y se guardarán automáticamente en un archivo CSV llamado "resultados_mac.csv".

## Implementaciones

### Autómata Finito Determinista (AFD-V1)

La implementación del AFD-V1 utiliza estructuras condicionales (if-else) para validar cada carácter de la dirección MAC. Esta versión es útil para entender el proceso de validación paso a paso y puede ser más intuitiva para algunos desarrolladores.

Características clave del AFD-V1:
- Utiliza una serie de condiciones if-else para determinar las transiciones entre estados
- Manejo de diferentes separadores (dos puntos, guiones, espacios)
- Validación de la longitud correcta de la dirección MAC
- Aseguramiento de que la dirección MAC no forme parte de una cadena más larga

### Autómata Finito Determinista (AFD-V2)

La implementación del AFD-V2 utiliza un diccionario para representar las transiciones entre estados. Esta versión ofrece una estructura más clara y puede ser más eficiente en términos de rendimiento.

Características clave del AFD-V2:
- Utiliza un diccionario para mapear las transiciones entre estados
- Proporciona una representación más concisa y fácil de mantener del autómata
- Ofrece mayor flexibilidad para modificar o extender el autómata
- Mantiene las mismas capacidades de validación que AFD-V1

### Expresión Regular

La implementación con expresión regular utiliza una única expresión compleja para validar las direcciones MAC. Esta versión es más concisa y potencialmente más rápida para grandes volúmenes de datos.

Expresión regular utilizada:
```python
r'(?<!\S)(?:[0-9A-Fa-f]{2}(?::[0-9A-Fa-f]{2}){5}|[0-9A-Fa-f]{2}(?:-[0-9A-Fa-f]{2}){5}|[0-9A-Fa-f]{2}(?: [0-9A-Fa-f]{2}){5})(?!\S)'
```

Esta expresión regular:
- Valida direcciones MAC con diferentes separadores
- Asegura que la dirección MAC esté aislada (no forma parte de una cadena más larga)
- Verifica la longitud y formato correctos

## Comparación entre AFD-V1 y AFD-V2

- **Estructura**: AFD-V1 utiliza una serie de condiciones if-else, mientras que AFD-V2 utiliza un diccionario para representar las transiciones.
- **Legibilidad**: AFD-V2 suele ser más fácil de leer y entender, especialmente para autómatas complejos.
- **Mantenibilidad**: AFD-V2 es más fácil de mantener y modificar, ya que los cambios en las transiciones solo requieren actualizar el diccionario.
- **Rendimiento**: AFD-V2 puede ser ligeramente más eficiente en términos de rendimiento, especialmente para autómatas grandes.
- **Flexibilidad**: AFD-V2 permite una mayor flexibilidad para extender o modificar el autómata sin cambiar la lógica principal.

Ambas implementaciones son válidas y ofrecen el mismo resultado final. La elección entre AFD-V1 y AFD-V2 dependerá de las preferencias del desarrollador y los requisitos específicos del proyecto.