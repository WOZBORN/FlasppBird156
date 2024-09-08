import pygame as pg

pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 480, 640
BIRD_WIDTH, BIRD_HEIGHT = 50, 50
PIPE_WIDTH, PIPE_GAP = 80, 250
SPEED = 5

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Bird(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((BIRD_WIDTH, BIRD_HEIGHT))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH//4, SCREEN_HEIGHT//2))
        self.gravity = 1
        self.lift = -15
        self.velocity = 0
    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity = 0
    def jump(self):
        self.velocity = self.lift

bird = Bird()

def main():
    while True:
        #1
        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT:
                return
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_SPACE:
                    bird.jump()
        #2
        bird.update()
        #3
        screen.fill('white')
        screen.blit(bird.image, bird.rect)
        pg.display.update()
        pg.time.delay(30)

if __name__ == '__main__':
    main()