import pygame


class Projectile :
    def __init__(self, image, top) :
            self.image = pygame.image.load(image).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topleft = top
            
    def affiche(self, fenetre):
            fenetre.blit(self.image, self.rect)
            
    def deplace(self) :
            self.rect = self.rect.move(0,-1)
