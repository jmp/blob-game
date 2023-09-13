from dataclasses import asdict

import pyxel

from ..constants import SCREEN_WIDTH
from ..image import Image
from .protocols import Renderer


CHAR_WIDTH = 4
CHAR_HEIGHT = 5


class PyxelRenderer(Renderer):
    def clear(self, color: int):
        pyxel.cls(color)

    def draw(self, img: Image, x: int, y: int):
        pyxel.blt(**asdict(img), x=x, y=y)

    def draw_title(self, x: int, y: int, text: str, color: int):
        text_width = calculate_text_width(text)
        x = SCREEN_WIDTH // 2 - text_width // 2

        pyxel.text(x + 1, y, text, 0)
        pyxel.text(x, y, text, color)

    def draw_button(self, x: int, y: int, text: str, color: int, bgcolor: int | None = None):
        button_w = 50
        v_pad = 4
        text_width = calculate_text_width(text)
        x = SCREEN_WIDTH // 2 - text_width // 2
        if bgcolor is not None:
            w, h = CHAR_WIDTH, CHAR_HEIGHT
            pyxel.rect(SCREEN_WIDTH // 2 - button_w // 2, y, button_w, h + v_pad * 2, 0)
        pyxel.text(x + 1, y + v_pad, text, 0)
        pyxel.text(x, y + v_pad, text, color)

    def draw_text_with_background(self, x: int, y: int, text: str):
        pyxel.rect(x - 3, y - 2, len(text) * CHAR_WIDTH + CHAR_HEIGHT, 9, 4)
        pyxel.text(x, y, text, 7)


def calculate_text_width(text):
    return CHAR_WIDTH * len(text) - 1
