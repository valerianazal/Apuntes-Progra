# Semana 1
1. [Tuplas](#Tuplas)
2. [Listas](#Listas)
3. [Stacks](#Stacks)
4. [Colas](#Colas)
5. [Diccionarios](#Diccionarios)
6. [Sets](#Sets)
7. [Args-Kwargs](#Args-Kwargs)
## Tuplas
Se utilizan para manejar datos de manera **ordenada e inmutable**, no se pueden cambiar los datos de las tuplas. Sin embargo, se pueden modificar datos contenidos dentro de un elemento de esta, siempre qu el tipo de dato lo permita. Estas pueden ser **heterogéneas**, contienen tipos de datos distintos, u **homogéneas**, mismo tipo de dato.
```python
Formas de crear tuplas
a = tuple()
b = (0, 1, 2)
c = (0, )
d = 0, 'uno'

print(a)
print(b)
print(c)
print(d)
```
```
()
(0, 1, 2)
(0,)
(0, 'uno')
```
### Desempaquetamiento de elementos
Las tuplas pueden ser desempaquetadas en **variables individuales**. 
```python

def calcular_geometria(a, b):
    area = a*b
    perimeter = (2*a) + (2*b)
    mpa = a / 2
    mpb = b / 2
    return (area, perimeter, mpa, mpb) # Los paréntesis son opcionales, ya que estamos creando una tupla

data = calcular_geometria(20.0, 10.0)
print(f"1: {data}")

print(type(data))

p = data[1]
print(f"2: {p}")

a, p, mpa, mpb = data
print(f"3: {a}, {p}, {mpa}, {mpb}")

a, p, mpa, mpb = calcular_geometria(20.0, 10.0)
print(f"4: {a}, {p}, {mpa}, {mpb}")
```
```
1: (200.0, 60.0, 10.0, 5.0)
2: 60.0
3: 200.0, 60.0, 10.0, 5.0
4: 200.0, 60.0, 10.0, 5.0
```
### Slicing de tuplas
Es posible tomar secciones de la tupla usando la notación _**slicing**_. Los índices no coinciden directamente con la posición del elemento, sino que funcionan como márgenes. 
```python
data = (400, 20, 1, 4, 10, 11, 12, 500)

# Recuperamos los elementos que están entre los índices 1 y 3
a = data[1:3]
print('1: {0}'.format(a))

# Recuperamos desde el índice 3 en adelante
a = data[3:]
print('2: {0}'.format(a))

# Recuperamos los valores hasta el índice 5
a = data[:5]
print('3: {0}'.format(a))

# Recuperamos desde el índice 2 en adelante respecto del slice en pasos de a dos
a = data[2::2]
print('4: {0}'.format(a))

# Recuperamos entre los índices 1 y 6, en pasos de a dos
a = data[1:6:2]
print('5: {0}'.format(a))

a = data[::-1]
print('6: {0}'.format(a))
```
```
1: (20, 1)
2: (4, 10, 11, 12, 500)
3: (400, 20, 1, 4, 10)
4: (1, 10, 12)
5: (20, 4, 11)
6: (500, 12, 11, 10, 4, 1, 20, 400)
```
## Listas
- `.extend()`: Agrega una lista al final de otra, se fusionan
- `.insert(n, variable)`: Inserta la variable en la posición n de la lista
- `.sort()`: Ordena de menor a mayor
- `.sort(reverse=True)`: Ordena de mayor a menor
- Se puede hacer _**slicing**_ igual que elas tuplas
### Listas por comprensión
Se pueden agregar elementos a las listas de una manera más eficientes, utilizando el iterador dentro de la lista. 
```python
nueva_lista = [expresion for elemento in lista/iterador]
```
```python
largo_de_bandas = []

for nombre in bandas:
    largo_de_bandas.append(len(nombre))

Se puede escribir:
largo_de_bandas = [len(nombre) for nombre in bandas]
```
## Stacks
Un _stack_ es una estructura de datos que como funciona como si fuera una pila de objetos, uno arriba del otro. 
Algunos comandos importantes:
| Operación | Código | Descripción |
| --------- | ------ | ----------- |
| Crear stack | `stack = []` | Crea un stack vacío |
| _Push_ | `stack.append(elemento)` | Agrega un elemento al tope del stack |
| _Pop_ | `stack.pop()` | Retorna y extrae el elemento del tope del stack |
| _Peek_ | `stack[-1]` | Retorna el elemento del tope del stack sin extraerlo |
| _Length_ | `len(stack)` | Cantidad de elementos |
| *is_empty* | `len(stack) == 0` | Retorna *true* si el stack está vacío |
## Colas
Una **cola** es una estructura de datos secuencial que mantiene objetos ordenados de acuerdo a su orden de llegada. 
Algunos comandos importantes:
| Operación | Código | Descripción |
| --------- | ------ | ----------- |
|Crear cola | `cola = deque()` | Crea una cola vacía |
| Crear cola | `cola = deque(cola)` | Crea una cola a partir de los elementos de una lista |
| _Enqueue_ | `cola.append(elemento)` | Agrega un elemento al final de la cola |
| _Dequeue_ | `cola.popleft()` | Retorna y extrae el primer elemento |
| _Peek_ | `cola[0]` | Retorna el primer elemento sin extraerlo |
| _length_ | `len(cola)` | Retorna la cantidad de elementos |
| *is_empty* | `len(cola) == 0` | Retorna *true* si la cola está vacía |

IMPORTANTE: 
```python
from collections import deque
```

### Colas de doble extremo
| Operación | Código | Descripción |
| --------- | ------ | ----------- |
| Crear _deque_ | `deque()` | Vacío |
| Crear _deque_ | `deque(lista)` | A partir de elementos |
| _Add first_ | `deque.appendleft(elemento)` | Agrega al inicio |
| _Add last_ | `deque.append(elemento)` | Agrega al final |
| _Delete first_ | `deque.popleft()` | Retorna y extrae el primer elemento |
| _Delete last_ | `deque.pop()` | Retorna y extrae el último elemento |
| _First_ | `deque[0]` | Retorna el primer elemento |
| _Last_ | `deque[-1]` | Retorna el último elemento |
| _Clear_ | `deque.clear()` | Limpia el deque |
| _Remove_ | `deque.remove(elemento)` | Saca el primer elemento que encuentre |
| _Count_ | `deque.count(elemento)` | Cuenta el número de elementos iguales |

## Diccionarios
Son estructuras de datos **no secuenciales**, es decir, no establecen necesariamente un orden fijo de acceso. Sin embargo, se compensa al proveer métodos muy eficientes de **búsqueda** de datos. 
- Permiten asociar pares de elementos mediante la relación **llave-valor**
- Son **mutables**
- No es necesario que las llaves sean todas del mismo tipo
- Se le consulta por una **llave** y retorna su **valor** asociado
- Implementados por la clase `dict`
- La notación para escribir un diccionario es con llaves {}
```python
monedas = {'Chile': 'Peso', 'Perú': 'Soles', 'España': 'Euro', 'Holanda': 'Euro', 'Brasil': 'Real'}
```
Para acceder al valor asociado a una llave se usan los corchetes []
```python
moneda['Chile']
```
'Peso'
- Si se consulta por una llave que no existe obtenemos un error
- Otra manera de acceder al valor asociado es utilizar el método `get`, el que requiere 2 parámetros: la llave buscada y un valor en caso de que la llave no exista
```python
print(monedas.get('Chile', 'No tiene moneda'))
print(monedas.get('Argentina', 'No tiene moneda'))
```
```python
Peso
No tiene moneda
```
- Si se asigna un valor a una llave pueden pasar 2 cosas:
    - Si la llave **existe**: Se actualiza con el nuevo valor
    - Si la llave **no existe**: Se crea y se le asigna un valor
- No es necesario que las llaves sean todas del mismo tipo
- Se pueden **eliminar** ítems utilizando `del diccionario[nombre_llave]`
- Se puede commprobar la **existencia** de una llave con `llave in diccionario`. Imprime un bool
- Métodos útiles para acceder a valores asociados `dict`:
    - `keys()`: lista con las llaves del diccionario
    - `values()`: lista con los valores
    - `items()`: lista con los **pares** --> tupla (llave, valor)
```python
print(monedas.keys())
print(monedas.values())
print(monedas.items())
```
```
dict_keys(['Chile', 'Perú', 'España', 'Holanda', 'Brasil', 'Vaticano'])
dict_values(['Peso', 'Soles', 'Euro', 'Euro', 'Real', 'Euro'])
dict_items([('Chile', 'Peso'), ('Perú', 'Soles'), ('España', 'Euro'), ('Holanda', 'Euro'), ('Brasil', 'Real'), ('Vaticano', 'Euro')])
```
- **Diccionarios por comprensión:**
```python
from string import ascii_lowercase as letras

numero_por_letra = {letras[i].upper(): i + 1 for i in range(len(letras))}
print(numero_por_letra)

numero_por_vocales = {letras[i].upper(): i + 1 for i in range(len(letras)) if letras[i].upper() in "AEIOU"}
print(numero_por_vocales)
```
```
{'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
{'A': 1, 'E': 5, 'I': 9, 'O': 15, 'U': 21}
```
-- -- -- 
### defaultdicts
Son diccionarios que nos permiten asignar un valor por defecto a cada _key_ con la que se llama al diccioanrio. Reciben una **función** que debe devolver el valor que se adignará por defecto. Esta **no debe recibir parámetros**, puede realizar cualquier acción y puede devolver cualquier objeto.
```python
from collections import defaultdict

msg = 'supercalifragilisticoespialidoso'

# Crea un defaultdict vacío.
vocales = defaultdict(int)  

for letra in msg:
    if letra not in 'aeiou': # Revisa si la letra es una vocal
        continue

    vocales[letra] += 1 # si ya existe, agrega una cuenta mas

print(vocales)
```
```
defaultdict(<class 'int'>, {'u': 1, 'e': 2, 'a': 3, 'i': 6, 'o': 3})
```
```python
from random import random

def funcion_default():
    return random()

diccionario = defaultdict(funcion_default)

print(diccionario)
diccionario['A']
print(diccionario)
diccionario['B']
print(diccionario)
```
```
defaultdict(<function funcion_default at 0x7ffe337cad40>, {})
defaultdict(<function funcion_default at 0x7ffe337cad40>, {'A': 0.030343154687117457})
defaultdict(<function funcion_default at 0x7ffe337cad40>, {'A': 0.030343154687117457, 'B': 0.059489179944941406})
```
-- -- --
- Las **listas** NO se pueden utilizar como llaves
- Las llaves deben ser **únicas** y _**hasheables**_, esto significa que son **inmutables**
- Llaves permitidas: `int`, `str`, `tuple`
- La tupla es hasheable si todos sus elementos lo son
