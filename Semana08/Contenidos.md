# Semana 8
## Threading
- Unidad de ejecución de código dentro de un proceso (programa en ejecución)
- Todo proceso al crearse posee al menos un thread: Thread principal
- Podemos crear más para que se ejecuten distintas partes del código al mismo tiempo
- Cada _thread_ tiene una porción de tiempo para ejecutar en el núcleo. 
- _thread scheduling/slicing_:
    1. Se escoge un _thread_ entre los disponibles
    2. Se ejecuta un cierto nº de instrucciones o durante un cierto tiempo
    3. Se deja el _thread_ actual en espera
    4. Se vuelve al paso 1
- Cuando hay un solo núcleo, no hay paralelismo
### Creación de _threads_
```python
import threading
```
- Los _threads_ son representados por **objetos**
- Se le entrega una **función** que se recibe como parámetro **`target`** al crear el _thread_
```python
def contar_diez_ovejas():
    print("Tengo sueño...")
    for numero in range(1, 6):
        print(f"({numero} oveja{'s' if numero > 1 else ''})")
    print("A dormir...")

mi_hilo = threading.Thread(target=contar_diez_ovejas)
# Para ejecutar se llama al método start()
mi_hilo.start()
```
```
Tengo sueño...
(1 oveja)
(2 ovejas)
(3 ovejas)
(4 ovejas)
(5 ovejas)
A dormir...
```
- Los _threads_ definidos de esta forma son de un solo uso, nose pueden volver a ejecutar
- Le podemos poner nombre a los _threads_
- El nombre que se le asigna al principal es `MainThread`
```python
def saludar():
    thread_actual = threading.current_thread()  # Retorna un referencia de la instancia del thread que está ejecutando este código
    print(f"Hola desde {thread_actual.name}")

hilo_1 = threading.Thread(name="Mi thread 1", target=saludar)
hilo_2 = threading.Thread(name="Mi thread 2", target=saludar)

hilo_1.start()
hilo_2.start()
saludar()
```
```
Hola desde Mi thread 1
Hola desde Mi thread 2
Hola desde MainThread
```
- Se pueden crear _threads_ como instancias de una clase que hereda de la clase `Thread`
- Debemos definir el método `run` para que se ejecute el _thread_ con `start()`
- **`join()`**:
    - El _thread_ que llama al método queda bloqueado hasta que los _threads_ referenciados terminen correctamente
    - Se puede especificar un **`timeout`** (en segundos): el programa esperará al _thread_ referenciado solo por ese tiempo
    - Cualquier _thread_ puede esperar cualquier otro
- **`is_alive()`**:
    - Para ver si un _thread_ está en funcionamiento

### Daemons
- No impiden que el programa principal termine
- Los dejamos corriendo y el programa principal terminará aunque ellos sigan en ejecución
```python
dormilon = threading.Thread(name="Dormilón", target=dormilon, daemon=True)
```
- Es posible hacer que el programa espere a un _daemon_ mediante el uso de `join()`
- Una vez que se llama al método `start()`, un _daemon_ no puede pasar a ser _no daemon_ y viceversa
- Al hacer una subclase de Thread, que queremos que sea _daemon_, podemos indicar que el _thread_ es _daemon_ durante su inicialización, usando el atributo `daemon`
```python
class Daemon(threading.Thread):
    
    def __init__(self):
        super().__init__()
        # Cuando inicializamos el thread lo declaramos como daemon
        self.daemon = True
    
    def run(self):
        print("Daemon thread: Empezando...")
        time.sleep(2)
        print("Daemon thread: Terminando...")

daemon = Daemon()
daemon.start()
daemon.join()
```
```
Daemon thread: Empezando...
Daemon thread: Terminando...
```
- Podemos poner un **Timer** para que empiece un _thread_
```python
def mi_timer(ruta_archivo):
    with open(ruta_archivo) as archivo:
        for linea in archivo:
            print(linea)

t1 = threading.Timer(10.0, mi_timer, args=("files/mensaje_01.txt",))
t2 = threading.Timer(5.0, mi_timer, kwargs={"ruta_archivo": "files/mensaje_02.txt"})

t1.start() # el thread t comenzará después de 10 seconds
t2.start() # el thread t comenzará después de 5 seconds
```
