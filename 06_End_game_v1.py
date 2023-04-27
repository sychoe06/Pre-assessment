"""Component 6 - Ending the game
When llama touches the cactus make the game end
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
pixel_font = pygame.font.SysFont("pixpixelfjverdana12pt", 15)

quit_game = False

# Llama coordinate
llama_x = 200  # Middle point horizontally is (800-32 llama width)/2 = 384
llama_y = 300  # Bottom point vertically

cactus_x = 800  # Make cactus start at the edge of the screen
cactus_y = 300

cactus_x_change = 0

jumping = False  # Starts out false because Llama doesn't jump until space bar
cactus_start = False
Y_GRAVITY = 0.5
JUMP_HEIGHT = 15
Y_VELOCITY = JUMP_HEIGHT

score = 0


def message(msg, txt_colour, bkgd_colour):
    text = pixel_font.render(msg, True, txt_colour, bkgd_colour)

    # Position of text
    text_box = text.get_rect(center=(700, 50))
    screen.blit(text, text_box)


while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    # Returns a dictionary of all keys that can be pressed
    keys = pygame.key.get_pressed()
    # Checks that dictionary to see if space bar has been pressed
    if keys[pygame.K_SPACE]:
        jumping = True  # So jump happens only when space bar is pressed
        cactus_start = True  # Cactus only appears when space bar is pressed

    if jumping:
        llama_y -= Y_VELOCITY  # Makes Llama move up by 20px
        Y_VELOCITY -= Y_GRAVITY  # Reduces velocity by 1px

        if Y_VELOCITY < -JUMP_HEIGHT:  # When Y_VELOCITY is under -20
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT  # Rests Y_VELOCITY to 20

            if llama_x > cactus_x:  # When llama jumps over cactus
                score += 1
                # print(score)  testing purposes

    if cactus_start:
        cactus_x_change = -1.5  # Makes cactus move left across screen
        cactus_x += cactus_x_change
        if cactus_x <= 0:
            cactus_x = 800

    if llama_x == cactus_x and llama_y == cactus_y:
        quit_game = True

        print("Game over")  # testing purposes
        print(score)

    screen.fill(white)  # changes background to white

    # Llama sprite
    llama = pygame.transform.scale(pygame.image.load("Llama.png"), (55, 55))
    llama_rect = pygame.Rect(llama_x, llama_y, 55, 55)
    screen.blit(llama, llama_rect)

    # Create ground
    ground = pygame.transform.scale(pygame.image.load("ground.png"), (850, 600))
    ground_rect = ground.get_rect()
    screen.blit(ground, ground_rect)

    # Create cactus
    cactus = pygame.transform.scale(pygame.image.load("cactus.png"), (55, 55))
    cactus_rect = pygame.Rect(cactus_x, cactus_y, 55, 55)
    screen.blit(cactus, cactus_rect)

    # Score
    message(f"Score: {score}", black, white)

    pygame.display.update()

pygame.quit()
quit()
