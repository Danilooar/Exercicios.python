""" DESAFIO: FAZER VALORES ALEATÓRIOS COM RANDOM 
DESAFIO: FAZER CORES ALEATÓRIAS COM RANDOM 

"""

import math
import random

print(random.randint(1,10))

Cores = ['azul', 'rosa', 'roxonubnk','verde']

print(random.choice(Cores) )



Moeda = ['cara', 'coroa']

print(random.choice(Moeda))


Rifa_participantes = ['Hugo', 'Batalha','Roger','WELL','JACK']

Vencedor = (random.choice(Rifa_participantes))

print ("---Vencedor da Rifa: " + Vencedor,"----") 

#imprimir um número de 10 a 100
print(random.randint(10,100))

