from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BBox:
    x: int = 0
    y: int = 0
    w: int = 8
    h: int = 8
    offset_x: int = 0
    offset_y: int = 0

    def overlaps(self, other: BBox) -> bool:
        x = self.x + self.offset_x
        y = self.y + self.offset_y
        other_x = other.x + other.offset_x
        other_y = other.y + other.offset_y
        if x <= other_x - self.w:
            return False
        if x >= other_x + other.w:
            return False
        if y >= other_y + other.h:
            return False
        if y <= other_y - self.h:
            return False
        return True
