from dataclasses import dataclass


@dataclass
class Image:
    img: int = 0
    u: int = 0
    v: int = 0
    w: int = 8
    h: int = 8
    colkey: int = -1
