import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
objects = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            objects.append(pos)

    screen.fill("black")
    pygame.draw.line(screen, (255, 255, 255), (320, 240), (960, 240), 5)
    pygame.draw.line(screen, (255, 255, 255), (320, 450), (960, 450), 5)
    pygame.draw.line(screen, (255, 255, 255), (500, 120), (500, 600), 5)
    pygame.draw.line(screen, (255, 255, 255), (750, 120), (750, 600), 5)

    pygame.display.update()
    
    clock.tick(60)

print(objects)
pygame.quit()