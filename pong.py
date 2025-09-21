import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Screen size
pygame.display.set_caption("Pong") # Window's name
clock = pygame.time.Clock() # Clock object

paddle_width = 100
paddle_height = 10
paddle_x = (WIDTH-paddle_width) // 2
paddle_y = HEIGHT - 30
paddle_speed = 6



over = True
while over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = False
    print("Történés: ", event)
    screen.fill((0, 0, 0))  # background
    pygame.draw.rect(screen, (255, 255, 255), (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.display.flip()
    clock.tick(60) # We use clock object. Max 60 round / second

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    elif keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed
    else:
        mouse_x, _= pygame.mouse.get_pos()
        paddle_x = mouse_x - paddle_width // 2


pygame.quit()