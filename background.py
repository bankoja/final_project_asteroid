import pygame

class Background:
    def __init__(self):
        self.image = pygame.image.load("bg.png").convert()
        self.rect = self.image.get_rect()
