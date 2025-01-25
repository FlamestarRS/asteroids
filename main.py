# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from bullets import *



def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:    
            obj.update(dt)

        for obj in asteroids:

            for shot in shots:
                if obj.collision(shot) == True:
                    obj.kill()
                    shot.kill()

            if obj.collision(player) == True:
                print("Game over!")
                sys.exit()
            

        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        clock.tick(60)
        dt = (clock.tick(60) / 1000)



if __name__ == "__main__":
    main()