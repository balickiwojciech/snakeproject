import pygame

step = 20
width = 800
height = 600
dimensions = (width, height)

pygame.init()
screen = pygame.display.set_mode((dimensions))
clock = pygame.time.Clock()



def turn(direction):
    pressed_key = pygame.key.get_pressed()


    if pressed_key[pygame.K_DOWN]:
        return 2

    if pressed_key[pygame.K_UP]:
        return 0

    if pressed_key[pygame.K_LEFT]:
        return 3

    if pressed_key[pygame.K_RIGHT]:
        return 1

    return direction


def set_new_position(x_pos, y_pos, direction):



    if direction == 2:
        return (x_pos, y_pos + step)

    if direction == 0:
        return (x_pos, y_pos - step)


    if direction == 3:
        return (x_pos - step, y_pos)

    if direction == 1:
        return (x_pos + step, y_pos)

    return (x_pos, y_pos)

head_x = 400
head_y = 300
head_direction = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(1)

    head_direction = turn(head_direction)
    head_x, head_y = set_new_position(head_x, head_y, head_direction)
    screen.fill((255, 255, 255))  # RGB
    kwadrat = pygame.Rect(head_x,head_y,20,20)
    pygame.draw.rect(screen, (128,128,128), kwadrat)

    pygame.display.flip()
    pygame.display.set_caption("SNAKe by me")
    clock.tick(16)