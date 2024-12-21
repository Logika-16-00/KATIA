#Створи власний Шутер!

from typing import Any
from pygame import *
from random import *

wn = display.set_mode((700,500))
display.set_caption("shooter")
fps = 60
fon = transform.scale(image.load('galaxy.jpg'),(700,500))
finish = 0 
clock = time.Clock()
game = 1
rocket = draw
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()



class Player(sprite.Sprite):
    def __init__(self, image_player,x,y,size_x,size_y,speed,life):
        super().__init__()
        self.image= transform.scale(image.load(image_player),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.life = life
        
    def show(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))
        
    def move(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed

class Enemy(Player):
    def  update(self):
        self.rect.x += self.speed
        if self.rect.x > 500:
            self.rect.y = -10

rocket = Player('rocket.png',300,360,60,130,5,5)


monsters = sprite.Group()
for i in  range(5)
    monster = Enemy(randint'ufo',(0,650),60,60,randint(1,5),0)
    monsters.add(monster)
while 1:
    for e in event.get():
        if e.type == QUIT:
            game = 0


    if not finish:
        wn.blit(fon,(0,0))
        rocket.show()
        rocket.move()
        monsters.draw(wn)
        monsters.update()

    display.update()
    clock.tick(fps)
  
