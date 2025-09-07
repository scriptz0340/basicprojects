import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

# Load and scale image
apple_img = pygame.image.load('apple.png').convert()
apple_img = pygame.transform.scale(
    apple_img,
    (apple_img.get_width() // 2, apple_img.get_height() // 2)
)
apple_img.set_colorkey((0, 0, 0))  # Make black transparent

running = True
x = 0
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255))
    screen.blit(apple_img, (x, 200))

    # Create hitbox and target
    hitbox = pygame.Rect(x, 200, apple_img.get_width(), apple_img.get_height())
    target = pygame.Rect(250, 160, 160, 280)

    # Collision detection
    collision = hitbox.colliderect(target)
    color = (255, 255, 0) if collision else (0, 255, 0)
    pygame.draw.rect(screen, color, target)

    # Move apple
    x += 50 * (clock.get_time() / 1000)
    if x > 640:
        x = -apple_img.get_width()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    # Frame rate control
    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))

pygame.quit()
