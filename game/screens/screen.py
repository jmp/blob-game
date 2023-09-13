from abc import ABC, abstractmethod

from ..renderers.protocols import Renderer
from ..input_devices.protocols import InputDevice


class Screen(ABC):
    @abstractmethod
    def update(self, input_device: InputDevice) -> "Screen":
        raise NotImplementedError

    @abstractmethod
    def draw(self, renderer: Renderer) -> None:
        raise NotImplementedError
