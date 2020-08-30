# Semana 3
1. [Diagrama de Clases](#DiagramaDeClases)
2. [Miltuherencia](#Multiherencia)
3. [Clases Abstractas](#ClasesAbstractas)
## Diagrama de Clasess
- Permite visualizar fácilmente las clases que componen un sistema, incluyendo atributos, métodos e interacciones
- Hay que analizar atentamente los requerimientos del sistema
- Explican cómo ocurre la interacción entre las clases dentro del sistema
### Elementos de un diagrama
#### 1. Clases
- Estructuras básicas que **encapsulan** la información
- Se debe recopilar la info de forma independiente para cada clase
- Representamos una clase de la siguiente forma:

<p align="center">
<img src="img/img.png" alt="img" width="150"/>
</p>

- Para los atributos se debe especificar su nombre y tipo de variable. Ejemplo:

<p align="center">
<img src="img/img2.png" alt="img" width="150"/>
</p>

#### 2. Relaciones
- Relaciones más comunes: composición, agregación y herencia

-**Composición**
    - Los objetos se construyen a partir de **inclusión** de otros elementos
    - La existencia de los objetos inlcuidos depende de la existencia del objeto que los incluye

<p align="center">
<img src="img/img3.png" alt="img" width="100"/>
</p>

-**Agregación**
    - Contstruimos la clase bsae usando otros objetos
    - El tiempo de vida del objeto que agregamos es **independiente** del tiempo de vida del objeto que lo incluye

<p align="center">
<img src="img/img4.png" alt="img" width="100"/>
</p>

**Cardinalidad**
- Indica el grado y nivel de dependencia entre las relaciones
- Se indica en cada extremo de la relación
- Posibles casos:
    - 1 o muchos: 1..*
    - 0 o muchos: 0..*
    - Número fijo: n

**Herencia**

<p align="center">
<img src="img/img5.png" alt="img" width="100"/>
</p>

