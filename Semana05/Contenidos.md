# Semana 5
## Iterar sobre estructuras de datos
- **Iterable**: Cualquier objeto sobre el cual se puede iterar (for i in _iterable_)
    - Implementa el método `__iter()`
    - Se puede iterart todas las veces que uno queira sobre un iterable
- **Iterador**: Objeto que itera sobre un iterable
    - Objeto retornado por el método `__iter()__`
    - Implementa el método `__next()__` --> Retorna uno a uno los elementos de la estructura cada vez que se invoca la función
    - Si se piden más elementos de los que tiene la estructura levantará una **excepción** de tipo `StopIteration`
    - Cada iterador tiene su propia memoria, no depende del iterable
- Para empezar nuevamente a iterar se debe obtener otro iterador
- Si el iterador no implementa **`__iter__`**, no se podrá guardar y usar directament en un for
- Si paramos la iteración atnes  de recorrer todos los elementos, podemos continuar con el mismo iterador desde el punto en que lo dejamos
- Cada **iterador** tiene su propia memoria, la que no depende del iterable
```python
conjunto = {1, 3, 4, 6}
iterador = iter(conjunto)  # Esto es lo mismo que conjunto.__iter__()
print(type(iterador))

## Ahora vamos a invocar a next para que el iterador nos entregue el siguiente valor del iterable
print(next(iterador))      # Esto es lo mismo que iterador.__next__()
print(next(iterador))
print(next(iterador))
```
1
3
4
### Forma básica de hacer una estructura iterable
```python
class Nodo:
    
    def __init__(self, valor, siguiente):
        # Cada nodo contiene un valor...
        self.valor = valor
        # ... y referencia al siguiente Nodo
        self.siguiente = siguiente
    
    def __repr__(self):
        return f"{self.valor}"

class Iterable:

    def __init__(self, a):
        self.a = a
    
    def __iter__(self):
        return Iterador(self.a)

class Iterador:

    def __init__(self,  iterable):
        self.iterable = iterable
    
    def __iter__(self):
        return self
    
    def  __next__(self):
        if self.iterable is None:
            # Levantamos una excepción del tipo StopIteration
            # con el mensaje "Llegamos al final".
            raise StopIteration("Llegamos al final")
        else:           
            valor = self.iterable
            self.iterable = self.iterable.siguiente
            return valor
        
datos = Nodo(1, Nodo(2, Nodo(3, Nodo(4, Nodo(5, None)))))
iterable = Iterable(datos)
for i in iterable:
    print(i)
```
1
2
3
4
5
## Generadores
- Son un caso especial de los **iteradores**
- Nos permiten iterar sobre  secuencias de datos isn la  necesidad de almacenarlos en alguna estructura especial
- Una vez que terminamos de iterar sobre un generador, este desaparece
- La sintaxis para crearlos es muy parecida a la comprensión de  listas, pero con **paréntesis normales ()**
- Solo se pueden usar **1 VEZ**
- Se ahorra almacenamiento
- Los podemos poner en `__iter__`
```python
generador_pares = (2 * i for i in range(6))
for i in generador_pares:
    print(i)
```
0
2
4
6
8
10
```python
generador_pares = (2 * i for i in range(10))
print(next(generador_pares))
print(next(generador_pares))
```
0
2
### Funciones generadoras
- Las funciones pueden funcionar como generadores con la sentencia`yield`, un análogo de `return`, con ciertas diferencias
- `yield`: Se encarga de **retornar el valor indicado**, pero también se  asegura que en la próxima llamada a la función, la ejecución parta **desde donde la dejamos**
- También se puede usar `next`
```python
def conteo_decreciente(n):
    print(f"Contando en forma decreciente desde {n}")
    while n > 0:
        yield n
        n -= 1

x = conteo_decreciente(5)
for number in x:
    print(number)
```
Contando en forma decreciente desde 5
5
4
3
2
1
## Funciones lambda
- Las funciones son tratadas como cualquier otra variable:
    - Pueden ser asignadas a una variables y usarlas
    - Pueden ser pasadas como parámetros a otras
**Funciones lambda**: 
    - Forma alternativa de funciones. 
    - No se necesita `return`
    - Se caracterizan por pueden ser definidas en forma anónima
    - No tienen nombre espécifico
    - Son utilizadas únicamente donde fueron creadas
```python
sucesor = lambda x: x + 1
# Es (casi) equivalente a
def sumar_uno(x):
    return x + 1

restar = lambda x, y: x - y
# Es (casi) equivalente a
def sustracción(x, y):
    return x - y
```
### `map`
`map(f, iterable)` = `(f(x) for x in iterable)`
- Recibe como parámetro una función y **al menos** un iterable
- Retorna un generador que resulta de aplicar la función sobre cada  elemento del iterable
- La cantidad de elementos que se procesan corresponde a la  cantidad que tiene el  iterable más pequeño
```python
strings = ['Señores pasajeros', 'Disculpen', 'mi', 'IntencIÓN', 'no', 'Es', 'MolEstar']
mapeo = map(lambda x: x.lower(), strings)
', '.join(mapeo)
```
'señores pasajeros, disculpen, mi, intención, no, es, molestar'
```python
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

mapeo_1 = map(lambda x, y: x ** 2 + y ** 2, a, b)
mapeo_2 = map(lambda x, y, z: x + y ** 2 + z ** 3, a, b, c)

print(list(mapeo_1))
print(list(mapeo_2))
```
[290, 148, 130, 116]
[289, 82, 249, 833]
### `filter`
`filter(f, iterable)` = `(x for x in iterable if f(x))`
- Recibe una función que retorna `True` o `False` y un iterable
- Retorna un generador que entrega  aquellos elementos  del iterable donde la función retorna `True`
```python
def fibonacci(límite):
    a, b = 0, 1
    for _ in range(límite):
        yield b
        a, b = b, a + b

filtrado_impares = filter(lambda x: x % 2 != 0, fibonacci(10))
print(list(filtrado_impares))

filtrado_pares = filter(lambda x: x % 2 == 0, fibonacci(10))
print(list(filtrado_pares))
```
[1, 1, 3, 5, 13, 21, 55]
[2, 8, 34]
```python
set_filtrado = filter(lambda x: x < 10, {100, 1, 5, 9, 91, 1})
list(set_filtrado)
```
[1, 5, 9]
### `reduce`
`reduce(f, iterable)`
`from functools import reduce`
- Consiste enaplicar sucesivamente la función f(x, y), donde `x` es el resultado acumulado e `y` es un elemento de la secuencia
- Recibe una función que toma dos valores y un iterable
- Retorna lo que resulta de aplicarla función al irerable `[s1, s2, s3, ..., sn] de la siguiente forma: f(f(f(f(s1, s2), s3), s4), s5), ...