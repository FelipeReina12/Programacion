import random as rand

for i in range(0, 5):
    n = rand.randint(10, 20)               #Numeros aleatorios enteros
    r = round(rand.uniform(10, 20), 2)     #Numeros aleatorios decimales
    l = rand.choice('Murcielago')          #Letras aleatorias de un string establecido
    print(n, end= '   ')
    print(r, end= '   ')
    print(l, '\n')

