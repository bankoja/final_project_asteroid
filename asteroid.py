import pygame

class Asteroid(pygame.sprite.Sprite):

   def __init__(self, screen):
       super().__init__()
       self.frame = pygame.image.load("asteroid.jpg")
       self.rect = self.frame.get_rect()
       self.screen = screen
       self.speedx = 0
       self.speedy = 0


   def move(self):
       self.rect.x += self.speedx
       self.rect.y += self.speedy


