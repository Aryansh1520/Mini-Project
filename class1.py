import pygame
import time as t 
class giveposition():
    def position(positionof,dienumber,player,screen):
        l1 = [91,92,93,94,95,96,97,98,99,100]
        l2 = [81,82,83,84,85,86,87,88,89,90]
        l3 = [71,72,73,74,75,76,77,78,79,80]
        l4 = [61,62,63,64,65,66,67,68,69,70]
        l5 = [51,52,53,54,55,56,57,58,59,60]
        l6 = [41,42,43,44,45,46,47,48,49,50]
        l7 = [31,32,33,34,35,36,37,38,39,40]
        l8 = [21,22,23,24,25,26,27,28,29,30]
        l9 = [11,12,13,14,15,16,17,18,19,20]
        l10 = [1,2,3,4,5,6,7,8,9,10]

        positionof = positionof+dienumber
#Ladders
        if  positionof == 5:
            lx = 10 + (l7.index(32)*65)
            ly = 405
            positionof = 32
        elif positionof == 75:
            lx = 10 + (l1.index(97)*65)
            ly = 15
            positionof = 97
        elif positionof == 59:
            lx = 10 + (l1.index(99)*65)
            ly = 15
            positionof = 99
#Snakes
        elif positionof ==91:
            lx = 10 + (l5.index(54)*65)
            ly = 275
            positionof = 54

        elif positionof == 78:
            lx = 10+(l5.index(55)*65)
            ly = 275
            positionof = 55

        elif positionof == 36:
            lx = 10+(l8.index(25)*65)
            ly = 470
            positionof = 25

        elif positionof == 40:
            lx = 10+(l9.index(19)*65)
            ly = 535
            positionof = 19

        elif positionof >100:
            positionof = 100 - (positionof -100)
            lx = 10 + (l1.index(positionof)*65)
            ly = 15
        elif positionof == 100:
            lx = 10+(l1.index(positionof)*65)
            ly = 15
            if player == "blue":
                print("Blue Won!Closing in 5 seconds")
                t.sleep(5)
                quit()
            else:
                lx = 10+(l1.index(positionof)*65)
                ly = 15
                print("Yellow Won! Closing in 5 seconds")
                t.sleep(5)
                quit()

        else:

            if positionof in l10:
                lx = 10+(l10.index(positionof)*65)
                ly = 600
            elif positionof in l9:
                lx = 10+(l9.index(positionof)*65)
                ly = 535
            elif positionof in l8:
                lx = 10+(l8.index(positionof)*65)
                ly = 470
            elif positionof in l7:
                lx = 10+(l7.index(positionof)*65)
                ly = 405
            elif positionof in l6:
                lx = 10+(l6.index(positionof)*65)
                ly = 340
            elif positionof in l5:
                lx = 10+(l5.index(positionof)*65)
                ly = 275
            elif positionof in l4:
                lx = 10+(l4.index(positionof)*65)
                ly = 210
            elif positionof in l3:
                lx = 10+(l3.index(positionof)*65)
                ly = 115
            elif positionof in l2:
                lx = 10+(l2.index(positionof)*65)
                ly =80
            elif positionof in l1:
                lx = 10+(l1.index(positionof)*65)
                ly = 15
  
        print(player," : ",positionof)
        return lx,ly,positionof




