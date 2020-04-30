import pyxel

from constants import SCREEN_WIDTH

CHAR_WIDTH = 4
CHAR_HEIGHT = 5


def calculate_text_width(text):
    return CHAR_WIDTH * len(text) - 1


def draw_title(x, y, text, color):
    text_width = calculate_text_width(text)
    x = SCREEN_WIDTH // 2 - text_width // 2

    # pyxel.rect(0, 16, SCREEN_WIDTH, 13, 0)
    pyxel.text(x + 1, y, text, 0)
    pyxel.text(x, y, text, color)


def draw_button(x, y, text, color, bgcolor=None):
    button_w = 50
    button_h = 15
    v_pad = 4
    text_width = calculate_text_width(text)
    x = SCREEN_WIDTH // 2 - text_width // 2
    if bgcolor is not None:
        w, h = CHAR_WIDTH, CHAR_HEIGHT
        pyxel.rect(SCREEN_WIDTH // 2 - button_w // 2, y, button_w, h + v_pad * 2, 0)
    pyxel.text(x + 1, y + v_pad, text, 0)
    pyxel.text(x, y + v_pad, text, color)
