import pygame
import random
import time as t
from sys import exit
from pygame import *
from class1 import giveposition as gp
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 16)
font2 = pygame.font.Font('freesansbold.ttf', 20)
bx , by = 700,550
rx , ry = 700,600
white = (200,200,200)

positionred = 0
positionblue = 0

def blueroll():
    msg1 = font2.render("Your Turn",True,(0,0,255))
    screen.blit(msg1,[690,70])
    
def redroll():
    msg = font2.render("Your Turn",True,(255,0,0))
    screen.blit(msg,[690,180])


def game(player1name,player2name):
    global screen , bx , by , rx , ry , diceroll , dice1 , positionred , positionblue
    turn = "blue"
    while True:

        screen = pygame.display.set_mode((855,650))
        screen.blit(dice1,(720,300))           
        pygame.display.set_caption("Snakes and ladders")
        screen.blit(bg,(0,0))
        screen.blit(text,textRect)
        screen.blit(text1,textRect1)
        screen.blit(player1_image,(820,35))
        screen.blit(player2_image,(820,145))




        if turn =="blue":
            blueroll()
        else:
            redroll()      
        def blue_player():
            screen.blit(blue,(bx,by))

        def red_player():
            screen.blit(red,(rx,ry))
        blue_player()
        red_player()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button.collidepoint(mouse_pos):
                    dice,diceroll = pick_number()
                    screen.blit(dice,(730,440))
                    if pick_number and turn == "red":
                        turn = "blue"
                        if diceroll == 6  and rx ==700 and ry ==600:
                            rx,ry = 10,600
                            positionred = 1
                        elif (positionred >= 1 and positionred<100 )and diceroll!=6:
                            rx,ry,positionred = gp.position(positionred,diceroll,"Yellow")
                        elif (positionred >= 1 and positionred<100 )and diceroll==6:
                            rx,ry,positionred = gp.position(positionred,diceroll,"Yellow")
                            turn = "red"




                    elif pick_number and turn == "blue":
                        turn = "red"
                        if diceroll == 6 and bx == 700 and by == 550:
                            bx,by = 30,600
                            positionblue = 1
                        elif (positionblue >= 1 and positionblue<100) and diceroll!=6:
                            bx,by,positionblue = gp.position(positionblue,diceroll,"Blue")
                        elif (positionblue >= 1 and positionblue<100) and diceroll==6:
                            bx,by,positionblue = gp.position(positionblue,diceroll,"Blue")
                            turn = "blue"



        t.sleep(0.5)
        pygame.display.update()




def pick_number():
    global diceroll
    diceroll = random.randint(1,6)
    if diceroll == 1:
        dice = pygame.image.load(r".\assets\one.png")
        dice = pygame.transform.scale(dice,size)

    elif diceroll == 2:
        dice = pygame.image.load(r".\assets\two.png")
        dice = pygame.transform.scale(dice,size)

    elif diceroll == 3:
        dice = pygame.image.load(r".\assets\three.png")
        dice = pygame.transform.scale(dice,size)

    elif diceroll == 4:
        dice = pygame.image.load(r".\assets\four.png")
        dice = pygame.transform.scale(dice,size)

    elif diceroll == 5:
        dice = pygame.image.load(r".\assets\five.png")
        dice = pygame.transform.scale(dice,size)

    elif diceroll == 6:
        dice = pygame.image.load(r".\assets\six.png")
        dice = pygame.transform.scale(dice,size)

    return (dice,diceroll)


bg = pygame.image.load(r".\assets\board_image.png")
bg = pygame.transform.scale(bg,(650,650))

player1_image = pygame.image.load(r".\assets\ellipse.png")
player2_image = pygame.image.load(r".\assets\record.png")

player1_image = pygame.transform.scale(player1_image,(30,30))
player2_image = pygame.transform.scale(player2_image,(30,30))


player1name , player2name = input("Enter Player 1 and Player 2 name with space between them\n").split()
player1name = "Player 1 : "+ player1name
player2name = "Player 2 : "+ player2name

text = font.render(player1name, True, "WHITE", "BLACK")
textRect = text.get_rect()

text1 = font.render(player2name, True,"WHITE", "BLACK")
textRect1 = text.get_rect()



dice1 = pygame.image.load(r".\assets\dice.png")
dice1 = pygame.transform.scale(dice1,(80,80))

textRect.center = (730,50)
textRect1.center = (730,160)

text2 = font.render("player 2 won!", True,"WHITE", "BLACK")
textRect2 = text.get_rect()
text3 = font.render("player 1 won!", True,"WHITE", "BLACK")
textRect3 = text.get_rect()
textRect2.center = (730,240)
textRect3.center = (730,190)

button = pygame.Rect(720,300,100,100)

size = (45,45)

blue = pygame.image.load(r".\assets\blueplayer.png")
blue = pygame.transform.scale(blue,(32,32))
red = pygame.image.load(r".\assets\redplayer.png")
red = pygame.transform.scale(red,(30,30))

game(player1name,player2name)







