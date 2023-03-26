"""Component 2 - Starting the game
Making ground longer by adding multiple ground images
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
ground_x_1 = 300
ground_x_2 = 600
ground_x_3 = 0
ground_y = 244
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

    # Ground
    ground_position_2 = pygame.Rect(ground_x_2, ground_y, 200, 150)
    ground_2 = pygame.image.load('ground.png').convert_alpha()
    resized_ground_2 = pygame.transform.smoothscale(ground_2, [300, 200])
    screen.blit(resized_ground_2, ground_position_2)

    ground_position_1 = pygame.Rect(ground_x_1, ground_y, 200, 150)
    ground_1 = pygame.image.load('ground.png').convert_alpha()
    resized_ground_1 = pygame.transform.smoothscale(ground_1, [300, 200])
    screen.blit(resized_ground_1, ground_position_1)

    ground_position_3 = pygame.Rect(ground_x_3, ground_y, 200, 150)
    ground_3 = pygame.image.load('ground.png').convert_alpha()
    resized_ground_3 = pygame.transform.smoothscale(ground_3, [300, 200])
    screen.blit(resized_ground_3, ground_position_3)

    pygame.display.update()
pygame.quit()
quit()
