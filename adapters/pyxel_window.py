from typing import Callable

import pyxel

from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, CAPTION
from game.window import Window


class PyxelWindow(Window):
    def initialize(self) -> None:
        pyxel.init(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            title=CAPTION,
            quit_key=pyxel.KEY_NONE,
        )
        pyxel.load('../assets/data.pyxres')

    def run_main_loop(self, update_func: Callable, draw_func: Callable) -> None:
        pyxel.run(update_func, draw_func)

    def close(self) -> None:
        pyxel.quit()
