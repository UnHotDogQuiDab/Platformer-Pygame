import pygame
from World import screen


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                action = True
                self.clicked = True
                return action
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        screen.blit(self.image, self.rect)
        return action
