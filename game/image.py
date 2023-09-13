from dataclasses import dataclass


@dataclass(frozen=True)
class Image:
    img: int = 0  # image bank
    u: int = 0  # u-coordinate on image
    v: int = 0  # v-coordinate on image
    w: int = 8  # image width
    h: int = 8  # image height
    colkey: int = -1  # no color key
