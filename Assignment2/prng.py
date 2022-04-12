# Program that generates psuedo-random numbers (PRNG service)

import random
import time

random.seed()   #initialize rng

while True:
    time.sleep(1)       #sleep for one second
    #erase image-service file to clear it
    #image = open('image-service.txt', 'w')
    #imageNum = image.readline()


    prng = open('prng-service.txt', 'r')    #open prng-service.txt file
    entry = prng.readline()     #read file entry

    if entry == 'run':      #if entry file "run"
        randomNum = str(random.randint[1,3])    #generate random number 1-3
        #prng.seek(0)
        prng.write(randomNum)
    else:
        continue
    prng.close()