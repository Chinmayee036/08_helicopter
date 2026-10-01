"""
GameEngine: owns the helicopter and all obstacles.

Starter version: the helicopter moves and obstacles scroll by, but
there's no collision detection at all yet (the helicopter can fly
straight through obstacles harmlessly), no scoring, and no shield.
That's Tasks 2, 3, and 4. Movement also has known bugs (see
game/helicopter.py) that Task 1 asks you to fix.
"""

import pygame
import random
from game.helicopter import Helicopter
from game.obstacle import Obstacle

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.reset_game()

    def reset_game(self):
        self.helicopter = Helicopter(100, self.height // 2)
        self.obstacles = []
        self.game_over = False
        self.score = 0  # Task 3: Distance scoring
        self.spawn_timer = 0

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and self.game_over:
                self.reset_game()
            # Task 4: Press SPACE to activate shield
            elif event.key == pygame.K_SPACE:
                self.helicopter.shield_active = True

    def update(self):
        if self.game_over:
            return

        keys = pygame.key.get_pressed()
        self.helicopter.handle_input(keys)
        self.helicopter.update(self.height)

        # Task 3: Increase score/distance steadily while playing
        self.score += 1

        # Spawn obstacles
        self.spawn_timer += 1
        if self.spawn_timer > 90:
            self.obstacles.append(Obstacle(self.width, self.height))
            self.spawn_timer = 0

        # Update obstacles
        for obs in self.obstacles:
            obs.update()

        # Remove off-screen obstacles
        self.obstacles = [obs for obs in self.obstacles if not obs.is_off_screen()]

        # Task 2 & 4: Obstacle Collision and Shield check
        heli_rect = self.helicopter.get_rect()
        for obs in self.obstacles:
            top_wall, bottom_wall = obs.get_rects()
            if heli_rect.colliderect(top_wall) or heli_rect.colliderect(bottom_wall):
                if self.helicopter.shield_active:
                    # Task 4: Shield absorbs the hit and deactivates
                    self.helicopter.shield_active = False
                    self.obstacles.remove(obs)
                    break
                else:
                    # Task 2: Trigger game over on collision
                    self.game_over = True
