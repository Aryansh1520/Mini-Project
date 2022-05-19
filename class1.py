import time as t 
class giveposition():
    def position(positionof,dienumber,player):
        l1 = [100,99,98,97,96,95,94,93,92,91]
        l2 = [81,82,83,84,85,86,87,88,89,90]
        l3 = [80,79,78,77,76,75,74,73,72,71]
        l4 = [61,62,63,64,65,66,67,68,69,70]
        l5 = [60,59,58,57,56,55,54,53,52,51]
        l6 = [41,42,43,44,45,46,47,48,49,50]
        l7 = [40,39,38,37,36,35,34,33,32,31]
        l8 = [21,22,23,24,25,26,27,28,29,30]
        l9 = [20,19,18,17,16,15,14,13,12,11]
        l10 = [1,2,3,4,5,6,7,8,9,10]
        print(player," die number : " ,dienumber)
        positionof = positionof+dienumber
#Ladders
        if  positionof == 10:#done
            lx = 10 + (l7.index(33)*65)
            ly = 405
            print(player,"climbed from 10 to 33")
            positionof = 33
        elif positionof == 16:#done
            lx = 10 + (l7.index(37)*65)
            ly = 405
            positionof = 37
            print(player,"climbed from 16 to 37")

        elif positionof == 21:#done
            lx = 10 + (l6.index(41)*65)
            ly = 340
            positionof = 41
            print(player,"climbed from 21 to 41")

        elif positionof ==35:#done
            lx = 10 + (l5.index(54)*65)
            ly = 275
            positionof = 54
            print(player,"climbed from 35 to 54")

        elif positionof == 44:#done
            lx = 10+(l3.index(76)*65)
            ly = 115
            positionof = 76
            print(player,"climbed from 44 to 76")

        elif positionof == 80:#done
            lx = 10+(l1.index(99)*65)
            ly = 15
            positionof = 99
            print(player,"climbed from 80 to 99")


#snakes
        elif positionof == 23:#done
            lx = 10+(l10.index(2)*65)
            ly = 600
            positionof = 2
            print(player,"was cut at 23 and placed at 2")

        elif positionof == 34:#done
            lx = 10+(l9.index(15)*65)
            ly = 535
            positionof = 15
            print(player,"was cut at 34 and placed at 15")

        elif positionof == 52:
            lx = 10+(l7.index(31)*65)
            ly = 405
            positionof = 31
            print(player,"was cut at 52 and was placed at 31")

        elif positionof == 62:
            lx = 10+(l6.index(43)*65)
            ly = 405
            positionof = 43
            print(player,"was cut 62 and placed at 43")

        elif positionof == 89:
            lx = 10+(l4.index(68)*65)
            ly = 210
            positionof = 68
            print(player,"was cut at 89 and placed at 68")

        elif positionof == 95:
            lx = 10+(l3.index(74)*65)
            ly = 115
            positionof = 74
            print(player,"was cut 95 and placed at 74")




        elif positionof >100:
            positionof = 100 - (positionof -100)
            lx = 10 + (l1.index(positionof)*65)
            ly = 15

        elif positionof == 100:
            lx = 10+(l1.index(positionof)*65)
            ly = 15
            if player == "blue":
                print("**********Blue Won!Closing in 5 seconds**********")
                t.sleep(5)
                quit()
            else:
                lx = 10+(l1.index(positionof)*65)
                ly = 15
                print("**********Yellow Won! Closing in 5 seconds**********")
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




