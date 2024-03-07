# Demo #2b: Label Sprite Demo

# I - Import and Initialize
import mySprites
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))


def main():
    """This function defines the 'mainline logic' for our game."""

    # Display
    pygame.display.set_caption("Label demo")

    # Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    label1 = mySprites.Label("Hi. I'm a label.", (100, 100))
    label2 = mySprites.Label("I'm another label.", (400, 400))
    labelEvent = mySprites.Label("", (320, 200))

    allSprites = pygame.sprite.Group(label1, label2, labelEvent)

    # ACTION

    # Assign 
    clock = pygame.time.Clock()
    keepGoing = True

    # Loop
    while keepGoing:

        # Time
        clock.tick(30)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                labelEvent.set_text("mouse: (%d, %d)" % (mouseX, mouseY))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                labelEvent.set_text("button press")
            elif event.type == pygame.KEYDOWN:
                labelEvent.set_text("key down")

        # Refresh screen
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()

    # Close the game window
    pygame.quit()


# Call the main function
main()
