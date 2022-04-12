# A user interface (UI) that either has a button or can receive a user
# command. When
# the button is pushed or the command is entered...
# a.    UI calls the PRNG Service
# b.    UI calls the Image Service using the psuedo-random number from the PRNG Service
# c.    UI displays the image (or a path to it)

import time

while True:

    #request for input
    userinput = int(input("1 to generate new image or 2 to exit: "))
    if userinput == 1:
        #print("#1")
        prngwrite = open('prng-service.txt', 'w')    #open 'prng-service.txt' file
        #print("#2")
        prngwrite.write('run')                     #write 'run' in file
        #print("#3")
        prngwrite.close()
        #print("#4")
        time.sleep(5)                           #sleep five sec for prng.py

        #print("#5")
        prngread = open('prng-service.txt', 'r')        #read the random number generated
        #print("#6")
        number = prngread.readline()
        #print("#7")
        #print(number)
        prngread.close()

        #print("#8")
        imagewrite = open('image-service.txt', 'w')
        #print("#9")
        imagewrite.write(number)
        #print("#10")
        imagewrite.close()
        #print("#11")
        time.sleep(5)

        #print("#12")
        readandoutput = open('image-service.txt', 'r')
        #print("#13")
        writepath = readandoutput.readline()
        #print("#14")
        readandoutput.close()
        #print("#15")
        print(f"{writepath}")

        clearprng = open('prng-service.txt', 'w')
        clearprng.close()
        clearimage = open('image-service.txt', 'w')
        clearimage.close()

    elif userinput == 2:
        exit

    else:
        print(f"try again\n")
