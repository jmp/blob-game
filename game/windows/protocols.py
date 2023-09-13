from typing import Protocol, Callable


class Window(Protocol):
    def initialize(self) -> None:
        raise NotImplementedError

    def run_main_loop(self, update_func: Callable, draw_func: Callable) -> None:
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError
