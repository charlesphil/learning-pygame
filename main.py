import pygame
from sys import exit

# Initialize pygame
pygame.init()
# Draw screen
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
# Clock object to control framerate
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# Surface objects
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface = test_font.render("My Game", False, "black")
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))


player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
# Create game loop
while True:
    # From all pygame events...
    for event in pygame.event.get():
        # If the QUIT event is called, quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            # Gracefully exit the program (from sys)
            exit()

    if snail_rect.right <= 0:
        snail_rect.left = 800

    # Show surfaces and rectangles
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    # Move snail position
    snail_rect.x -= 4
    screen.blit(snail_surface, snail_rect)
    # Move player position
    player_rect.left += 1
    screen.blit(player_surface, player_rect)

    # Draw all of our elements and update them
    pygame.display.update()

    # Prevents the while loop from running faster than 60 frames/second
    clock.tick(60)
