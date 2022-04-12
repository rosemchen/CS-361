# Program that, given a non-negative integer i, returns the ith image in a set (order
# doesn't matter) (Image Service)
# If i is >= the number of images, modulo i by the size of the image set

import time

while True:
    #print("#31")
    time.sleep(1)   #sleep for one second

    #print("#32")
    image = open('image-service.txt', 'r')  #open "image-service.txt"
    #print("#33")
    imageNum = image.readline()     #read file line as imageNum

    image.close()

    #print("#34")
    if imageNum.isnumeric():      #if line entry is numerical value
        #print("#35")
        time.sleep(1)
        #print("#36")
        imageNum = int(imageNum)
        #print("#37")
        path = open('image-service.txt', 'w')  #write in file
        #print("#38")
        path.write(f"/Users/RMC/PycharmProjects/CS-361/Assignment2/images/"
                   f"{imageNum}.jpeg\n")     #write file path
        #print("#39")
        path.close()