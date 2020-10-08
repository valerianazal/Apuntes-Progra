import time
import random
import threading 


# Implementar modelacion con Thread...
# ... puedes usar herencia si quieres ;)
class Minero(threading.Thread):

    def __init__(self, nombre):
        super().__init__(name='o')
        self.nombre = nombre
        self.cantidad = 0
        self.adentro = False
        self.velocidad = random.randint(2, 4)

    def recolectar_recursos(self):
        cantidad = random.randint(5, 15)
        tiempo = cantidad/self.velocidad
        self.adentro = True
        time.sleep(tiempo)
        print(f'Trabajador {self.nombre} ha recolectado {cantidad} DCCriptoMonedas')
        self.cantidad += cantidad
        self.adentro = False

    def run(self): #Puedes modificarlo si quieres trabajar con herencia ;)
        for i in range(3):
            print(f'Trabajador {self.nombre} ha entrado a la DCCueva')
            self.recolectar_recursos()


t1 = Minero('John') #Eres libre de modificar los nombres
t2 = Minero('Alex') #Eres libre de modificar los nombres
t3 = Minero('Peter') #Eres libre de modificar los nombres :)

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

#No modificar
total = t1.cantidad + t2.cantidad + t3.cantidad
print('------------------------------------------')
print(f'Se han recolectado {total} DCCriptoMonedas')