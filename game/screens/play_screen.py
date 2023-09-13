from typing import List

from ..renderers.protocols import Renderer
from ..input_devices.protocols import InputDevice
from ..objects.ghost import Ghost
from ..objects.player import Player
from .screen import Screen


class PlayScreen(Screen):
    def __init__(self):
        self.player: Player = Player(75, 55)
        self.enemies: List[Ghost] = []
        for x in range(15):
            enemy = Ghost()
            enemy.x = 0 - x * 10
            self.enemies.append(enemy)
        self.objects = [self.player] + self.enemies
        self.enemy_counter = 0
        self.game_over = False

    def update(self, input_device: InputDevice) -> Screen:
        if input_device.is_cancel_pressed:
            from .menu_screen import MenuScreen
            return MenuScreen()
        if self.game_over:
            return self
        self.enemy_counter += 1
        if self.enemy_counter > 70:
            self.enemy_counter = 0
            enemy = Ghost()
            self.enemies.append(enemy)
            self.objects.append(enemy)
        for enemy in self.enemies:
            enemy.update()
            if enemy.overlaps(self.player):
                self.game_over = True
        self.player.handle_input(input_device)
        self.player.update()
        return self

    def draw(self, renderer: Renderer) -> None:
        renderer.clear(0)
        # pyxel.text(5, 5, f'{len(self.enemies)}', 15)
        for obj in self.objects:
            obj.draw(renderer)
        if self.game_over:
            renderer.draw_text_with_background(60, 20, 'GAME OVER')
            renderer.draw_text_with_background(45, 50, 'Press ESC to quit')
