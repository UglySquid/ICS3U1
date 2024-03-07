"""
Author: Christine Wei
Date: May 11, 2023,
Description: Christine's Self Portrait
"""

# I - Import and Initialize
import pygame

pygame.init()


def statusSurface(drawColor, lineWidth):
    """ creates a Surface object for status text """

    myFont = pygame.font.SysFont("Courier", 20)
    status_string = "color: %s, width: %d" % (drawColor, lineWidth)
    status = myFont.render(status_string, True, drawColor)
    return status


def main():
    """This function defines the 'mainline logic' for our paint program."""

    # D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint: (w)hite, blac(k), (c)lear, (q)uit")

    # E - Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))

    # A - Action (broken into ALTER steps)

    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 0)
    lineWidth = 3

    # L - Loop
    while keepGoing:  

        # T - Timer to set frame rate
        clock.tick(30)

        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()

        # Check if a left mouse button is down
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.draw.line(background, drawColor, lineStart, lineEnd, lineWidth)
            lineStart = lineEnd

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                # quit
                keepGoing = False
            elif event.key == pygame.K_c:
                # clear screen
                background.fill((255, 255, 255))
            elif event.key == pygame.K_w:
                # white
                drawColor = (255, 255, 255)
            elif event.key == pygame.K_k:
                # black
                drawColor = (0, 0, 0)
            elif event.key == pygame.K_r:
                # red
                drawColor = (255, 0, 0)
            elif event.key == pygame.K_g:
                # green
                drawColor = (0, 255, 0)
            elif event.key == pygame.K_b:
                # blue
                drawColor = (0, 0, 255)
            elif event.key == pygame.K_1:
                # pixel width 1
                lineWidth = 1
            elif event.key == pygame.K_2:
                # pixel width 2
                lineWidth = 2
            elif event.key == pygame.K_3:
                # pixel width 3
                lineWidth = 3
            elif event.key == pygame.K_4:
                # pixel width 4
                lineWidth = 4
            elif event.key == pygame.K_5:
                # pixel width 5
                lineWidth = 5
            elif event.key == pygame.K_6:
                # pixel width 6
                lineWidth = 6
            elif event.key == pygame.K_7:
                # pixel width 7
                lineWidth = 7
            elif event.key == pygame.K_8:
                # pixel width 8
                lineWidth = 8
            elif event.key == pygame.K_9:
                # pixel width 9
                lineWidth = 9
            elif event.key == pygame.K_s:
                # Save the drawing as a PNG file
                pygame.image.save(screen, "painting.bmp")
            elif event.key == pygame.K_l:
                # load
                image = pygame.image.load("painting.bmp")

        # R - Refresh display
        screen.blit(background, (0, 0))
        myLabel = statusSurface(drawColor, lineWidth)
        screen.blit(myLabel, (450, 450))
        try:
            screen.blit(image, (0, 0))
        except UnboundLocalError:
            pass
        pygame.display.flip()

    # Close the game window
    pygame.quit()


# Call the main function
main()
