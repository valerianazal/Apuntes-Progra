
import threading
import time
from random import randint


def cuenta_hasta_diez():
    nombre_thread = threading.current_thread().name
    for numero in range(1, 11):
        time.sleep(randint(1, 5))
        print(f"{nombre_thread}: {numero}...")
        
# Instancia 5 threads distintos y ejecútalos.
thread1 = threading.Thread(name='Skeret 1', target=cuenta_hasta_diez)
thread2 = threading.Thread(name='Skeret 2', target=cuenta_hasta_diez)
thread3 = threading.Thread(name='Skeret 3', target=cuenta_hasta_diez)
thread4 = threading.Thread(name='Skeret 4', target=cuenta_hasta_diez)
thread5 = threading.Thread(name='Skeret 5', target=cuenta_hasta_diez)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()