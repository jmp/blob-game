from .object import Object
from ..constants import SCREEN_WIDTH, SCREEN_HEIGHT
from ..image import Image
from ..input_device import InputDevice


class Player(Object):
    images = [
        Image(0, 0, 0, colkey=13),
        Image(0, 8, 0, colkey=13),
        Image(1, 0, 0, colkey=13),
        Image(1, 8, 0, colkey=13),
    ]

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.bbox.y = 1
        self.bbox.h = 7
        self.is_moving = False

    def handle_input(self, input_device: InputDevice) -> None:
        self.is_moving = False
        if input_device.is_left_held:
            self.move_left()
        if input_device.is_right_held:
            self.move_right()
        if input_device.is_up_held:
            self.move_up()
        if input_device.is_down_held:
            self.move_down()

    def update(self) -> None:
        self.img = self.images[self.direction]
        if self.is_moving:
            self.img = self.images[self.direction::2][
                self.frame_index % len(self.images[self.direction::2])
            ]

    def move_left(self) -> None:
        self.x -= self.move_speed
        if self.x < -self.bbox.x:
            self.x = -self.bbox.x
        self.direction = 1
        self.is_moving = True

    def move_right(self) -> None:
        self.x += self.move_speed
        max_x = SCREEN_WIDTH - (self.bbox.x + self.bbox.w)
        if self.x > max_x:
            self.x = max_x
        self.direction = 0
        self.is_moving = True

    def move_up(self) -> None:
        self.y -= self.move_speed
        if self.y < -self.bbox.y:
            self.y = -self.bbox.y
        self.is_moving = True

    def move_down(self) -> None:
        self.y += self.move_speed
        max_y = SCREEN_HEIGHT - (self.bbox.y + self.bbox.h)
        if self.y > max_y:
            self.y = max_y
        self.is_moving = True
