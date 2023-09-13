import pyxel

from game.input_device import InputDevice


class PyxelInputDevice(InputDevice):
    @property
    def is_left_held(self) -> bool:
        return pyxel.btn(pyxel.KEY_LEFT)

    @property
    def is_right_held(self) -> bool:
        return pyxel.btn(pyxel.KEY_RIGHT)

    @property
    def is_up_held(self) -> bool:
        return pyxel.btn(pyxel.KEY_UP)

    @property
    def is_down_held(self) -> bool:
        return pyxel.btn(pyxel.KEY_DOWN)

    @property
    def is_up_pressed(self) -> bool:
        return pyxel.btnp(pyxel.KEY_UP)

    @property
    def is_down_pressed(self) -> bool:
        return pyxel.btnp(pyxel.KEY_DOWN)

    @property
    def is_accept_pressed(self) -> bool:
        return pyxel.btnp(pyxel.KEY_RETURN)

    @property
    def is_cancel_pressed(self) -> bool:
        return pyxel.btnp(pyxel.KEY_ESCAPE)
