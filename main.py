import pyglet
import random
from character import select
from pyglet.window import mouse
from dp import main, match
from reporteam import screen
import time
from multiprocessing import Process

music = pyglet.resource.media('soundtrack/soundtrack.mp3')
music.play()

files, path = select()
ninjas = []
pos_x = []
pos_y = []
index = 0
pairs = 7
direct = 'img/character/'
pairteam = []

window = pyglet.window.Window(1200,630)
image = pyglet.resource.image('img/background/worldmap2.jpg')


mapping = {}

@window.event
def on_mouse_press(x, y, button, modifiers):
    global index
    if ((button == mouse.LEFT or button == mouse.RIGHT or button == mouse.MIDDLE)and index < 2*pairs):
        if(not(pos_x.count(x) and pos_y.count(y))):
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
            pairteam.append(direct + str(mapping[pos_x[save[i]], pos_y[save[i]]]))
            pairteam.append(direct + str(mapping[pos_x[save[i+1]], pos_y[save[i+1]]]))
        print('================================================================================================')
        
        p1 = Process(target=screen, args=(pairteam,))
        time.sleep(2)
        
        p1.start()
        

@window.event
def on_draw():
    window.clear()
    image.blit(0,0,width=window.width,height=window.height)
    for ninja in ninjas:
        ninja.draw()

pyglet.app.run()
