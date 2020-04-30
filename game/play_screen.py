import pyxel

from .objects.ghost import Ghost
from .objects.player import Player
from .screen import Screen


class PlayScreen(Screen):
    def __init__(self):
        self.player = Player()
        self.enemies = []
        for x in range(15):
            enemy = Ghost()
            enemy.x = 0 - x * 10
            self.enemies.append(enemy)
        self.objects = [self.player] + self.enemies
        self.enemy_counter = 0
        self.game_over = False

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            from game.menu_screen import MenuScreen
            self.next_screen = MenuScreen()
            return
        if self.game_over:
            return
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
                return
        self.player.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(5, 5, f'{len(self.enemies)}', 15)
        for obj in self.objects:
            obj.draw()
        if self.game_over:
            game_over_text = 'GAME OVER'
            pyxel.rect(57, 18, len(game_over_text) * 4 + 5, 9, 4)
            pyxel.text(60, 20, game_over_text, 7)
            press_text = 'Press ESC to quit'
            pyxel.rect(42, 48, len(press_text) * 4 + 5, 9, 4)
            pyxel.text(45, 50, press_text, 7)
