# Semana 4
## Excepciones
- Condición que altera el flujo normal o esperado de un programa
- También se utilizan para señalar que una acción no pudo ser ejecutada tal como se esperaba
- Ocurren al momento de ejecutar una instrucción

**Tipos de excepciones**
- `SyntaxError`: Sentencia mal escrita o viola reglas sintácticas
- `NameError`: Se intenta utilizar algo co algún nombre que es desconocido para el programa
- `ZeroDivisionError`: Denominador es 0
- `IndexError`: Acceso a un índice no válido
- `KeyError`: Alerta sobre el uso incorrecto o inválido de llaves en diccionarios
- `AtributeError`: Uso incorrecto de métodos o atributos de una clase o tipo de dato
- `TypeError`: Ejecutar operación o función con un argumento que no pertenece tipo correcto
- `ValueError`: Argumento cuyo valor no es apropiado para la ejecución

### Levantando excepciones: `raise`
Podemos mostrar que hubo un error con un mensaje de la siguiente manera:
```python
raise TipoDeError('Mensaje')
```
### Manejo de Excepciones: `try` y `except`
- Cada vez que se levanta una excepción, es posible **atraparla** mediante el uso de sentencias `try`y `except`
- `try`: Permite definir un _scope_ (bloque de código) y si se levanta un excepción dentro del *scope* se **captura**
- A continuación del bloque `try`debe haber una o más instrucciones `except`
- `except`: Permiten implementar el manejo de la excepción capturada
- Cuando se captura la excepción en el bloque `try`el flujo salta al `except`
- El programa continúa en la instrucción **posterior** al bloque `try/except`
- `else`: Se ejecutarán siempre y cuando **no** se haya lanzado una **excepción**
- `finally`: Se realizan **siempre**, independiente de si ocurrió una excepción o no 

### Excepciones personalizadas
- Todas las excepciones heredan de `BaseException`
- Existen tre tipos: `SystemExit`, `KeyboradInterrupt`, y `Exception`
- Podemos crear nuestro tipo de excepciones heredando de la calse `Exception`