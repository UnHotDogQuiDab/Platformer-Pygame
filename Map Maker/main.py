import pygame
import pytmx

screen = pygame.display.set_mode((0, 0))
tmx_data = pytmx.util_pygame.load_pygame('world.tmx')


with open("world.txt", 'w') as world:
    for layer in tmx_data:
        if layer.name == 'Usefull':
            world.write("[\n")
            data = layer.data
            for i in range(len(layer.data)):
                world.write("[")
                row = data[i]
                for j in range(len(layer.data[i])):
                    value = row[j]
                    world.write(f"{value}, ")
                world.write("],\n")
            world.write("]")
