import os
from random import shuffle, choice
from collections import namedtuple
        
class Juego:
    
    def __init__(self, turnos):
        
        self.mazo = []
        self.cartas_j1 = []
        self.cartas_j2 = []
        
        self.read_file()
        self.repartir_cartas()
        self.comenzar_juego(turnos)
    
    def read_file(self):
        Crear_tupla = namedtuple('Crear_carta', ['nombre', 'ataque', 'defensa'])
        path_cards = os.path.join('contenidos', 'semana-01', \
            'ejercicios_propuestos', 'cards.csv')
        with open(path_cards, 'rt') as archivo:
            lineas = archivo.readlines()
            for i in range(len(lineas)):
                if i == 0:
                    pass
                else:
                    carta = lineas[i].strip().split(',')
                    self.mazo.append(Crear_tupla(carta[0], carta[1], carta[2]))
        pass
    
    def repartir_cartas(self):
        shuffle(self.mazo)
        for i in range(5):
            self.cartas_j1.append(self.mazo.pop(0))
            self.cartas_j2.append(self.mazo.pop(0))
        pass
    
    def atacar(self, atacante, defen):
        ptos_atacante = atacante.ataque
        ptos_defensa = defen.defensa
        if ptos_atacante >= ptos_defensa:
            return False
        else:
            return True


    def comenzar_juego(self, turnos):
        for i in range(1, turnos + 1):
            print(f"Turno número {i}")
            if self.cartas_j1 != [] and self.cartas_j2 != []:
                if i % 2:
                    # Ataca el jugador 1
                    ataque1 = choice(self.cartas_j1)
                    defensa2 = choice(self.cartas_j2)
                    if self.atacar(ataque1, defensa2) == True:
                        self.cartas_j1.remove(ataque1)
                        print(f'J2 gana el turno {i}')
                    else:
                        self.cartas_j2.remove(defensa2)
                        print(f'J1 gana el turno {i}')
                    pass
                else:
                    # Ataca el jugador 2
                    ataque2 = choice(self.cartas_j2)
                    defensa1 = choice(self.cartas_j1)
                    if self.atacar(ataque1, defensa2) == True:
                        self.cartas_j2.remove(ataque2)
                        print(f'J1 gana el turno {i}')
                    else:
                        self.cartas_j1.remove(defensa1)
                        print(f'J2 gana el turno {i}')
                    pass
            else:
                if self.cartas_j2 == []:
                    print('Gana J1')
                else:
                    print('Gana J2')
                break

juego = Juego(10)