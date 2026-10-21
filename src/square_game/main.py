import sys
import pygame

WIDTH, HEIGHT = 600, 400


def main():
    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))

    running: bool = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
