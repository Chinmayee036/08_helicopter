"""
renderer: all pygame drawing lives here, kept separate from game logic.
"""
import pygame

class Renderer:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 24)
        self.large_font = pygame.font.SysFont("Arial", 48)

    def draw(self, engine):
        # Background color (Sky blue)
        self.screen.fill((135, 206, 235))

        # Draw helicopter
        engine.helicopter.draw(self.screen)

        # Draw obstacles
        for obs in engine.obstacles:
            obs.draw(self.screen)

        # Task 3: Render and display the current score on top left
        score_surface = self.font.render(f"Distance Score: {engine.score}", True, (0, 0, 0))
        self.screen.blit(score_surface, (20, 20))

        # Task 4: Display shield status text
        shield_text = "Shield: ACTIVE" if engine.helicopter.shield_active else "Shield: Ready (Press SPACE)"
        shield_color = (0, 100, 255) if engine.helicopter.shield_active else (100, 100, 100)
        shield_surface = self.font.render(shield_text, True, shield_color)
        self.screen.blit(shield_surface, (20, 50))

        # Game Over message screen
        if engine.game_over:
            game_over_surf = self.large_font.render("GAME OVER", True, (255, 0, 0))
            final_score_surf = self.font.render(f"Final Distance: {engine.score} | Press 'R' to Restart", True, (0, 0, 0))
            
            self.screen.blit(game_over_surf, (self.width // 2 - 120, self.height // 2 - 50))
            self.screen.blit(final_score_surf, (self.width // 2 - 180, self.height // 2 + 10))

        pygame.display.flip()
