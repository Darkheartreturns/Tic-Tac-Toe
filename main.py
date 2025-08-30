import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
value = 1
objects = []
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

#still working on it
#def draw_o():
#     pygame.draw.circle(screen, (255, 255, 255), )

while running:
    screen.fill("black")
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            objects.append(pos)
            mouse_rect = pygame.Rect(pos[0], pos[1], 1, 1)
            #if mouse_rect.collidelistall(positions_list):
                
    pygame.display.update()

    clock.tick(60)
print(objects)

pygame.quit()