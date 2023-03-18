from pygame import *

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

clock = time.Clock()
FPS = 60
game = True

class GameSprite(sprite.Sprite):
    def __init__(self,filename,speed,x,y, size_x=65, size_y=65):
        super().__init__()
        self.image = transform.scale(image.load(filename),(size_x,size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 5 :
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 635 :
            self.rect.y += self.speed
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 5 :
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 635 :
            self.rect.y += self.speed



ball = GameSprite("ball.png", 10, 250, 250)
player1 = Player("Pingpong.png", 20, 500, 250)
player2 = Player("Pingpong.png", 20, 20, 250)

speed_x = 3
speed_y = 3
finish = False

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render("PLAYER 1 LOSES!", True, (180, 0, 0))
lose2 = font1.render("PLAYER 2 LOSES!", True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.fill(back)
        player1.reset()
        player1.update_2()
        player2.update_1()
        player2.reset()
        ball.reset()
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if ball.rect.x > 600-65:
        finish = True
        window.blit(lose2, (200, 200))

    display.update()
    clock.tick(FPS)