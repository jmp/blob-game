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
        if self.offset_x + self.x + self.w <= other.offset_x + other.x:
            return False
        if self.offset_x + self.x >= other.offset_x + other.x + other.w:
            return False
        if self.offset_y + self.y >= other.offset_y + other.y + other.h:
            return False
        if self.offset_y + self.y + self.h <= other.offset_y + other.y:
            return False
        return True
