from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BBox:
    x: int = 0
    y: int = 0
    w: int = 8
    h: int = 8

    def at(self, x, y) -> BBox:
        return BBox(x + self.x, y + self.y, self.w, self.h)

    def overlaps(self, other: BBox) -> bool:
        if self.x + self.w < other.x:
            return False
        if self.x > other.x + other.w:
            return False
        if self.y > other.y + other.h:
            return False
        if self.y + self.h < other.y:
            return False
        return True
