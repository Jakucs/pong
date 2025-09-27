import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Screen size
pygame.display.set_caption("Pong") # Window's name
clock = pygame.time.Clock() # Clock object
font = pygame.font.SysFont(None, 74) # Font object
font_point = pygame.font.SysFont(None, 24)

# Basic datas
control_mode = "mouse"
paddle_width = 100
paddle_height = 10
paddle_x = (WIDTH-paddle_width) // 2
paddle_y = HEIGHT - 30
paddle_speed_keyboard = 6 # to keyboard control
paddle_speed_actual = 0 # actual speed, because of the mouse
last_paddle_x = paddle_x # because of the mouse
ball_x = 100
ball_y = 100
ball_speed_x = 4
ball_speed_y = 4
ball_radius = 10
score = 0

colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (0, 255, 255)
]

targets = []
for row in range(2):
    if row % 2 == 0:
        row_colors = colors
    else:
        row_colors = list(reversed(colors))
    for col, color in enumerate(row_colors):
        rect = pygame.Rect(50 + col * 150, 20 + row * 30, 100, 20) # Every iteration the col value is different, the targets width is 100. So we have to make 50pixel break between targets.
        points = (col + 1) * 10    # it depends on col
        targets.append({"rect": rect, "color": color, "points": points})


over = True
while over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = False
        elif event.type == pygame.KEYDOWN: # Next if, we will check buttons.
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                control_mode = "keyboard"
        elif event.type == pygame.MOUSEMOTION:
            control_mode = "mouse"
    print("Történés: ", event)
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Drawings
    screen.fill((0, 0, 0))  # background

    for target in targets:
        pygame.draw.rect(screen, target["color"], target["rect"])

    point = font_point.render(f"Point: {score}", True, (255, 255, 255)) # Make a new pics (Surface, under point)
    screen.blit(point, (point.get_width()//4, 10)) # Draw this image on top of another image and we make position
    pygame.draw.rect(screen, (255, 255, 255), (paddle_x, paddle_y, paddle_width, paddle_height))
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height) # We create an invisible rectangle around paddle (due to collision)
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius) # Our ball
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius *2, ball_radius*2) # We create an invisible rectangle around ball (due to collision)
    pygame.display.flip()
    clock.tick(60) # We use clock object. Max 60 round / second

    for target in targets[:]: # Do not modify the list, we can safely iterate through it.
        if ball_rect.colliderect(target["rect"]): # We check if the ball invisible rect collides with the target invisible rect
            score += target["points"]
            targets.remove(target)
            if ball_y < target["rect"].top or ball_y > target["rect"].bottom:
                ball_speed_y = -ball_speed_y
            else:
                ball_speed_x = -ball_speed_x
            break

    # Ball collisions + speed
    if ball_x + ball_radius >= WIDTH:
        ball_speed_x = -ball_speed_x
    elif ball_y >= HEIGHT:
        text = font.render("Vesztettél!", True, (255, 0, 0)) # Make a new pics (Surface)
        screen.fill((0, 0, 0)) # background
        screen.blit(text, (WIDTH//2 - text.get_width()//2, 20)) # Draw this image on top of another image
        pygame.display.flip()
        pygame.time.wait(2000)  # wait 2 second
        over = False  # exit cycle
    elif ball_x - ball_radius < 0:
        ball_speed_x = -ball_speed_x
    elif ball_y - ball_radius < 0:
        ball_speed_y = -ball_speed_y
    elif ball_rect.colliderect(paddle_rect): # Old if: (paddle_x <= ball_x <= paddle_x + paddle_width) and (ball_y + ball_radius >= paddle_y)
        ball_speed_y = -ball_speed_y
        ball_speed_x += paddle_speed_actual * 0.5
        ball_y = paddle_y - ball_radius
        score += 1

    # Controls
    if control_mode == "keyboard":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed_keyboard
            paddle_speed_actual = -paddle_speed_keyboard
        if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
            paddle_x += paddle_speed_keyboard
            paddle_speed_actual = paddle_speed_keyboard
    elif control_mode == "mouse":
        mouse_x, _= pygame.mouse.get_pos()
        paddle_x = mouse_x - paddle_width // 2
        paddle_speed_actual = paddle_x - last_paddle_x
        last_paddle_x = paddle_x
    else:
        paddle_speed_actual = 0


pygame.quit()