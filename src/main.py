import pygame

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode([900, 600])
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        # Update Loop
        pygame.display.flip()
