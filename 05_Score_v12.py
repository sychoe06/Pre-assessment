"""Component 5 - Score
The score increases as the time of the llama surviving increases
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
start_time = None
clock = pygame.time.Clock()
start_game = False

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
        start_game = True

    if start_game:
        start_time = pygame.time.get_ticks()

    if jumping:
        llama_y -= Y_VELOCITY  # Makes Llama move up by 20px
        Y_VELOCITY -= Y_GRAVITY  # Reduces velocity by 1px

        if Y_VELOCITY < -JUMP_HEIGHT:  # When Y_VELOCITY is under -20
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT  # Rests Y_VELOCITY to 20

    if cactus_start:
        cactus_x_change = -1.5  # Makes cactus move left across screen
        cactus_x += cactus_x_change
        if cactus_x <= 0:
            cactus_x = 800

    if start_time:
        time_since_enter = pygame.time.get_ticks() - start_time
        message = "Score: " + str(time_since_enter)
        screen.blit(pixel_font.render(message, True, black), (20, 20))

        pygame.display.flip()
        clock.tick(60)

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

    pygame.display.update()

pygame.quit()
quit()
