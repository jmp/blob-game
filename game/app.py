import pyxel

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, CAPTION, DATA_FILE
from .renderers.protocols import Renderer
from .input_devices.protocols import InputDevice
from .screens.screen import Screen


class App:
    def __init__(self, renderer: Renderer, input_device: InputDevice, initial_screen: Screen):
        self.renderer = renderer
        self.input_device = input_device
        self.screen = initial_screen
        pyxel.init(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            title=CAPTION,
            quit_key=pyxel.KEY_NONE,
        )
        pyxel.load(DATA_FILE)
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        next_screen = self.screen.update(self.input_device)
        if next_screen is None:
            pyxel.quit()
        else:
            self.screen = next_screen

    def draw(self) -> None:
        self.screen.draw(self.renderer)
