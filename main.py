#!/usr/bin/env python3

from game.app import App
from game.input_devices.pyxel_input_device import PyxelInputDevice
from game.screens.menu_screen import MenuScreen

if __name__ == "__main__":
    input_device = PyxelInputDevice()
    initial_screen = MenuScreen()
    App(input_device, initial_screen)
