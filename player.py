# James Bankole 1/24/17 Final Project
import pygame

class Player(pygame.sprite.Sprite):

   def __init__(self):
      """This class creates the player/spaceship. It has the method necessary for the rotation of the spaceship. It also makes the
      spaceship respond to collisions."""
       super().__init__()
       self.frame = pygame.image.load("spaceship.png")
       self.updated = self.frame
       self.rect = self.frame.get_rect()
       self.angle = 0
       self.angleIncrement = 30

   def rotate(self):
       self.angle += self.angleIncrement
       self.angle = self.angle % 360
       self.updated = pygame.transform.rotate(self.frame, self.angle)
       rot_rect = self.rect.copy()
       rot_rect.center = self.updated.get_rect().center
       self.updated = self.updated.subsurface(rot_rect).copy()

   def rotateR(self):
       self.angle -= self.angleIncrement
       self.angle = self.angle % 360
       self.updated = pygame.transform.rotate(self.frame, self.angle)
       rot_rect = self.rect.copy()
       rot_rect.center = self.updated.get_rect().center
       self.updated = self.updated.subsurface(rot_rect).copy()

   def playerCollide(self, spriteGroup):
       if pygame.sprite.spritecollide(self, spriteGroup, False):
           return True



