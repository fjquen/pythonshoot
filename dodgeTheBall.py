import pygame
import time 
from time import sleep
from pygame.locals import *
from balle import Balle
from perso import Perso
from projectile import Projectile
from random import randint

#test pour push
pygame.init()
pygame.key.set_repeat(400, 30)
fenetre = pygame.display.set_mode((640, 480))
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond,(0,0))
perso = Perso("Perso.png", (270,380))
perso.image


continuer = True
listeBalles = []
listeTirs = []
test = 0

intervalFire = 0
clock = pygame.time.Clock()
while continuer :
    if len(listeBalles) < 3 and randint(1,500)<=3:
        listeBalles.append(Balle('golfBall.png',(randint(25,455),-25)))
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    dicKeys = pygame.key.get_pressed()
    if dicKeys[K_LEFT]:
       if perso.rect.left>=10 :
            perso.deplace(-1,0)
    if dicKeys[K_RIGHT]:
       if perso.rect.right<=630 :
            perso.deplace(1,0)
    dt = clock.tick() 
    intervalFire += dt
    if dicKeys[K_SPACE] and intervalFire >250:
        listeTirs.append(Projectile("tir.png",(perso.rect.left+15,perso.rect.top)))
        intervalFire = 0
    fenetre.blit(fond, (0,0))
    for tir in listeTirs :
        tir.deplace()
        if tir.rect.top <= 0 :
            listeTirs.remove(tir)
        tir.affiche(fenetre)
        
    for ball in listeBalles :
       ball.deplace()
       if ball.rect.top >= 480 :
            listeBalles.remove(ball)
       for tir in listeTirs :
              if ball.mask.overlap(tir.mask,(tir.rect.x-ball.rect.x,tir.rect.y-ball.rect.y)):
                 listeBalles.remove(ball)
       #else :
           #if ball.collision(perso.rect) :
               #continuer = False
       ball.affiche(fenetre)
    perso.affiche(fenetre)
    pygame.display.update()
pygame.quit()
