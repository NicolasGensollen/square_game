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
            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_RIGHT:
                        pos_x += SPEED
                    case pygame.K_LEFT:
                        pos_x -= SPEED
                    case pygame.K_UP:
                        pos_y -= SPEED
                    case pygame.K_DOWN:
                        pos_y += SPEED
        if pos_x < 0:
            pos_x = 0
        elif pos_x > WIDTH - SQUARE_SIZE:
            pos_x = WIDTH - SQUARE_SIZE
        if pos_y < 0:
            pos_y = 0
        elif pos_y > HEIGHT - SQUARE_SIZE:
            pos_y = HEIGHT - SQUARE_SIZE

        surface.fill(BACKGROUND_COLOR)
        pygame.draw.rect(surface, SQUARE_COLOR, (pos_x, pos_y, SQUARE_SIZE, SQUARE_SIZE))
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
