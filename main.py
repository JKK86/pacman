import pgzrun
from pgzero.builtins import Actor, keyboard
from pgzero.screen import Screen

from pacman_behavior import Pacman

WIDTH = 600
HEIGHT = 660
keys: keyboard
screen: Screen

pacman = Pacman(keys)

color_map = Actor('colorful_map', pos=(0, 80), anchor=(0, 0))


def draw():
    screen.fill((0, 0, 0))
    color_map.draw()
    pacman.draw(screen)


def on_key_down(key):
    pacman.on_key_down(key)


def on_key_up(key):
    pacman.on_key_up(key)


def update():
    pacman.update()


pgzrun.go()
