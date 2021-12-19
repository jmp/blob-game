import pyxel

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, CAPTION, DATA_FILE
from .screens.screen import Screen


class App:
    def __init__(self, initial_screen: Screen):
        self.screen: Screen = initial_screen
        pyxel.init(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            title=CAPTION,
            quit_key=pyxel.KEY_NONE,
        )
        pyxel.load(DATA_FILE)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.screen = self.screen.update()

    def draw(self):
        self.screen.draw()
