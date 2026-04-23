import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot




def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # GROUPS
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # ADD PLAYER CLASS TO GROUPS
    Player.containers = (updatable, drawable,)
    
    # ADD ASTEROID CLASS TO GROUPS
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    # ADD SHOT CLASS TO GROUPS
    Shot.containers = (updatable, drawable, shots)
    
    asteroid_field = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        for sprite in updatable:
            sprite.update(dt)

        for object in asteroids:
            if player.collides_with(object):
                log_event("player_hit")
                print ("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collides_with(object):
                    log_event("asteroid_shot")
                    object.split()
                    shot.kill()
                    

        
       
        for sprite in drawable:
            sprite.draw(screen)

        

        pygame.display.flip()
        dt = clock.tick(60) / 1000
       




if __name__ == "__main__":
    main()