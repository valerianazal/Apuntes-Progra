# Semana 5
## Iterar sobre estrudcturas de datos
- **Iterable**: Cualquier objeto sobre el cual se puede iterar (for i in _iterable_)
    - Implementa el método `__iter()`
    - Se puede iterart todas las veces que uno queira sobre un iterable
- **Iterador**: Objeto que itera sobre un iterable
    - Objeto retornado por el método `__iter()__`
    - Implementa el método `__next()__` --> Retorna uno a uno los elementos de la estructura cada vez que se invoca la función
    - Si se piden más elementos de los que tiene la estructura levantará una **excepción** de tipo `StopIteration`
    - Cada iterador tiene su propia memoria, no depende del iterable
- Para empezar nuevamente a iterar se debe obtener otro iterador
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
