import pygame


class Perso :
    def __init__(self, image,left):
            self.image = pygame.image.load(image).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topleft = left
    
    def affiche(self, fenetre):
            fenetre.blit(self.image, self.rect)
            
    def deplace(self,x,y):
            self.rect = self.rect.move(x,y)
