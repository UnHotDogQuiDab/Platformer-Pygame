import pygame
from World import screen, spike_group, blocker_group, locker_group, platform_up_group, key_group, exit_door_group, screen_height
from Trigger import locked


class Player:
    def __init__(self, x, y, world):
        self.reset(x, y, world)

    def reset(self, x, y, world):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for i in range(1, 5):
            player_img_right = pygame.image.load(f'Usefull_img/GUY/guy{i}.png')
            player_img_right = pygame.transform.scale(player_img_right, (45, 90))
            player_img_left = pygame.transform.flip(player_img_right, True, False)
            self.images_left.append(player_img_left)
            self.images_right.append(player_img_right)
        self.image = self.images_right[self.index]
        player_image_death = pygame.image.load(f'Usefull_img/GUY/guy_death.png')
        self.image_death = pygame.transform.scale(player_image_death, (90, 45))
        self.rect_death = self.image_death.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 1
        self.world = world

    def update(self, game_over):
        dx = 0
        dy = 0
        calm_down = 5

        # Mort
        if game_over == -1:
            self.rect_death.x = self.rect.x - 45
            self.rect_death.y = self.rect.y + 50
            self.image = self.image_death
            rect_affichage = [self.rect_death.x - self.world.offset.x, self.rect_death.y - self.world.offset.y]
            screen.blit(self.image, rect_affichage)
            return game_over

        # Touches
        key = pygame.key.get_pressed()
        if (key[pygame.K_z] or key[pygame.K_UP]) and not self.jumped:
            self.vel_y -= 15
            self.jumped = True

        if key[pygame.K_q] or key[pygame.K_LEFT]:
            dx -= 5
            self.direction = -1
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            dx += 5
            self.direction = 1

        if not (key[pygame.K_q] or key[pygame.K_LEFT]) and not (key[pygame.K_d] or key[pygame.K_RIGHT]):
            self.counter = 0
            self.index = 0
            if self.direction == -1:
                self.image = self.images_left[self.index]
            if self.direction == 1:
                self.image = self.images_right[self.index]

        # Animations
        self.counter += 1
        if self.counter > calm_down:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == -1:
                self.image = self.images_left[self.index]
            if self.direction == 1:
                self.image = self.images_right[self.index]

        # Gravit??
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # Collisions
        for tile in self.world.tile_list:
            if (tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height) and tile[2] != 0) or self.rect.x + dx < 0:
                dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height) and tile[2] != 0:
                for i in platform_up_group:
                    if i.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                        return -1
                    if i.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                        return -1
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.jumped = False
                    self.vel_y = 0

        if self.rect.y+dy >= screen_height:
            return -1

        # Ennemies/hazards/key
        if pygame.sprite.spritecollide(self, spike_group, False):
            return -1
        if pygame.sprite.spritecollide(self, blocker_group, False):
            return -1
        if pygame.sprite.spritecollide(self, exit_door_group, False):
            return 1

        for keys in key_group:
            if keys.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                if keys.idKey not in locked:
                    locked.append(keys.idKey)

        for i in platform_up_group:
            if i.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if i.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.vel_y < 0:
                    dy = i.rect.bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    dy = i.rect.top - self.rect.bottom-1
                    self.jumped = False
                    self.vel_y = 0

        for i in locker_group:
            if i.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if i.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.vel_y < 0:
                    dy = i.rect.bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    dy = i.rect.top - self.rect.bottom-1
                    self.jumped = False
                    self.vel_y = 0

        # Affichage
        self.rect.x += dx
        self.rect.y += dy
        offset = self.world.offset
        rect_affichage = [self.rect.x - offset.x, self.rect.y - offset.y]
        screen.blit(self.image, rect_affichage)
        return game_over
