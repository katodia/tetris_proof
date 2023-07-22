import pygame


class Shape:
    S = [['.00',
          '00.'
          ],
         ['0.',
          '00',
          '.0']]

    Z = [[
        '00.',
        '.00'],
        ['.0',
         '00',
         '0.']]

    I = [['0000'],
         ['0',
          '0',
          '0',
          '0']]

    O = [['00',
          '00']]

    J = [['0..',
          '000'],
         ['00',
          '0.',
          '0.'],
         ['000',
          '..0'],
         ['.0',
          '.0',
          '00']]

    L = [['..0',
          '000'],
         ['0.',
          '0.',
          '00'],
         ['000',
          '0.'],
         ['00',
          '.0',
          '.0']]

    T = [['.0.',
          '000'],
         ['0.',
          '00',
          '0.'],
         ['000',
          '.0.'],
         ['.0',
          '00',
          '.0']]
    shapes = [S, I, O, L, T, Z, J]
    shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 105, 0), (255, 165, 0), (0, 255, 0), (255, 105, 0)]
    rectangles = []
    is_dragging = False
    square_width = 30
    current_shape = 0

    def __init__(self, screen, x, y, type_of_shape=None):
        self.screen = screen
        self.x = x
        self.y = y
        if type_of_shape is None:
            self.type_of_shape = self.I
        else:
            self.type_of_shape = self.shapes[type_of_shape]

    def draw(self):
        the_shape = self.type_of_shape[self.current_shape]
        self.rectangles = []

        for i, line in enumerate(the_shape):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    self.rectangles.append({'color': self.shape_colors[self.shapes.index(self.type_of_shape)],
                                            'rect': pygame.Rect(self.x + (self.square_width + 1) * i,
                                                                self.y + (self.square_width + 1) * j,
                                                                self.square_width, self.square_width)})
                    pygame.draw.rect(self.screen, self.rectangles[-1]['color'],
                                     self.rectangles[-1]['rect'])

    def update(self):
        if self.is_dragging:
            self.x, self.y = pygame.mouse.get_pos()

    def is_colliding(self, event):
        for rectangle in self.rectangles:
            if rectangle['rect'].collidepoint(event.pos):
                return True

        return False

    def set_dragging(self, is_dragging: bool):
        self.is_dragging = is_dragging

    def rotate(self):
        if self.current_shape < len(self.type_of_shape) - 1:
            self.current_shape += 1
        else:
            self.current_shape = 0

    def flip(self):
        if self.type_of_shape == self.S:
            self.type_of_shape = self.Z
        elif self.type_of_shape == self.Z:
            self.type_of_shape = self.S
        elif self.type_of_shape == self.L:
            self.type_of_shape = self.J
        elif self.type_of_shape == self.J:
            self.type_of_shape = self.L
