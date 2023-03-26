"""Component 2 - Starting the game
Make ground with creating a line
"""
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))
game_icon = pygame.image.load('llama_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Llama game - by Sophia Choe")

# Tuples containing the colours to be used in the game
black = (0, 0, 0)
white = (255, 255, 255)

# Fonts for the game
pixel_font = pygame.font.SysFont("pixpixelfjverdana12pt", 20)

quit_game = False

# Llama coordinate
llama_x = 384  # Middle point horizontally is (800-32 llama width)/2 = 384
llama_y = 300  # Bottom point vertically

# Ground coordinates


# Create ground
ground = pygame.transform.scale(pygame.image.load("ground.png"), (800, 500))
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    screen.fill(white)  # changes background to white

    # Llama sprite
    llama_position = pygame.Rect(llama_x, llama_y, 32, 32)
    llama = pygame.image.load('Llama.png').convert_alpha()
    resized_llama = pygame.transform.smoothscale(llama, [50, 50])
    screen.blit(resized_llama, llama_position)

    llama_rect = ground.get_rect(center=(llama_x, llama_y))
    screen.blit(ground, llama_rect)

    pygame.display.update()
pygame.quit()
quit()
