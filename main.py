import pygame
from World import World, blocker_group, screen, spike_group, platform_up_group, key_group, exit_door_group, locker_group, reset_level, get_pos_player
from Player import Player
from Button import Button

pygame.init()
game_over = 0
level = 1
reset_level(level)

game_over_img = pygame.transform.scale(pygame.image.load("Usefull_img/GAME_OVER.jpg"), (600, 100))
exit_img = pygame.transform.scale(pygame.image.load("Usefull_img/exit.jpg"), (300, 50))
restart_img = pygame.transform.scale(pygame.image.load("Usefull_img/restart.jpg"), (300, 50))
restart_button = Button(350, 525, restart_img)
exit_button = Button(350, 600, exit_img)
game_over_button = Button(200, 400, game_over_img)


count = -1
world = World()
player = Player(get_pos_player(level)[0],  get_pos_player(level)[1], world)
clock = pygame.time.Clock()

run = True
while run:
    world.draw(player)
    for j in key_group:
        picked = j.update()
        if not picked:
            screen.blit(j.image, [j.rect.x - world.offset.x, j.rect.y - world.offset.y])
        else:
            key_group.remove(j)

    for k in locker_group:
        if not picked:
            screen.blit(k.image, [k.rect.x - world.offset.x, k.rect.y - world.offset.y])
        else:
            locker_group.remove(k)

    for i in platform_up_group:
        i.update()
        screen.blit(i.image, [i.rect.x - world.offset.x, i.rect.y - world.offset.y])

    for i in blocker_group:
        if game_over == 0:
            i.update()
        screen.blit(i.image, [i.rect.x - world.offset.x, i.rect.y - world.offset.y])

    for i in spike_group:
        i.update()
        screen.blit(i.image, [i.rect.x - world.offset.x, i.rect.y - world.offset.y])

    for i in exit_door_group:
        i.update()
        screen.blit(i.image, [i.rect.x - world.offset.x, i.rect.y - world.offset.y])
    game_over = player.update(game_over)

    if count == -1:
        screen.fill([255, 255, 255])
        if exit_button.draw():
            run = False
        if restart_button.draw():
            world = World()
            player.reset(get_pos_player(level)[0],  get_pos_player(level)[1], world)
            game_over = 0
            count = 0

    if game_over == -1:
        count += 1

    if game_over == 1:
        level += 1
        reset_level(level)
        world = World()
        player.reset(get_pos_player(level)[0],  get_pos_player(level)[1], world)
        game_over = 0

    if count >= 120:
        screen.fill([255, 255, 255])
        game_over_button.draw()
        if exit_button.draw():
            run = False
        if restart_button.draw():
            level = 1
            reset_level(level)
            world = World()
            player.reset(get_pos_player(level)[0],  get_pos_player(level)[1], world)
            game_over = 0
            count = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)
