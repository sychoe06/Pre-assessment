"""Component 1 - Setting up game display
Adding caption and icon
"""
import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 500))
game_icon = pygame.image.load('llama_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Llama game - by Sophia Choe")

time.sleep(5)

pygame.quit()
quit()
