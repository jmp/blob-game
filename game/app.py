from .window.protocols import Window
from .renderer.protocols import Renderer
from .input_device.protocols import InputDevice
from .screen.screen import Screen


class App:
    def __init__(self, window: Window, renderer: Renderer, input_device: InputDevice, initial_screen: Screen):
        self.window = window
        self.renderer = renderer
        self.input_device = input_device
        self.screen = initial_screen
        self.window.initialize()
        self.window.run_main_loop(self.update, self.draw)

    def update(self) -> None:
        next_screen = self.screen.update(self.input_device)
        if next_screen is None:
            self.window.close()
        else:
            self.screen = next_screen

    def draw(self) -> None:
        self.screen.draw(self.renderer)
