# Program that, given a non-negative integer i, returns the ith image in a set (order
# doesn't matter) (Image Service)
# If i is >= the number of images, modulo i by the size of the image set

import random
import time

while True:
    time.sleep(1)   #sleep for one second

    image = open('image-service.txt', 'r')  #open "image-service.txt"
    imageNum = image.readline()     #read file line as imageNum

    if imageNum.isnumeric():      #if line entry is numerical value
        time.sleep(1)
        imageNum = int(imageNum)
        path = open('image-service.txt', 'w')  #write in file
        path.write(f"/Users/RMC/PycharmProjects/CS-361/Assignment2/images/"
                   f"{imageNum}.jpg\n")     #write file path
        path.close()