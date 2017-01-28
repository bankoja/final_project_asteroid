# James Bankole 1/24/17 Final Project
import pygame

class Asteroid(pygame.sprite.Sprite):

   def __init__(self, screen):
      """This class creates the asteroids used in the game."""
       super().__init__()
       self.frame = pygame.image.load("asteroid.jpg")
       self.rect = self.frame.get_rect()
       self.screen = screen
       self.speedx = 0
       self.speedy = 0


   def move(self):
       self.rect.x += self.speedx
       self.rect.y += self.speedy


