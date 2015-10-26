#!/usr/bin/python

import math
import decimal
import pygame
from pygame import gfxdraw

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)

def tupper(x, y):
    return 0.5 < ((y//17) // (2**(17*x + y%17)))%2

k = 960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719

pygame.init()
screen = pygame.display.set_mode((800,600))

for y in range(k+0,k+17):
    for x in range(0,106):
        if tupper(x, y):
            col = WHITE
            #print("X", end = '')
            #print(x,y-k,1)
        else:
            col = BLACK
            #print(x,y-k,0)
            #print(" ", end = '')

        i = 200+ (300-x*2)
        j = 200+ ((y-k)*2)
        gfxdraw.pixel(screen, i, j, col)
        gfxdraw.pixel(screen, i+1, j, col)
        gfxdraw.pixel(screen, i, j+1, col)
        gfxdraw.pixel(screen, i+1, j+1, col)
    #print("")

pygame.display.flip()

while (True):
    pass

pygame.quit()
