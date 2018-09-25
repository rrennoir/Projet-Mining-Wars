import pygame

pygame.init()

size = [1280, 720]
screen = pygame.display.set_mode(size)

black = (0, 0, 0)
white = (255, 255, 255)
background = pygame.Surface(screen.get_size())

clock = pygame.time.Clock()

tileSize = 100
rectTile = pygame.Rect(100, 100 , tileSize, tileSize)

do = True
while do:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do = False
            quit()

    pygame.draw.rect(screen, white, rectTile)

    pygame.display.update()

    screen.blit(background, (0, 0))
