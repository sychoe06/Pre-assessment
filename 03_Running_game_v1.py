"""Component 3 - Starting the game

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

speed = pygame.time.Clock()  # sets the speed at which the llama moves

quit_game = False

# Llama coordinate
llama_x = 384  # Middle point horizontally is (800-32 llama width)/2 = 384
llama_y = 300  # Bottom point vertically

llama_x_change = 0  # holds the value of changes in the x-coordinate
llama_y_change = 0  # holds the value of changes in the y-coordinate

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                llama_x_change = -20
                llama_y_change = 0
            elif event.key == pygame.K_RIGHT:
                llama_x_change = 20
                llama_y_change = 0

    llama_x += llama_x_change
    llama_y += llama_y_change

    screen.fill(white)  # changes background to white

    # Llama sprite
    llama = pygame.Rect(llama_x, llama_y, 32, 32)
    sprite = pygame.image.load('Llama.png').convert_alpha()
    resized_sprite = pygame.transform.smoothscale(sprite, [32, 32])
    screen.blit(resized_sprite, llama)

    pygame.display.update()

    speed.tick(5)

pygame.quit()
quit()
