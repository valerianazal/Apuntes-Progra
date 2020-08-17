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
### Problema de portabilidad
Hay diferencias en los caracteres de separación entre sistemas operativos, entonces se genera un problema de portabilidad de programas. Por lo tanto, se puede utilizar el módulo `os.path.join`, ya que reescribe rutas usando los caracteres de separación nativos del sistema operativo
```python
ruta = os.path.join('Users', 'Pedro', 'Libros', 'python.pdf')
ruta
```
En Mac: 'Users/Pedro/Libros/python.pdf'
En Windows: 'Users\Pedro\Libros\python.pdf'
### Navegación entre directorios
- `listdir`: Al entregarle una ruta muestra una lista con todos los nombres de directorios y archivos dentro de esta
```python
lista_de_contenidos = os.listdir('data')
lista_de_contenidos
```
['archivo.txt', 'archivo_de_texto.jpg, 'files.png']
- `walk`: Permite obtener rutas de un directorio, de sus subdirectorios y de sus archivos. Se navega recursivamente dentro de la carpeta para ver lo que contiene.
```python
for raiz, directorios, archivos in os.walk("data", topdown = True):
    print("Raíz:",raiz)
    print()
    print("Archivos:")
    for archivo in archivos:
        print(os.path.join(raiz, archivo))
    print()
    print("Directorios:")
    for directorio in directorios:
        print(os.path.join(raiz, directorio))
    print("-"*30)
```

Raíz: data

Archivos:
data/archivo.txt
data/archivo_de_texto.jpg
data/files.png

Directorios:
data/gato
'------------------------------'
Raíz: data/gato

Archivos:
data/gato/juego_1.txt
data/gato/juego_2.txt

Directorios:
'------------------------------'

