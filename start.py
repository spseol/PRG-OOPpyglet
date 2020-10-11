#!/usr/bin/env python3
# Datum:   06.11.2018 10:01
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Popis: Startovací soubor pro začátek práce s knohovnou pylet
#        https://pyglet.readthedocs.io/en/latest/
############################################################################
import pyglet


# from pyglet.window.key import LEFT, RIGHT, UP, DOWN, LCTRL
# from pyglet.window.mouse import LEFT as MouseLEFT

window = pyglet.window.Window(width=800, height=600)
batch = pyglet.graphics.Batch()  # pro optimalizované vyreslování objektů


img = pyglet.image.load("img/Meteors/meteorBrown_big3.png")
ship = pyglet.sprite.Sprite(img, batch=batch)


@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event
def on_key_press(sym, mod):
    print(sym, mod)


@window.event
def on_key_release(sym, mod):
    print(sym, mod)


@window.event
def on_mouse_press(x, y, button, mod):
    print(x, y, button)
    ship.x = x
    ship.y = y


def tick(dt):
    ship.x += 1
    ship.y += 1


# funkce tick se spustí 30x za sekundu
pyglet.clock.schedule_interval(tick, 1 / 30)

# nekonečná smyčka ve které se čeká na události, které se následně obsluhují
pyglet.app.run()
