"""
Author: Christine Wei
Date: May 16, 2023,
Description: Bricks Image Sprite
"""

# I - Import and Initialize
import myPacmanSprites
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))


def main():
    """This function defines the 'mainline logic' for our game."""

    # Display
    pygame.display.set_caption("Ten Cherries and Pacman")

    # Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # sound effects
    boing = pygame.mixer.Sound("boing.wav")
    boing.set_volume(0.5)

    # Create pacman
    pacman = myPacmanSprites.Pacman(screen)

    # Create 10 random bricks
    cherries = []
    for i in range(10):
        cherries.append(myPacmanSprites.Cherry(screen))

    allSprites = pygame.sprite.Group(cherries, pacman)

    # ACTION

    # Assign
    keepGoing = True
    clock = pygame.time.Clock()

    # Loop
    while keepGoing:

        # Time
        clock.tick(30)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        for cherry in cherries:
            if pacman.rect.colliderect(cherry.rect):
                # Make cherry disappear
                cherry.kill()
                cherries.remove(cherry)
                # sound effect
                boing.play()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Pacman goes right
                pacman.go_right()
            elif event.key == pygame.K_LEFT:
                # Pacman goes left
                pacman.go_left()
            elif event.key == pygame.K_UP:
                # Pacman goes up
                pacman.go_up()
            elif event.key == pygame.K_DOWN:
                # Pacman goes down
                pacman.go_down()

        # Refresh screen
        allSprites.clear(screen, background)
        allSprites.draw(screen)
        allSprites.update()

        pygame.display.flip()

    # Close the game window
    pygame.quit()


# Call the main function
main()
