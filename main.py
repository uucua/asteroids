import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from highscore import load_high_score, save_high_score

def main()-> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()


    Shot.containers = (shots, drawable, updatable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers= (updatable,drawable)
    asteroidf = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0.0
    score = 0
    high_score = load_high_score()
    font = pygame.font.Font(None, 36)

    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                save_high_score(score)
                sys.exit()
            
            for shot in shots:
                if shot.collides_with(ast):
                    log_event("asteroid_shot")
                    if ast.radius <= 20:
                        score += 100
                    elif ast.radius <= 40:
                        score += 50
                    else:
                        score += 20
                    ast.split()
                    shot.kill()
                    break
        score_text = font.render(f"Score: {score}", True, "white")
        high_score_text = font.render(f"High Score: {high_score}", True, "white")
        screen.fill("black")
        

        for obj in drawable:
            obj.draw(screen)

        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (10, 40))
        pygame.display.flip()

        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
