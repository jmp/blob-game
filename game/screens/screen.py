from abc import ABC, abstractmethod


class Screen(ABC):
    @abstractmethod
    def update(self) -> "Screen":
        pass

    @abstractmethod
    def draw(self) -> None:
        pass
