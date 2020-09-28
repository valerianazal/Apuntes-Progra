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
