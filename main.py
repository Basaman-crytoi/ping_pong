from pygame import *

window = display.set_mode((900, 500))
display.set_caption("ping-pong")
syba = transform.scale(image.load("ping_pong.png"), (900, 500))

run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(syba, (0, 0))
    display.update()
quit()


    