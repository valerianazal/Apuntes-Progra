# Semana 2
1. [Objetos](#Objetos)
2. [Properties](#Properties)
3. [Herencia](#Herencia)
## Objetos
- Un **objeto** es una colección de datos que además tienen comportamientos asociados
- Datos --> **Atributos**
- Comportamientos --> **Métodos**
```python
class Nombre:

    def __init__(self, a, b, c, ...): # Define los atributos
        self.atributo1 = a
        self.tributo2 = b
        self.atributo3 = c
    
    def nombre_metodo(self, parámteros): # No es necesario entregar parámetros
        función
```
### Encapsulamiento
- Ocultamiento de los atributos de manera que solo puedan ser modificados mediante los métodos que el programador defina
- La **interfaz** define el conjunto de atributos y métodos de un objeto que son expuestos para poder interactuar con otros objetos
- Para tener atributos y métodos que no puedan ser llamados directamente utilizamos `__` (doble underscore)
## Properties
- Se definen métodos específicos para obtener un valor de un atributo privado y para actualizar el valor
- Estos se llaman **getters y setters**
- Una **_property_** funciona como un atributo sobre el cual podemos modificar su comportamiento cada vez que es leido (**get**), escrito (**set**) o eliminado (**del**)
```python
# Formas de crear properties

# 1
@property # getter
def nombre_atributo(self):
    return self.__nombre_atributo

@nombre_atributo.setter
def nombre_property(self, parámetros):
    modificar self.__nombre_atributo

# 2
def _get_nombre_atributo(self):

def _set_nombre_atributo(self, parámetros):

nombre_atributo = property(_get_nombre_atributo, _set_nombre_atributo)
```
## Herencia
- Relación de **especialización** y **generealización** entre clases
- Una clase hereda atributos y métodos de otra
- La que hereda es una _subclase_ y la otra es una _superclase_
- **Overriding**: Podemos volver a definir un método en una subclase, con el mismo nombre que tenía en la superclase (se modifica solo para la subclase)
```python
class ClaseMadre:

    def __init__(self, a, ...):
        self.a = a
        ...

    def metodo1(self, parámetros):

class SubClase(ClaseMadre): # Se marca de donde se hereda

    def __init__(self, b, ...):
        # Para inicializar algunos datos en la clase madres, llamamos explícitamente al __init__ de esa clase
        ClaseMadre.__init__(self, a, ...)
        self.b = b # Proprio de la subclase
    
    def metodo2(self, parámetros):
        # Propio de la subclase

# Otra forma de heredar es con sup(), no se nombre a la clase superior
class SubClase(ClaseMadre):

    def __init__(self, b, ...):
        super().__init__(a, ...)
```
