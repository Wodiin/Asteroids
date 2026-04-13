import pygame
import constants
from logger import log_state
from player import Player

def main():
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print("Screen width: " + str(constants.SCREEN_WIDTH))
    print("Screen height: " + str(constants.SCREEN_HEIGHT))
    
    # Initialize pygame
    pygame.init() 

    # Set up the display
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    # Set up the clock for managing the frame rate
    clock = pygame.time.Clock()
    dt = 0

    # Create a player instance
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Main game loop
    while True:
        log_state()
        
        # Handle events (e.g., keyboard input, quitting)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update game state 
        screen.fill("black")
        player.update(dt) 
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
       

if __name__ == "__main__":
    main()
