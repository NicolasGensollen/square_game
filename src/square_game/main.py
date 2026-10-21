import sys
import pygame

WIDTH, HEIGHT = 600, 400
BACKGROUND_COLOR = (0, 0, 0)
SQUARE_COLOR = (23, 154, 175)
SQUARE_SIZE = 50
SPEED = 5
FPS = 60


def main():
    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    pos_x = (WIDTH - SQUARE_SIZE) // 2
    pos_y = (HEIGHT - SQUARE_SIZE) // 2

    running: bool = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill(BACKGROUND_COLOR)
        pos_x += SPEED
        pygame.draw.rect(surface, SQUARE_COLOR, (pos_x, pos_y, SQUARE_SIZE, SQUARE_SIZE))
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
