import pygame
from random import randint

class Balle :
    def __init__(self, image, center) :
        """ Initialisation d'un objet de classe Balle a partir de deux arguments :
    - image est l'adresse relative ou absolue de l'image voulue pour l'objet ;
    - center est un tuple de deux entiers donnant la position du centre de la balle lors de
    sa création."""

        self.image = pygame.image.load(image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.balle_mask = self.mask.to_surface()
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.vitesse = randint(1,2)

    def affiche(self, fenetre) :
        fenetre.blit(self.balle_mask, self.rect)

    def deplace(self) :
        self.rect = self.rect.move(0,self.vitesse)


    def collision(self, targetRect) :
        return self.rect.colliderect(targetRect)                    
