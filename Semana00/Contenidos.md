# Semana 0
1. [Modularización](#Modularización)
2. [Paths](#Paths)
3. [Strings](#Strings)
## Modularización
Se pueden importar archivos .py para utilizarlos en el programa
- `import` nombre_archivo --> Importa todo el archivo
- `import` nombre_archivo `as` lol --> Importa el archivo y se cambia el nombre para utilizarlo
```python
import nombre_archivo as lol

lol.__name__
```
  nombre_archivo
- `from` nombre_archivo `import` a, b, c --> Solo se importa a, b y c
## Paths
"El módulo `os`de python nos provee una interfaz portables para ejecutar operaciones relacionadas al sistema operativo y al sistema de archivos."
```python
import os
```
Un path nos indica el lugar donde se encuentra el archivo, desde la primera carpeta hasta llegar a él. Existen 2 tipos de paths:
- Path **absoluto**: dirección del archivo desde la **raíz** del sistema. Siempre comienza con la dirección del directorio principal. 
    - Ventaja --> No presenta ambigüedades
    - Desventaja --> La ruta debe ser **exactamente igual** en todos los sistemas de archivos
- Path **relativo**: Nunca comienza con el caracter del directorio raíz. Se interpreya a partir de algún directorio específico. Cambian dependiendo de la carpeta donde se ejecute
    - Ventaja --> Permite referenciar a un directorio de manera más simple
    - Desventaja --> Hay que ser meticulos@ para que se ejecute correctamente
El **path** se divide en dos partes:
- Nombre de directorio o `dirname`: Carpeta donde se encuentra el archivo o directorio objetivo
- Nombre del archivo o `basename`: Incluye su extensión (pdf, jpg, etc)
```python
import os

path1 = '/carpeta1/carpeta2/imagen.jpg'

dirname1 = os.path.dirname(path1)
basename1 = os.path.basename(path1)

print(f'path: {path1}')
print(f'dirname: {dirname1}')
print(f'filename/basename: {basename1}')
```
path: carpeta1/carpeta2/imagen.jpg
dirname: /carpeta1/carpeta2
filename/basename: imagen.jpg
-- -- --
### Extensión de archivo
Sirven para dos objetivos:
1. Darle una pista al usuario sobre el tipo de archivo de que se trata
2. Darle una pista al sistema para saber qué programa lo lee
Se puede separar la extensión del archivo utilizando `os.path.splitext`:
```python
nombre_sin_extension, extension = os.path.splitext(basenam1)
print(nombre_sin_extension)
print(extension)
```
imagen
.jpg
-- -- --
