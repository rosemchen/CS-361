# Program that generates psuedo-random numbers (PRNG service)

import random
import time

random.seed()   #initialize rng
while True:
    #print("#21")
    time.sleep(1)       #sleep for one second
    #print("#22")
    prng = open('prng-service.txt', 'r')    #open prng-service.txt file
    #print("#23")
    entry = prng.readline()     #read file entry
    prng.close()
    if entry == 'run':
        break

#erase image-service file to clear it
#image = open('image-service.txt', 'w')
#imageNum = image.readline()


prng1 = open('prng-service.txt', 'w')
#print("#24")
#print(entry)
if entry == 'run':      #if entry file "run"
    #print("#25")
    randomNum = str(random.randint(1,3))    #generate random number 1-3
    #prng.seek(0)
    #print("#26")
    #print(randomNum)
    prng1.write(randomNum)
prng1.close()