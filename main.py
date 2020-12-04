import pyglet
import random
from character import select
from pyglet.window import mouse
from dp import main, match



files, path = select()
ninjas = []
pos_x = []
pos_y = []
index = 0
pairs = 5

window = pyglet.window.Window(1200,630)
image = pyglet.resource.image('img/background/worldmap2.jpg')
label = pyglet.text.Label('Konoha',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//1, y=window.height//1,
                          anchor_x='center', anchor_y='center')

mapping = {}

@window.event
def on_mouse_press(x, y, button, modifiers):
    global index
    if ((button == mouse.LEFT or button == mouse.RIGHT or button == mouse.MIDDLE)and index < 2*pairs):
        print('mouse clicked', x, y)
        ninja_sprite = pyglet.resource.animation(path + files[index])
        mapping[x, y] = str(files[index])
        pos_x.append(x)
        pos_y.append(y)   
        ninja = pyglet.sprite.Sprite(ninja_sprite, x=int(x - 30), y=int(y-30))
        ninjas.append(ninja)
        index+=1
        #print(mapping)
    
    if ((button == mouse.LEFT or button == mouse.RIGHT or button == mouse.MIDDLE)and index == 2*pairs):
        save = main(pos_x, pos_y, pairs)
        print('\n\n\n================================TEAMS REPORT===============================================')
        for i in range(0,len(save), 2):
            if(save[i] == -1): continue
            print(mapping[pos_x[save[i]], pos_y[save[i]]], mapping[pos_x[save[i+1]], pos_y[save[i+1]]])

        print('================================================================================================')


@window.event
def on_draw():
    window.clear()
    label.draw()
    image.blit(0,0,width=window.width,height=window.height)
    for ninja in ninjas:
        ninja.draw()

pyglet.app.run()
