import pyglet
import random
from character import select
from pyglet.window import mouse



files, path = select()
ninjas = []
index = 0

window = pyglet.window.Window(1200,630)
image = pyglet.resource.image('img/background/worldmap2.jpg')
label = pyglet.text.Label('Konoha',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//1, y=window.height//1,
                          anchor_x='center', anchor_y='center')



@window.event
def on_mouse_press(x, y, button, modifiers):
    global index
    if button == mouse.LEFT or button == mouse.RIGHT or button == mouse.MIDDLE:
        print('mouse clicked', x, y)
        ninja_sprite = pyglet.resource.animation(path + files[index])
        ninja = pyglet.sprite.Sprite(ninja_sprite, x=int(x - 30), y=int(y-30))
        ninjas.append(ninja)
        index+=1
        

@window.event
def on_draw():
    window.clear()
    label.draw()
    image.blit(0,0,width=window.width,height=window.height)
    for ninja in ninjas:
        ninja.draw()

pyglet.app.run()
