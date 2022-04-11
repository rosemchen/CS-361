# Program that generates psuedo-random numbers (PRNG service)

import random
import time

random.seed()

while True:
    time.sleep(1)

    prng = open('prng-service.txt', 'r')
    entry = prng.readline()

    if entry == 'run':
        randomNum = str(random.randint[1,3])
        prng.seek(0)
        prng.write(randomNum)
    else:
        continue
    prng.close()