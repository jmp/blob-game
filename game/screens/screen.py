from abc import ABC, abstractmethod
from typing import Optional


class Screen(ABC):
    def __init__(self):
        self.next_screen: Optional[Screen] = None

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass
