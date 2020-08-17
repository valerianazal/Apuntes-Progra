# Semana 1
1. [Tuplas-Listas](#Tuplas-Listas)
2. [Stacks](#Stacks)
3. [Colas](#Colas)
4. [Diccionarios](#Diccionarios)
5. [Sets](#Sets)
6. [Args-Kwargs](#Args-Kwargs)
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
()
(0, 1, 2)
(0,)
(0, 'uno')
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
Es posible tomar secciones de la tupla usando la notación _*slicing*_