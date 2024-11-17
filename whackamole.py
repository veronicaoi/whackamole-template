import pygame
import random
import math

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mx = 0
        my = 0

        running = True
        while running:
            for event in pygame.event.get(): #Noting each event that occurs

                if event.type == pygame.QUIT: #Close window
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN: #Click on grid
                    x, y = event.pos  #mouse coordinates
                    
                    if (mx <= x <= mx + 32) and (my - 32 <= y <= my + 32):
                        xmult = random.randrange(0, 20)
                        ymult = random.randrange(0, 16)
                        mx = 32 * xmult
                        my = 32 * ymult


            screen.fill("light green") #background color, pre-defined

            #Drawing the grid
            for i in range(0, 20):  # vertical lines
                pygame.draw.line(screen, 'black', (i*32, 0), (i*32, 512))
            for i in range(16):  #horizontal lines
                pygame.draw.line(screen, 'black', (0, i*32), (640, i*32))

            screen.blit(mole_image, mole_image.get_rect(topleft=(mx, my)))
            pygame.display.flip() #update screen with anything that was drawn/colored
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
