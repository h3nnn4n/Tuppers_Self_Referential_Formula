#!/usr/bin/python2

import math
import decimal
import pygame
from pygame import gfxdraw

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)

def tupper(x, y):
    return 0.5 < ((y//17) // (2**(17*x + y%17)))%2

k = int(
        '9609393799189588849716729621278527547150043396'
        '6012930665150551927170280239526642468964284217'
        '4350718121267153782770623355993237280874144307'
        '8913259639413377234878577357498239266297155171'
        '7371699516523289053822161240323885586618401323'
        '5585136048828693337902491454229288667081096184'
        '4960917051834540678277315517054053816273809676'
        '0256562501698148208341878316384911559022561000'
        '3652351370343874461848378737238198224849863465'
        '0331594100549747005931383392264972494617515457'
        '2836670236974546101465599793379853748314378684'
        '1806593422227898388722980000748404719'
       )

pygame.init()
screen = pygame.display.set_mode(((115*2) + 10, (17*2) + 10))
pygame.display.set_caption('Tupper\'s Self-referential formula')

for y in range(k+0,k+17):
    for x in range(0,106):
        if tupper(x, y):
            col = WHITE
        else:
            col = BLACK

        i = 10 + 105 + (105 - x*2)
        j = 5 + ((y - k)*2)

        gfxdraw.pixel(screen, i    , j    , col)
        gfxdraw.pixel(screen, i + 1, j    , col)
        gfxdraw.pixel(screen, i    , j + 1, col)
        gfxdraw.pixel(screen, i + 1, j + 1, col)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.dict["key"] == 27):
            pygame.quit()
            exit()
