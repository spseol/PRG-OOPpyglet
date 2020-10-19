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

window = pyglet.window.Window(width=1000, height=800)
batch = pyglet.graphics.Batch()  # pro optimalizované vyreslování objektů


class Sutr(pyglet.sprite.Sprite):
    def __init__(self, img_file, x=0, y=0, speedx=0, speedy=0):
        self.img = pyglet.image.load(img_file)
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        super().__init__(self.img, batch=batch)
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy

    def move(self):
        self.x += self.speedx
        self.y += self.speedy


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
    stoneA.x = x
    stoneA.y = y


def tick(dt):
    stoneA.move()
    stoneB.move()


stoneA = Sutr("img/Meteors/meteorBrown_big4.png", speedx=2, speedy=3)
stoneB = Sutr(
    "img/Meteors/meteorBrown_big1.png", x=100, y=200, speedx=1, speedy=4
)

# funkce tick se spustí 30x za sekundu
pyglet.clock.schedule_interval(tick, 0.030)


# nekonečná smyčka ve které se čeká na události, které se následně obsluhují
pyglet.app.run()
