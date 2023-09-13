from dataclasses import asdict

import pyxel

from image import Image
from .protocols import Renderer


class PyxelRenderer(Renderer):
    def draw(self, img: Image, x: int, y: int):
        pyxel.blt(**asdict(img), x=x, y=y)
