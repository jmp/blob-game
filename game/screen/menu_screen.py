from .screen import Screen
from ..renderer.protocols import Renderer
from ..input_device.protocols import InputDevice

START = 'Start'
QUIT = 'Quit'


class MenuScreen(Screen):
    selection = START

    def update(self, input_device: InputDevice) -> Screen | None:
        if input_device.is_cancel_pressed:
            return None
        if input_device.is_up_held:
            self.selection = START
        if input_device.is_down_held:
            self.selection = QUIT
        if input_device.is_accept_pressed:
            if self.selection == START:
                from .play_screen import PlayScreen
                return PlayScreen()
            if self.selection == QUIT:
                return None
        return self

    def draw(self, renderer: Renderer) -> None:
        renderer.clear(1)
        renderer.draw_title(10, 20, 'BLOB GAME', 7)
        renderer.draw_button(25, 50, START, 7, 0 if self.selection == START else None)
        renderer.draw_button(25, 65, QUIT, 7, 0 if self.selection == QUIT else None)
