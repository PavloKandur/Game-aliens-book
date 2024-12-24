import pygame

class Ship:
    '''Clas for managing a ship'''

    def __init__(self, ai_game):
        '''Creating a ship'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Download ship img
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        #Creatig new ship in the centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Create a ship'''
        self.screen.blit(self.image, self.rect)