from typing import Protocol

from .image import Image


class Renderer(Protocol):
    def clear(self, color: int) -> None:
        raise NotImplementedError

    def draw(self, img: Image, x: int, y: int) -> None:
        raise NotImplementedError

    def draw_title(self, x: int, y: int, text: str, color: int) -> None:
        raise NotImplementedError

    def draw_button(self, x: int, y: int, text: str, color: int, draw_background: bool = False) -> None:
        raise NotImplementedError

    def draw_text_with_background(self, x: int, y: int, text: str) -> None:
        raise NotImplementedError
