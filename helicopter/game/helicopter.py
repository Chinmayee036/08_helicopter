import pygame

class Helicopter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 20
        self.vy = 0
        self.gravity = 0.5
        self.lift = -0.8
        self.max_speed = 8  # Task 1: Max speed cap
        self.shield_active = False # Task 4: Shield mechanic

    def handle_input(self, keys):
        # Task 1: Fix laggy controls by handling up/down directly with speed limits
        if keys[pygame.K_UP]:
            self.vy += self.lift
        elif keys[pygame.K_DOWN]:
            self.vy += -self.lift  # Move down
        else:
            # Apply slight damping when no key is pressed
            self.vy *= 0.9

        # Cap the speed so it doesn't build up forever
        if self.vy < -self.max_speed:
            self.vy = -self.max_speed
        elif self.vy > self.max_speed:
            self.vy = self.max_speed

    def update(self, screen_height):
        self.y += self.vy

        # Task 1: Top and bottom boundary check so it never leaves the screen
        if self.y < 0:
            self.y = 0
            self.vy = 0
        elif self.y > screen_height - self.height:
            self.y = screen_height - self.height
            self.vy = 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        # Draw helicopter body
        pygame.draw.rect(surface, (0, 255, 0), self.get_rect())
        # Task 4: Visual indication if shield is active (blue outline/glow)
        if self.shield_active:
            pygame.draw.rect(surface, (0, 191, 255), self.get_rect(), 3)
