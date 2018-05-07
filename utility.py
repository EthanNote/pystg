import os

import pygame


class Utility:
    screen = None
    group = {}

    @staticmethod
    def load_image_file(name):
        """ Load image and return image object"""
        fullname = os.path.join('data', name)
        try:
            image = pygame.image.load(fullname)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except pygame.error as message:
            print('Cannot load image:', fullname)
            raise SystemExit(message)
        return image, image.get_rect()

    @classmethod
    def setup(cls):
        pygame.init()
        cls.display = pygame.display
        cls.screen = cls.display.set_mode((800, 600), pygame.locals.DOUBLEBUF)
        cls.group = {}
        cls.default_group = pygame.sprite.Group()

    @classmethod
    def create_group(cls, name):
        cls.group[name] = pygame.sprite.Group()

    @classmethod
    def add_to_group(cls, sprite, name):
        if not name in cls.group.keys():
            cls.create_group(name)
        cls.group[name].add(sprite)

    @classmethod
    def gameloop(cls):
        clock = pygame.time.Clock()

        font = pygame.font.Font(None, 36)

        while True:
            clock.tick(120)
            fps = clock.get_fps()
            text = font.render('%.2f fps' % (fps,), 1, (0, 255, 0))
            text_rect = text.get_rect()
            surface_rect = cls.screen.get_rect()

            eventlist = pygame.event.get()
            for event in eventlist:
                if event.type == pygame.locals.QUIT:
                    return

            cls.screen.fill((0, 0, 0))

            for v in cls.group.values():
                v.draw(cls.screen)

            for v in cls.group.values():
                v.update(eventlist, clock)

            cls.screen.blit(text, text_rect.move(surface_rect.width - text_rect.width,
                                                 surface_rect.height - text_rect.height))
            pygame.display.flip()