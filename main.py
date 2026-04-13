import pygame
import constants
from logger import log_state

def main():
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print("Screen width: " + str(constants.SCREEN_WIDTH))
    print("Screen height: " + str(constants.SCREEN_HEIGHT))
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    screen.fill("black")
    display.flip()
if __name__ == "__main__":
    main()
