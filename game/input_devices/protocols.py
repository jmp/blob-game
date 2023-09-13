from typing import Protocol


class InputDevice(Protocol):
    @property
    def is_left_held(self) -> bool:
        raise NotImplementedError

    @property
    def is_right_held(self) -> bool:
        raise NotImplementedError

    @property
    def is_up_held(self) -> bool:
        raise NotImplementedError

    @property
    def is_down_held(self) -> bool:
        raise NotImplementedError

    @property
    def is_up_pressed(self) -> bool:
        raise NotImplementedError

    @property
    def is_down_pressed(self) -> bool:
        raise NotImplementedError

    @property
    def is_accept_pressed(self) -> bool:
        raise NotImplementedError

    @property
    def is_cancel_pressed(self) -> bool:
        raise NotImplementedError
