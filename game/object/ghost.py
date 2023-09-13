from random import randint
from time import time

from ..constants import SCREEN_WIDTH, SCREEN_HEIGHT
from ..image import Image
from .object import Object


class Ghost(Object):
    images = [
        Image(0, 0, 16, colkey=13),
        Image(0, 8, 16, colkey=13),
        Image(1, 0, 16, colkey=13),
        Image(1, 8, 16, colkey=13),
    ]

    def __init__(self):
        super().__init__()
        self.reset()

    def reset(self) -> None:
        self.x = -self.size
        self.y = randint(0, SCREEN_HEIGHT - 8)

    def update(self) -> None:
        self.img = self.images[self.direction::2][
            self.frame_index % len(self.images[self.direction::2])
        ]
        self.x += 1
        if self.x > SCREEN_WIDTH:
            self.reset()
