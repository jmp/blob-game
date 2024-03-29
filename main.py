#!/usr/bin/env python3

from game.app import App
from game.screen.menu_screen import MenuScreen

from adapters.pyxel_window import PyxelWindow
from adapters.pyxel_renderer import PyxelRenderer
from adapters.pyxel_input_device import PyxelInputDevice


if __name__ == "__main__":
    window = PyxelWindow()
    renderer = PyxelRenderer()
    input_device = PyxelInputDevice()
    initial_screen = MenuScreen()
    App(window, renderer, input_device, initial_screen)
