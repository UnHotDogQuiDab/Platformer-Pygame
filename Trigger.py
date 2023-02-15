import pygame
locked = []


class Exit_door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'Usefull_img/window.png')
        self.image = pygame.transform.scale(self.image, (54, 75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 23


class Key(pygame.sprite.Sprite):
    def __init__(self, x, y, idKey):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'Usefull_img/keyYellow.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.idKey = idKey

    def update(self):
        if self.idKey in locked:
            return True
        return False


class Locker(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'Usefull_img/lock_yellow.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
