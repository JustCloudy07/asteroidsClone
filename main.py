import pygame

from constants import *

from player import Player

from asteroid import Asteroid

from asteroidfield import AsteroidField

import sys


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots)
    
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

   

    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for updatable in updatables:
            updatable.update(dt)
        
        for asteroid in asteroids:
            if player.collision_detection(asteroid):
                print("Game over!")
                sys.exit()

        screen.fill("black")
       
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        
        
        dt = clock.tick(60) / 1000

       

if __name__ == "__main__":
    main()