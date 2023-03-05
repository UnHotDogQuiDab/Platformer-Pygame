import pygame
import pytmx
from Enemy import Enemy
from Hazards import Spike, Platform_up
from Trigger import Key, Exit_door, Locker, locked

tile_size = 50
screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

world_data = []
platform_up_group = []
key_group = []
locker_group = []
blocker_group = []
spike_group = []
exit_door_group = []

tmx_data = pytmx.util_pygame.load_pygame(f'level_data/level_1.tmx')
player_position_x = (tmx_data.get_object_by_name("Player_spawn").x/64)*tile_size
player_position_y = (tmx_data.get_object_by_name("Player_spawn").y/64)*tile_size
border_x = tmx_data.get_object_by_name("Border").x


def get_pos_player(level):
    tmx_data = pytmx.util_pygame.load_pygame(f'level_data/level_{level}.tmx')
    player_position_x = (tmx_data.get_object_by_name("Player_spawn").x / 64) * tile_size
    player_position_y = (tmx_data.get_object_by_name("Player_spawn").y / 64) * tile_size
    return [player_position_x, player_position_y]


def reset_level(level):
    global world_data
    global player_position_x
    global player_position_y
    global border_x
    world_data = []
    tmx_data = pytmx.util_pygame.load_pygame(f'level_data/level_{level}.tmx')
    player_position_x = (tmx_data.get_object_by_name("Player_spawn").x/64) * tile_size
    player_position_y = (tmx_data.get_object_by_name("Player_spawn").y/64) * tile_size
    border_x = tmx_data.get_object_by_name("Border").x - 20 * 64
    for layer in tmx_data:
        if layer.name == 'Usefull':
            data = layer.data
            for i in range(len(layer.data)):
                world_data.append([])
                row = data[i]
                for j in range(len(layer.data[i])):
                    value = row[j]
                    world_data[i].append(value)


class World:
    def __init__(self):
        locked.clear()
        platform_up_group.clear()
        blocker_group.clear()
        spike_group.clear()
        key_group.clear()
        locker_group.clear()
        exit_door_group.clear()
        self.tile_list = []
        self.offset = pygame.math.Vector2()

        sky_img = pygame.image.load('Usefull_img/bg.png')
        grass_img = pygame.image.load('Usefull_img/grassMid.png')
        dirt_img = pygame.image.load('Usefull_img/grassCenter.png')

        row_count = 0

        for rows in world_data:
            col_count = 0
            for tile in rows:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, 1)
                    self.tile_list.append(tile)
                elif tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, 1)
                    self.tile_list.append(tile)

                elif tile == 3:
                    blocker = Enemy(col_count * tile_size, row_count * tile_size + 10)
                    blocker_group.append(blocker)

                    img = pygame.transform.scale(sky_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, 0)
                    self.tile_list.append(tile)

                elif tile == 4:
                    spike = Spike(col_count * tile_size, row_count * tile_size)
                    spike_group.append(spike)

                    img = pygame.transform.scale(sky_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, 0)
                    self.tile_list.append(tile)

                elif tile == 5:
                    platform_up = Platform_up(col_count * tile_size, row_count * tile_size)
                    platform_up_group.append(platform_up)

                    img = pygame.transform.scale(sky_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, 0)
                    self.tile_list.append(tile)

                elif tile == 6:
                    yellow_key = Key(col_count * tile_size, row_count * tile_size, 1)
                    key_group.append(yellow_key)

                    img = pygame.transform.scale(sky_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, 0)
                    self.tile_list.append(tile)

                elif tile == 7:
                    yellow_locker = Locker(col_count * tile_size, row_count * tile_size)
                    locker_group.append(yellow_locker)

                    img = pygame.transform.scale(sky_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, 0)
                    self.tile_list.append(tile)

                elif tile == 8:
                    exit_door = Exit_door(col_count * tile_size, row_count * tile_size)
                    exit_door_group.append(exit_door)

                    img = pygame.transform.scale(sky_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, 0)
                    self.tile_list.append(tile)

                else:
                    img = pygame.transform.scale(sky_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, 0)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self, player):
        self.offset = pygame.math.Vector2()
        self.offset.x = player.rect.centerx - (screen_width//2)
        if self.offset.x < 0:
            self.offset.x = 0
        if self.offset.x > border_x:
            self.offset.x = border_x
        for tile in self.tile_list:
            offset_pos = tile[1].topleft - self.offset
            screen.blit(tile[0], offset_pos)
