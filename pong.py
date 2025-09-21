import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Screen size
pygame.display.set_caption("Pong") # Window's name
clock = pygame.time.Clock() # Clock object

control_mode = "mouse"
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
        elif event.type == pygame.KEYDOWN: # Next if, we check buttons.
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                control_mode = "keyboard"
        elif event.type == pygame.MOUSEMOTION:
            control_mode = "mouse"
    print("Történés: ", event)
    screen.fill((0, 0, 0))  # background
    pygame.draw.rect(screen, (255, 255, 255), (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.display.flip()
    clock.tick(60) # We use clock object. Max 60 round / second

    if control_mode == "keyboard":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
            paddle_x += paddle_speed
    elif control_mode == "mouse":
        mouse_x, _= pygame.mouse.get_pos()
        paddle_x = mouse_x - paddle_width // 2


pygame.quit()