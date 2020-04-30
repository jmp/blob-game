from abc import ABC, abstractmethod


class Screen(ABC):
    next_screen = None

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass
