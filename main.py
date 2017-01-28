# James Bankole 1/24/17 Final Project
import pygame, sys

from pygame.locals import *

import background

import player

import asteroid

import laser

def main():
   # Constants that will be used in the program
   APPLICATION_WIDTH = 670
   APPLICATION_HEIGHT = 670
   
   mainSurface = pygame.display.set_mode((APPLICATION_HEIGHT, APPLICATION_WIDTH), 0, 32)
   pygame.display.set_caption("ASTEROID ANNIHILATOR")

   backG = background.Background()
   mainSurface.blit(backG.image, (0,0))

   mainCharacter = player.Player()
   mainSurface.blit(mainCharacter.frame, (APPLICATION_HEIGHT / 2, APPLICATION_WIDTH / 2))


   projectileGroup = pygame.sprite.Group()
   projectileGroupTwo = pygame.sprite.Group()
   projectileGroupThree = pygame.sprite.Group()
   projectileGroupFour = pygame.sprite.Group()
   projectileGroupFive = pygame.sprite.Group()
   projectileGroupSix = pygame.sprite.Group()
   projectileGroupSeven = pygame.sprite.Group()
   projectileGroupEight = pygame.sprite.Group()


   def reblitA():
       projectile = asteroid.Asteroid(mainSurface)
       projectile.rect.x = APPLICATION_WIDTH / 2
       projectile.rect.y = -250
       projectile.speedy = 1
       projectile.speedx = 0
       projectileGroup.add(projectile)

   def reblitA2():
       projectileTwo = asteroid.Asteroid(mainSurface)
       projectileTwo.rect.x = -750
       projectileTwo.rect.y = -750
       projectileTwo.speedy = 1
       projectileTwo.speedx = 1
       projectileGroupTwo.add(projectileTwo)

   def reblitA3():
       projectileThree = asteroid.Asteroid(mainSurface)
       projectileThree.rect.x = -1300
       projectileThree.rect.y = APPLICATION_HEIGHT / 2
       projectileThree.speedy = 0
       projectileThree.speedx = 1
       projectileGroupThree.add(projectileThree)

   def reblitA4():
       projectileFour = asteroid.Asteroid(mainSurface)
       projectileFour.rect.x = -2000
       projectileFour.rect.y = APPLICATION_HEIGHT + 2000
       projectileFour.speedy = -1
       projectileFour.speedx = 1
       projectileGroupFour.add(projectileFour)

   def reblitA5():
       projectileFive = asteroid.Asteroid(mainSurface)
       projectileFive.rect.x = APPLICATION_WIDTH / 2
       projectileFive.rect.y = APPLICATION_HEIGHT + 2600
       projectileFive.speedy = -1
       projectileFive.speedx = 0
       projectileGroupFive.add(projectileFive)

   def reblitA6():
       projectileSix = asteroid.Asteroid(mainSurface)
       projectileSix.rect.x = APPLICATION_WIDTH + 3300
       projectileSix.rect.y = APPLICATION_HEIGHT + 3300
       projectileSix.speedy = -1
       projectileSix.speedx = -1
       projectileGroupSix.add(projectileSix)

   def reblitA7():
       projectileSeven = asteroid.Asteroid(mainSurface)
       projectileSeven.rect.x = APPLICATION_WIDTH + 4000
       projectileSeven.rect.y = APPLICATION_HEIGHT / 2
       projectileSeven.speedy = 0
       projectileSeven.speedx = -1
       projectileGroupSeven.add(projectileSeven)

   def reblitA8():
       projectileEight = asteroid.Asteroid(mainSurface)
       projectileEight.rect.x = APPLICATION_WIDTH + 4500
       projectileEight.rect.y = -6500
       projectileEight.speedy = 1
       projectileEight.speedx = -1
       projectileGroupEight.add(projectileEight)

   hasFired = False


   reblitA()
   reblitA2()
   reblitA3()
   reblitA4()
   reblitA5()
   reblitA6()
   reblitA7()
   reblitA8()

   pygame.display.update()

   while True:
       for event in pygame.event.get():
           if event.type == QUIT:
               pygame.quit()
               sys.exit()
           keys = pygame.key.get_pressed()
           if keys[pygame.K_LEFT]:
               mainCharacter.rotate()
           if keys[pygame.K_RIGHT]:
               mainCharacter.rotateR()
           if keys[pygame.K_SPACE]:
               beam = laser.Projectile(mainCharacter.angle)
               beam.rect.x = APPLICATION_HEIGHT / 2
               beam.rect.y = APPLICATION_WIDTH / 2
               hasFired = True


       mainSurface.blit(backG.image,(0,0))

       for aprojectile in projectileGroup:
           aprojectile.move()
           mainSurface.blit(aprojectile.frame, aprojectile.rect)

       for aprojectile in projectileGroupTwo:
           aprojectile.move()
           mainSurface.blit(aprojectile.frame, aprojectile.rect)

       for aprojectile in projectileGroupThree:
           aprojectile.move()
           mainSurface.blit(aprojectile.frame, aprojectile.rect)

       for aprojectile in projectileGroupFour:
           aprojectile.move()
           mainSurface.blit(aprojectile.frame, aprojectile.rect)

       for aprojectile in projectileGroupFive:
           aprojectile.move()
           mainSurface.blit(aprojectile.frame, aprojectile.rect)

       for aprojectile in projectileGroupSix:
           aprojectile.move()
           mainSurface.blit(aprojectile.frame, aprojectile.rect)

       for aprojectile in projectileGroupSeven:
           aprojectile.move()
           mainSurface.blit(aprojectile.frame, aprojectile.rect)

       for aprojectile in projectileGroupEight:
           aprojectile.move()
           mainSurface.blit(aprojectile.frame, aprojectile.rect)


       if hasFired:
           beam.move()
           mainSurface.blit(beam.orb, beam.rect)

           for projectile in projectileGroup:
               if beam.projectileCollide(projectileGroup):
                   reblitA()
               if mainCharacter.playerCollide(projectileGroup):
                   print("hello")
                   pygame.time.wait(2000)
                   pygame.quit()
                   sys.exit()

           for projectileTwo in projectileGroupTwo:
               if beam.projectileCollide(projectileGroupTwo):
                   reblitA2()
               if mainCharacter.playerCollide(projectileGroupTwo):
                   pygame.time.wait(2000)
                   pygame.quit()
                   sys.exit()

           for projectileThree in projectileGroupThree:
               if beam.projectileCollide(projectileGroupThree):
                   reblitA3()
               if mainCharacter.playerCollide(projectileGroupThree):
                   pygame.time.wait(2000)
                   pygame.quit()
                   sys.exit()

           for projectileFour in projectileGroupFour:
               if beam.projectileCollide(projectileGroupFour):
                   reblitA4()
               if mainCharacter.playerCollide(projectileGroupFour):
                   pygame.time.wait(2000)
                   pygame.quit()
                   sys.exit()

           for projectileFive in projectileGroupFive:
               if beam.projectileCollide(projectileGroupFive):
                   reblitA5()
               if mainCharacter.playerCollide(projectileGroupFive):
                   pygame.time.wait(2000)
                   pygame.quit()
                   sys.exit()

           for projectileSix in projectileGroupSix:
               if beam.projectileCollide(projectileGroupSix):
                   reblitA6()
               if mainCharacter.playerCollide(projectileGroupSix):
                   pygame.time.wait(2000)
                   pygame.quit()
                   sys.exit()

           for projectileSeven in projectileGroupSeven:
               if beam.projectileCollide(projectileGroupSeven):
                   reblitA7()
               if mainCharacter.playerCollide(projectileGroupSeven):
                   pygame.time.wait(2000)
                   pygame.quit()
                   sys.exit()

           for projectileEight in projectileGroupEight:
               if beam.projectileCollide(projectileGroupEight):
                   reblitA8()
               if mainCharacter.playerCollide(projectileGroupEight):
                   pygame.time.wait(2000)
                   pygame.quit()
                   sys.exit()


       mainSurface.blit(mainCharacter.updated, (APPLICATION_HEIGHT / 2, APPLICATION_WIDTH / 2))


       pygame.display.update()

main()
