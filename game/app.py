import pyxel

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, CAPTION, DATA_FILE
from .screens.screen import Screen


class App:
    def __init__(self, initial_screen: Screen):
        self.screen: Screen = initial_screen
        pyxel.init(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            caption=CAPTION,
            quit_key=pyxel.KEY_NONE,
        )
        pyxel.load(DATA_FILE)
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.screen.next_screen is not None:
            self.screen = self.screen.next_screen
            self.screen.next_screen = None
        self.screen.update()

    def draw(self):
        self.screen.draw()
