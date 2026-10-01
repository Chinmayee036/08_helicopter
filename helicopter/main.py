"""
Helicopter Game (Lab Starter)

Run with:  python3 main.py

Controls: Up/Down arrows to move.
"""
import pygame
from game.game_engine import GameEngine
from game.renderer import Renderer

def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Helicopter Game")

    clock = pygame.time.Clock()
    engine = GameEngine(width, height)
    renderer = Renderer(screen, width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            engine.handle_input(event)

        engine.update()
        renderer.draw(engine)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
