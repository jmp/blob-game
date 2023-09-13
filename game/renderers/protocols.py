from typing import Protocol

from ..image import Image


class Renderer(Protocol):
    def clear(self, color: int):
        raise NotImplementedError

    def draw(self, img: Image, x: int, y: int):
        raise NotImplementedError

    def draw_title(self, x: int, y: int, text: str, color: int):
        raise NotImplementedError

    def draw_button(self, x: int, y: int, text: str, color: int, bgcolor: int | None = None):
        raise NotImplementedError

    def draw_text_with_background(self, x: int, y: int, text: str):
        raise NotImplementedError
