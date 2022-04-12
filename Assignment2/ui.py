# A user interface (UI) that either has a button or can receive a user command. When
# the button is pushed or the command is entered...
# a.    UI calls the PRNG Service
# b.    UI calls the Image Service using the psuedo-random number from the PRNG Service
# c.    UI displays the image (or a path to it)

import time

while True:

    #request for input
    userinput = input("1 to generate new image or 2 to exit: ")
    if userinput == 1:
        prngwrite = open('prng-service.txt', 'w')    #open 'prng-service.txt' file
        prngwrite.write('run')                     #write 'run' in file
        prngwrite.close()
        time.sleep(5)                           #sleep five sec for prng.py

        prngread = open('prng-service.txt', 'r')        #read the random number generated
        number = prngread.readline()
        prngread.close()

        imagewrite = open('image-service.txt', 'w')
        imagewrite.write(number)
        imagewrite.close()
        time.sleep(5)

        readandoutput = open('image-service.txt', 'r')
        writepath = readandoutput.readline()
        readandoutput.close()
        print(f"{filepath}")

    elif input == 2:
        exit

    else:
        print(f"try again\n")

