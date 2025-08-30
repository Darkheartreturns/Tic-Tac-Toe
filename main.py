import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
value = 1
objects = []
drawn_shapes = []
color_b = (0, 0, 0)
color_w = (255, 255, 255)
def draw_board():
    pygame.draw.line(screen, (255, 255, 255), (320, 240), (960, 240), 5)
    pygame.draw.line(screen, (255, 255, 255), (320, 450), (960, 450), 5)
    pygame.draw.line(screen, (255, 255, 255), (500, 120), (500, 600), 5)
    pygame.draw.line(screen, (255, 255, 255), (750, 120), (750, 600), 5)

positions_list = [
    #left side
    pygame.Rect(320, 246, 173, 198),
    pygame.Rect(320, 114, 173, 112),
    pygame.Rect(320, 459, 173, 145),
    #middle side
    pygame.Rect(503, 246, 240, 198),
    pygame.Rect(503, 114, 240, 112),
    pygame.Rect(503, 459, 240, 145),
    #right side
    pygame.Rect(754, 246, 202, 198),
    pygame.Rect(754, 114, 202, 112),
    pygame.Rect(754, 459, 202, 145),
]

def draw_o(color,pos):
    pygame.draw.circle(screen, color, pos, 20)

def draw_x(color,pos):
    x, y = pos
    size = 20
    pygame.draw.line(screen, color, (x-size, y-size), (x+size, y+size), 2)
    pygame.draw.line(screen, color, (x-size, y+size), (x+size, y-size), 2)

while running:
    screen.fill("black")
    draw_board()
    draw_x(color_w, (80, 55))
    for shape_type, shape_pos in drawn_shapes:
        if shape_type == 'x':
            draw_o(color_w, (1201, 55))
            draw_x(color_w, shape_pos)
            draw_x(color_b, (80, 55))
        elif shape_type == 'o':
            draw_x(color_w, (80, 55))
            draw_o(color_w, shape_pos)
            draw_o(color_b, (1201, 55))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            objects.append(pos)
            mouse_rect = pygame.Rect(pos[0], pos[1], 1, 1)
            collided = mouse_rect.collidelistall(positions_list)
            if collided:
                if value == 1:
                    collided_index = collided[0]
                    collided_rect = positions_list[collided_index]
                    drawn_shapes.append(('x', collided_rect.center))
                    positions_list.pop(collided_index)
                    value *= -1
                elif value == -1:
                    collided_index = collided[0]
                    collided_rect = positions_list[collided_index]
                    drawn_shapes.append(('o', collided_rect.center))
                    positions_list.pop(collided_index)
                    value *= -1
    pygame.display.flip()

    clock.tick(60)
print(objects)

pygame.quit()