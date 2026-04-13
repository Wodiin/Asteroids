import pygame
import constants
import sys
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid 
from asteroidfield import AsteroidField
from shot import Shot

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
    
    # Set up sprite groups and containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Create a player instance
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Set up asteroid field and asteroids
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    # Main game loop
    while True:
        log_state()
        
        # Handle events (e.g., keyboard input, quitting)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update game state 
        screen.fill("black")
        
        # Check for collisions between the player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                return sys.exit()

        # Update and draw all sprites
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        # Update the display and manage the frame rate
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
       

if __name__ == "__main__":
    main()
