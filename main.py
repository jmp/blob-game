#!/usr/bin/env python3

from game.app import App
from game.adapter.pyxel_window import PyxelWindow
from game.adapter.pyxel_renderer import PyxelRenderer
from game.adapter.pyxel_input_device import PyxelInputDevice
from game.screen.menu_screen import MenuScreen

if __name__ == "__main__":
    window = PyxelWindow()
    renderer = PyxelRenderer()
    input_device = PyxelInputDevice()
    initial_screen = MenuScreen()
    App(window, renderer, input_device, initial_screen)
