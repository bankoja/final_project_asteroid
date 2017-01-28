# James Bankole 1/24/17 Final Project
import pygame

class Background:
    def __init__(self):
        """This class creates the background used in the game"""
        self.image = pygame.image.load("bg.png").convert()
        self.rect = self.image.get_rect()
