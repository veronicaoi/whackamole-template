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


        running = True
        while running:
            for event in pygame.event.get(): #Collecting each event that occurs
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green") #background color, pre-defined
            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))

            #Drawing the grid
            for i in range(0, 20):  # vertical lines
                pygame.draw.line(screen, 'black', (i*32, 0), (i*32, 512))
            for i in range(16):  #horizontal lines
                pygame.draw.line(screen, 'black', (0, i*32), (640, i*32))

            #Click event:
            mx, my = mole_image.pos #mole coordinates
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos #click coordinates
                if (mx - 32 <= x <= mx + 32) and (mx - 32 <= y <= mx + 32):
                    mx = random.randrange(0, 641)
                    my = random.randrange(0, 513)
            pygame.display.flip() #update screen with anything that was drawn/colored
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
