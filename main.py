import pygame
from Player import Player
from World import World, blocker_group, screen, spike_group, platform_up_group
from Button import Button

pygame.init()
game_over = 0

game_over_img = pygame.transform.scale(pygame.image.load("Platformer sprites/Base pack/GAME_OVER.jpg"), (600, 100))
game_over_button = Button(200, 400, game_over_img)
exit_img = pygame.transform.scale(pygame.image.load("Platformer sprites/Base pack/exit.jpg"), (300, 50))
exit_button = Button(350, 600, exit_img)
restart_img = pygame.transform.scale(pygame.image.load("Platformer sprites/Base pack/restart.jpg"), (300, 50))
restart_button = Button(350, 525, restart_img)

count = -1
player = Player(100, 870)
world = World()
clock = pygame.time.Clock()

run = True
while run:

    world.draw()
    for i in platform_up_group:
        if game_over == 0:
            i.update()
        screen.blit(i.image, i.rect)
    if game_over == 0:
        blocker_group.update()
    spike_group.draw(screen)
    blocker_group.draw(screen)
    game_over = player.update(game_over)

    if count == -1:
        screen.fill([255, 255, 255])
        if exit_button.draw():
            run = False
        if restart_button.draw():
            player.reset(100, 870)
            game_over = 0
            count = 0
    if game_over != 0:
        count += 1
    if count >= 120:
        screen.fill([255, 255, 255])
        game_over_button.draw()
        if exit_button.draw():
            run = False
        if restart_button.draw():
            player.reset(100, 870)
            game_over = 0
            count = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)
