import pygame


class Projectile(pygame.sprite.Sprite):

   def __init__(self, angle):
       super().__init__()

       self.orb = pygame.Surface((10,10))
       self.rect = self.orb.get_rect()
       self.orb.fill((255,0,0))
       self.angle = angle
       if self.angle < 30:
           self.speedy = -3
           self.speedx = 0
       if self.angle == 30:
           self.speedy = -3
           self.speedx = -1.5
       if self.angle == 60:
           self.speedy = -3
           self.speedx = -3
       if self.angle == 90:
           self.speedy = 0
           self.speedx = -3

       if self.angle == 120:
           self.speedy = 3
           self.speedx = -3
       if self.angle == 150:
           self.speedy = 3
           self.speedx = -1
       if self.angle == 180:
           self.speedy = 3
           self.speedx = 0

       if self.angle == 210:
           self.speedy = 3
           self.speedx = 3
       if self.angle == 240:
           self.speedy = 2
           self.speedx = 3
       if self.angle == 270:
           self.speedy = 0
           self.speedx = 3

       if self.angle == 300:
           self.speedy = -1
           self.speedx = 3
       if self.angle == 330:
           self.speedy = -3
           self.speedx = 3
       if self.angle == 360:
           self.speedy = -3
           self.speedx = 0


   def move(self):
       self.rect.x += self.speedx
       self.rect.y += self.speedy

   def projectileCollide(self, spriteGroup):
       if pygame.sprite.spritecollide(self, spriteGroup, True):
           return True
