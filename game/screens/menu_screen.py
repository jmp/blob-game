from typing import Optional

import pyxel

from .screen import Screen
from ..ui import draw_button, draw_title

START = 'Start'
QUIT = 'Quit'


class MenuScreen(Screen):
    selection = START

    def update(self) -> Screen:
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
            return self
        if pyxel.btnp(pyxel.KEY_UP):
            self.selection = START
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.selection = QUIT
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN):
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
