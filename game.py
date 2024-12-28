from pygame import *
from pygame.sprite import *

d_x=700
d_y=700
window = display.set_mode((d_x,d_y))
display.set_caption('pong')
background=transform.scale(image.load('black.jpg'),(d_x,d_y))
class game_sprite (sprite.Sprite):
    def __init__(self, images,speed,rect_y,rect_x,sx,sy):
        super().__init__()
        self.image=transform.scale(image.load(images),(sx,sy))
        self.speed= speed
        self.rect=self.image.get_rect()
        self.rect.x= rect_x
        self.rect.y= rect_y
    def reset(self): 
        window.blit(self.image,(self.rect.x,self.rect.y))

class player1(game_sprite):
    def move(self):
        keys_pressed=key.get_pressed()
        
        if keys_pressed[K_UP] and self.rect.y >=0:
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y <=d_y-200:

            self.rect.y+=self.speed

class player2(game_sprite):
    def move(self):
        keys_pressed=key.get_pressed()
        
        if keys_pressed[K_w] and self.rect.y >=0:
            self.rect.y-=self.speed
        if keys_pressed[K_s] and self.rect.y <=d_y-200:

            self.rect.y+=self.speed
class ball(game_sprite):
    def move(self):
        self.rect.x+=self.speed
        self.rect.y+=15

pong1=player1('racket.png',20,300,100,50,150)
pong2=player2('racket.png',20,300,d_x-100,50,150)
ping=ball('tenis_ball.png',15,350,350,50,50)
game=True
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type==QUIT:
            game=False
    if sprite.collide_rect(pong1,ping):
        ping.speed*=-1
    elif sprite.collide_rect(pong2,ping):
        ping.speed*=-1    
    elif ping.rect.y==-50 or ping.rect.x==-50 or ping.rect.y==d_y-50 or ping.rect.x==d_x-50:
        ping.speed*=-1
    pong1.reset()
    pong1.move()
    pong2.reset()
    pong2.move()
    ping.move()
    ping.reset()
    time.delay(50)
    display.update()
