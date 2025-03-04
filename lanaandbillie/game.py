from pygame import *
from random import *
from time import time as timer
wn =  display.set_mode((700,600))
display.set_caption("Shooter")


menu_fon = transform.scale(image.load("start.jpg"),(700,600))
level_1_fon = transform.scale(image.load("fongame1.jpg"),(700,600))
level_2_fon = transform.scale(image.load("fongame2.jpg"),(700,600))
game_over_fon = transform.scale(image.load("Gameover.jpg"),(700,600))
game_win_fon = transform.scale(image.load("youwin.jpg"),(700,600))

finish = False

menu = 1
level_1=0
level_2=0

fps = 60
clock = time.Clock()

font.init()
font1 = font.Font(None,30)
font2 = font.Font(None,80)

mixer.init()
#фонова музика
mixer.music.load("billie-eilish-birds-of-a-feather.mp3")
# mixer.music.play()

music_level1 = mixer.Sound("Lana Del Rey - Ultraviolence.mp3")
music_level2 = mixer.Sound("billie-eilish-birds-of-a-feather.mp3")
#музика для зіткення


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
        draw.rect(wn, (255, 0, 0), self.rect, 2)

    def move1(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
    def move2(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
game = 1


lanas = Player("Lana1.png", -400,-800,70,90,0,10)
billies = Player("billie1.png",170,100,80,100,0,10)
billie2 = Player("billie2.png", 240,100,90,100,5,10)
lana2 = Player("Lana2.png",310,100,90,100,5,10)
maslo = Player("maslo.png",305,350,50,70,0,10)
beyonces = Player("beyonce.png",randint(0,400),350,120,140,0,5)
play = Player("cnopkastart.png",randint(0,395),randint(0,150),300,190,0,10)
playagain = Player("cnopkaplay.png",270,430,380,260,0,10)
exit = Player("cnopkaexit.png",randint(0,395),randint(300,400),300,190,0,10)
game_over = 0
game_win = 0

while game:
   
    for e in event.get():
        if e.type == QUIT:
            game = 0
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            print(x, y)
            if play.rect.collidepoint(x, y) and menu:
                play.rect.x = randint(0,500)
                play.rect.y = randint(0,500)
                
            if exit.rect.collidepoint(x, y) and menu:
                menu = 0
                level_1 = 1
                music_level1.play()
                start_level1 = timer()
                
            if playagain.rect.collidepoint(x, y) and game_over:
                game_over = 0
                game_win = 0
                finish = 0 
                level_1 = 1
                start_level1 = timer()
                level_2 = 0
                
                lanas = Player("Lana1.png", -400,-800,70,90,0,10)
                billies = Player("billie1.png",170,100,80,100,0,10)
                billie2 = Player("billie2.png", 240,100,90,100,5,10)
                lana2 = Player("Lana2.png",310,100,90,100,5,10)
                maslo = Player("maslo.png",305,350,50,70,0,10)
                beyonces = Player("beyonce.png",randint(0,400),350,120,140,0,5)

    
                        
    if not finish:
        if menu:
            wn.blit(menu_fon,(0,0))
            play.show()
            exit.show()
            
        if level_1:
            wn.blit(level_1_fon,(0,0))
            lanas.show()
            # lanas.move1()
            billies.show()
            billies.move1()
            if lanas.rect.x > billies.rect.x:
                lanas.rect.x -= 5
            if lanas.rect.x < billies.rect.x:
                lanas.rect.x += 5
            if lanas.rect.y > billies.rect.y:
                lanas.rect.y -= 5
            if lanas.rect.y < billies.rect.y:
                lanas.rect.y += 5
                
            if lanas.rect.colliderect(billies.rect):
                finish = 1
                game_over = 1
                
            if timer() - start_level1 > 10:
                level_1 = 0
                level_2 = 1
                start_level2 = timer()
                music_level1.stop()
                music_level2.play()
        if level_2:
            wn.blit(level_2_fon,(0,0))
            life_text1 = font1.render(f"Життя: {lana2.life}", True, (255, 255, 255))
            
            wn.blit(life_text1, (10, 10))
            billie2.show()
            billie2.move1()
            lana2.show()
            lana2.move1()
            maslo.show()
            beyonces.show()
            beyonces.rect.x += beyonces.speed
            if beyonces.rect.x <= 0 or beyonces.rect.x >= 650:
                beyonces.speed *= -1
            maslo.rect.y -=7
            if maslo.rect.y <= 0 :
                maslo.rect.y = beyonces.rect.centery 
                maslo.rect.x =  beyonces.rect.centerx -40
                
            if lana2.rect.colliderect(maslo.rect) or billie2.rect.colliderect(maslo.rect):
                maslo.rect.y = beyonces.rect.centery 
                maslo.rect.x =  beyonces.rect.centerx -40
                lana2.life -= 1
                
            if lana2.life <= 0:
                game_win = 1
                finish = 1
            
            if timer() - start_level2 > 3:
                finish = 1
                game_win = 1
            
        if game_over:
            music_level1.stop()
            music_level2.stop()

            wn.blit(game_over_fon,(0,0))
            playagain.show()
            
        if game_win:
            music_level1.stop()
            music_level2.stop()
            wn.blit(game_win_fon,(0,0))
            
            
        
            

            
            
    display.update()
    clock.tick(fps)
