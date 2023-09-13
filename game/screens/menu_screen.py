import pyxel

from .screen import Screen
from ..input_devices.protocols import InputDevice
from ..ui import draw_button, draw_title

START = 'Start'
QUIT = 'Quit'


class MenuScreen(Screen):
    selection = START

    def update(self, input_device: InputDevice) -> Screen:
        if input_device.is_cancel_pressed:
            pyxel.quit()
            return self
        if input_device.is_up_held:
            self.selection = START
        if input_device.is_down_held:
            self.selection = QUIT
        if input_device.is_accept_pressed:
            if self.selection == START:
                from .play_screen import PlayScreen
                return PlayScreen()
            if self.selection == QUIT:
                pyxel.quit()
        return self

    def draw(self) -> None:
        pyxel.cls(1)
        draw_title(10, 20, 'BLOB GAME', 7)
        draw_button(25, 50, START, 7, 0 if self.selection == START else None)
        draw_button(25, 65, QUIT, 7, 0 if self.selection == QUIT else None)
