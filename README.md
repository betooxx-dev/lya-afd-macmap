# MacMap - Reconocedor de Direcciones MAC

## Descripción del Proyecto

MacMap es una aplicación de escritorio desarrollada en Python que permite reconocer y validar direcciones MAC en diversos tipos de archivos. El proyecto incluye dos implementaciones diferentes para el reconocimiento de direcciones MAC:

1. Utilizando un Autómata Finito Determinista (AFD)
2. Utilizando una Expresión Regular

Ambas implementaciones ofrecen una interfaz gráfica de usuario (GUI) para facilitar su uso.

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
   git clone https://github.com/tu-usuario/macmap.git
   ```
2. Navega al directorio del proyecto:
   ```
   cd macmap
   ```

## Uso

### Versión AFD

Para ejecutar la versión que utiliza el Autómata Finito Determinista:

```
python afd.py
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

### Autómata Finito Determinista (AFD)

La implementación del AFD sigue un enfoque de estados para validar cada carácter de la dirección MAC. Esta versión es particularmente útil para entender el proceso de validación paso a paso y puede ser más fácil de modificar para requisitos específicos.

Características clave del AFD:
- Manejo de diferentes separadores (dos puntos, guiones, espacios)
- Validación de la longitud correcta de la dirección MAC
- Aseguramiento de que la dirección MAC no forme parte de una cadena más larga

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
