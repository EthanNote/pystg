import pygame.locals


class Axis:
    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.locals.KEYDOWN:
                if event.key in self.keymap.keys():
                    self.keydown_state[self.keymap[event.key]] = 1

            if event.type == pygame.locals.KEYUP:
                if event.key in self.keymap.keys():
                    self.keydown_state[self.keymap[event.key]] = 0

    def __init__(self):
        self.keydown_state = [0, 0, 0, 0, 0]
        self.keymap = {pygame.locals.K_LEFT: 0, pygame.locals.K_RIGHT: 1, pygame.locals.K_UP: 2,
                       pygame.locals.K_DOWN: 3, pygame.locals.K_LSHIFT: 4}


    def get_vector(self):
        return self.keydown_state[1] - self.keydown_state[0], self.keydown_state[3] - self.keydown_state[2]

    def get_shift(self):
        return self.keydown_state[4]==1