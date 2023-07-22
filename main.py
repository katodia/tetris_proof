import pygame

from Shape import Shape

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1024, 768])
square_width = 30
rows = 8
cols = 5
#posicion inicial x,y desde la que se colocaran las piezas
x_position = 120
y_position = 40

# Run until the user asks to quit
running = True
shapes = []
previous_pos = pygame.mouse.get_pos()

for i in range(5):
    shapes.append(Shape(screen, (cols*square_width) + 40 + (i * x_position), y_position, i))
    shapes.append(Shape(screen, (cols*square_width) + 40 + (i * x_position), y_position + 150, i)) #comentar esta linea si solo se quiere una fila de piezas

pygame.event.set_grab(True)


def draw_matrix(square_width, cols, rows):
    for i in range(cols):
        for j in range(rows):
            pygame.draw.rect(screen, (0, 0, 0),
                             pygame.Rect(20 + ((square_width + 1) * i), 20 + (square_width + 1) * j, square_width,
                                         square_width))


def get_sense(coord):
    if coord < 0:
        return -1
    elif coord > 0:
        return 1
    return 0


while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for shape in shapes:
                if shape.is_colliding(event) and event.button == 1:
                    shape.set_dragging(True)
                    break
                if event.button == 2 and shape.is_colliding(event):
                    shape.flip()
                    break
                if event.button == 3 and shape.is_colliding(event):
                    shape.rotate()
                    break

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for shape in shapes:
                shape.set_dragging(False)

    for shape in shapes:
        shape.update()

    # Fill the background with white
    screen.fill((255, 255, 255))
    draw_matrix(square_width, cols, rows)
    for i in range(len(shapes)):
        shapes[i].draw()
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
