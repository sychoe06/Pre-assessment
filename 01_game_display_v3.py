"""Component 1 - Setting up game display
Added a basic game loop which lets users quit the game by clicking 'x'
"""
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))
game_icon = pygame.image.load('llama_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Llama game - by Sophia Choe")

quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

pygame.quit()
quit()
