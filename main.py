from pygame import *

SCREENSIZE = (600, 600)
COLOR = (0, 201, 198)

window = display.set_mode(SCREESIZE)
window.set_title('ping-pong')

timeer = time.Clock()

class GameSprite(spriteSprite):
    def __init__(self, img, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(img), width, height)
        self.speed = 0
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

while True:
    for e in event.get():
        if e.type == QUIT:
            run = False

        window.fill(COLOR)
        display.update()
        timeer.tick(60)