from pygame import *
from random import *
from time import time as timer
wn =  display.set_mode((700,500))
display.set_caption("Shooter")


menu_fon = transform.scale(image.load("start.jpg"),(700,500))
level_1_fon = transform.scale(image.load("fongame1.jpg"),(700,500))

finish = False

menu = 0
level_1=1

fps = 60
clock = time.Clock()

font.init()
font1 = font.Font(None,30)
font2 = font.Font(None,80)





class Player(sprite.Sprite):
    def __init__(self, image_player,x,y,size_x,size_y,life,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.life = life
    
    def show(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))

    def move(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
            
game = 1


lanas = Player("Lana1.png", 100,100,70,90,0,10)
billies = Player("billie1.png",170,100,80,100,0,10)
billie2 = Player("billie2.png", 240,100,120,140,0,10)
lana2 = Player("Lana2.png",310,100,90,100,0,10)
beyonces = Player("beyonce.png",410,100,120,140,0,10)
maslo = Player("maslo.png",480,100,90,100,0,10)
while game:
   
    for e in event.get():
        if e.type == QUIT:
            game = 0
    
                        
    if not finish:
        if menu:
            wn.blit(menu_fon,(0,0))
            
        if level_1:
            wn.blit(level_1_fon,(0,0))
            lanas.show()
            lanas.move()
            billies.show()
            billie2.show()
            lana2.show()
            beyonces.show()
            maslo.show()


            
            
    display.update()
    clock.tick(fps)
