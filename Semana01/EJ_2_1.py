import os
from random import shuffle, choice
        
class Juego:
    
    def __init__(self, turnos):
        
        self.mazo = []
        self.cartas_j1 = []
        self.cartas_j2 = []
        
        self.read_file()
        self.repartir_cartas()
        self.comenzar_juego(turnos)
        self.atacar(atacante)
    
    def read_file(self):
        path_cartas = os.path.join('contenidos', 'semana-01', \
            'ejercicios_propuestos', 'cards.csv')
        with open(path_cartas, 'rt') as cartas:
            lineas = cartas.readlines()
            self.mazo = [n.strip().split(',') for n in lineas[1:]]
        pass
    
    def repartir_cartas(self):
        shuffle(self.mazo)
        for i in range(5):
            self.cartas_j1.append(self.mazo.pop(0))
            self.cartas_j2.append(self.mazo.pop(0))
        pass
    
    def atacar(self, atacante):
        j1 = choice(self.cartas_j1)
        j2 = choice(self.cartas_j2)
        x = 1
        if atacante % 2 == 0:
            if int(j1[1]) >= int(j2[2]):
                self.cartas_j2.remove(j2)
            else:
                self.cartas_j1.remove(j1)
                x = 2
        else:
            if int(j2[1]) >= int(j1[2]):
                self.cartas_j1.remove(j1)
                x = 2
            else:
                self.cartas_j2.remove(j2)
        print(f'El jugador {x} gana el turno')

    def comenzar_juego(self, turnos):
        for i in range(1, turnos + 1):
            print(f"Turno número {i}")
            if self.cartas_j1 != [] and self.cartas_j2 != []:
                if i % 2:
                    # Ataca el jugador 1
                    self.atacar(i)
                    pass
                else:
                    # Ataca el jugador 2
                    self.atacar(i)
                    pass
            else:
                if self.cartas_j2 == []:
                    print('Gana J1')
                else:
                    print('Gana J2')
                break



juego = Juego(10)