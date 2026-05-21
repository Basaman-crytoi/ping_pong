from pygame import *

z = 900
h = 600

font.init()
font = font.SysFont('Arial', 100)




window = display.set_mode((z, h))
display.set_caption("ping-pong")
syba = transform.scale(image.load("ping_pong.png"), (z, h))


class GameSprite(sprite.Sprite):
    def __init__(self, paper, x, y, speed, up=K_p, down=K_o, wid=70, hei=70):
        super().__init__()
        self.image = transform.scale(image.load(paper), (wid, hei))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.up = up
        self.down = down

    def blit(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        klavisha = key.get_pressed()
        if klavisha[self.up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if klavisha[self.down] and self.rect.y < h - 135:
            self.rect.y += self.speed


ball = GameSprite("ball.png", 200, 100, 10)
player1 = Player("platform.png", 54, 250, 8, K_w, K_s, 45, 135)
player2 = Player("platform.png", 800, 250, 8, K_UP, K_DOWN, 45, 135)


run = True
dx = 5
dy = -10
while run:
    window.blit(syba, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    if ball.rect.y < 0 or ball.rect.y > 530:
        dy *= -1
    ball.rect.x += dx
    ball.rect.y += dy
    if sprite.collide_rect(ball, player2):
        dx *= -1  
    if sprite.collide_rect(ball, player1):
        dx *= -1  
    if ball.rect.x > 900:
        window.blit(font.render("Игрок справа проиграл", 1, (145, 4, 4)), (150, 350))
    if ball.rect.x < 0:
        window.blit(font.render("Игрок слева проиграл", 1, (145, 4, 4)), (150, 350))
    ball.blit()
    ball.update()
    player1.blit()
    player1.update()
    player2.blit()
    player2.update()
    display.update()
quit()
