import pygame

# making a sky background and some clouds
# 0 is sky, 1 is cloud top, 2 is cloud body

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
]

# set the size of each tile
TILE = 100
sky = pygame.image.load("images/background_0000.png")
cloud1 = pygame.image.load("images/background_0001.png")
cloud2 = pygame.image.load("images/background_0002.png")

air = [sky, cloud1, cloud2]

tile_rect = sky.get_rect()

def draw_background(bg_size):
    backgd = pygame.Surface(bg_size)
    # draw the tiles
    for k, grid_list in enumerate(grid):
        for p, grid_element in enumerate(grid_list):
            backgd.blit(air[grid_element], (p * TILE, k * TILE))
    return backgd