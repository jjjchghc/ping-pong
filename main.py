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
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
          self.rect.y -= self.speed
        if keys[k_s]  and self.rect.y + self.rect.height < SCREENSIZE[1]:
            self.rect.y += self.speed

    def update_left(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
          self.rect.y -= self.speed
        if keys[k_DOWN]  and self.rect.y + self.rect.height < SCREENSIZE[1]:
            self.rect.y += self.speed
            
platform_left = Player("platform.png", 20, 350, 4, 25, 99)
platform_right = Player("platform.png", 660, 350, 4, 25, 99)

while True:
    for e in event.get():
        if e.type == QUIT:
            run = False

        window.fill(COLOR)
        display.update()
        timeer.tick(60)