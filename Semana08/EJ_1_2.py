
import threading
import time


def deletrea_palabra(palabra, periodo):
    for caracter in palabra:
        time.sleep(periodo)
        print(caracter.upper())

thread1 = threading.Thread(name='Palabra 1', target=deletrea_palabra, args=('be í', 3))
thread2 = threading.Thread(name='Palabra 2', target=deletrea_palabra, args=('ud cIUes', 5))
thread3 = threading.Thread(name='Palabra 3', target=deletrea_palabra, args=('naHq', 7))

thread1.start()
thread2.start()
thread3.start()
# Instancia 3 threads distintos y ejecútalos con los parametros dados.