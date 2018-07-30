from _ast import Set

import pygame
import random

from CoreGame import Settings



WIDTH = Settings.WITDH  # Largura
HEIGHT = Settings.HEIGHT  # ALTURA
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Inicializa o PYGAME e cria a Janela

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceShip Dário")
clock = pygame.time.Clock()


#Instaciar e carregar imagens pro SPRITE

Background2 = ['1.gif','2.gif','3.gif','4.gif','5.gif','6.gif','7.gif','8.gif','9.gif','10.gif','11.gif','12.gif','13.gif','14.gif','15.gif'
    , '16.gif','17.gif','18.gif','19.gif','20.gif','21.gif','22.gif','23.gif','24.gif','25.gif','26.gif','27.gif','28.gif','29.gif','0.gif']

Background1 = pygame.image.load(("space5.jpg"))

img_dir = ((__file__), "space5.jpg")

meteors = []
meteor_list1 =['meteorBrown_big1.png','meteorBrown_med1.png',
              'meteorBrown_med1.png','meteorBrown_med3.png',
              'meteorBrown_small1.png','meteorBrown_small2.png',
              'meteorBrown_tiny1.png']

img_dir = ((__file__), "RD1.png")
inimigo_img = pygame.image.load(("RD1.png")).convert()

img_dir = ((__file__), "Laser.png")
tiroIni_img = pygame.image.load(("Laser.png")).convert()

img_dir = ((__file__), "laser2.png")
tiro_img = pygame.image.load(("laser2.png")).convert()

mob_img = pygame.image.load((meteor_list1[random.randrange(0,5)])).convert()

background = pygame.image.load(Settings.backimg[Settings.bgcurrente])






background_rect = background.get_rect()


#carregar pro Player
player_img = pygame.image.load(Settings.NAVIMG).convert()



spawnini = Settings.INILOCAL

for img in meteor_list1:
    meteors.append(pygame.image.load((img)).convert())






class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = tiro_img
        self.image = pygame.transform.scale(tiro_img, (15, 500))

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.centerx = player.rect.centerx
        self.rect.bottom = player.rect.top
        keystate = pygame.key.get_pressed()
        if not keystate[pygame.K_m]:
            self.kill()



class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y,d):
        pygame.sprite.Sprite.__init__(self)
        self.image = tiro_img
        self.image = pygame.transform.scale(tiro_img, (8, 10))

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.direc = d

    def update(self):
        self.rect.y += self.speedy

        if self.direc == 1:
            self.rect.x += self.speedy +7
        elif self.direc == 2:
            self.rect.x -= self.speedy +7

        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


class BulletIni(pygame.sprite.Sprite):
    def __init__(self, x, y,d):
        pygame.sprite.Sprite.__init__(self)
        self.image = tiro_img
        self.image = pygame.transform.scale(tiroIni_img, (8, 10))

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -5
        self.direc = d

    def update(self):
        self.rect.y -= self.speedy

        if self.direc == 1:
            self.rect.x += self.speedy +7
        elif self.direc == 2:
            self.rect.x -= self.speedy +7

        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = player_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.image_orig = pygame.transform.scale(player_img, (50, 52))
        self.image = self.image_orig.copy()

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx

        self.speedy = 0
        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self,powerup):
        if powerup == 1:
            bullet = Bullet(self.rect.centerx, self.rect.top, 0)
            all_sprites.add(bullet)
            bullets.add(bullet)
        elif powerup == 2:
            bullet = Bullet(self.rect.centerx - 10, self.rect.top, 0)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet1 = Bullet(self.rect.centerx + 10, self.rect.top, 0)
            all_sprites.add(bullet1)
            bullets.add(bullet1)
        elif powerup == 3:
            bullet = Bullet(self.rect.centerx - 20, self.rect.top, 1)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet1 = Bullet(self.rect.centerx, self.rect.top, 0)
            all_sprites.add(bullet1)
            bullets.add(bullet1)
            bullet3 = Bullet(self.rect.centerx + 20, self.rect.top, 2)
            all_sprites.add(bullet3)
            bullets.add(bullet3)



    def laser(self):
        laser = Laser(self.rect.centerx, self.rect.top)
        all_sprites.add(laser)
        lasers.add(laser)





class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image = mob_img
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center


class Inimigos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 12))
        self.image = inimigo_img
        self.image = pygame.transform.scale(inimigo_img, (50, 50))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        r = random.randrange(0,2)
        self.rect.x = spawnini[r]
        self.rect.y = random.randrange(20, 300)
        self.speedy = 1
        if r == 0:
            self.speedx = 5
        else:
            self.speedx = -5


        self.i = 0


    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.speedx *= -1
        elif self.rect.left < 0:
            self.speedx *= -1




        self.i +=1

        if self.i % 10 == 0:
            for j in range(20):
                self.shoot()

    def shoot(self):
        bullet4 = BulletIni(self.rect.centerx, self.rect.bottom , 0)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)




mobs = pygame.sprite.Group()

player = Player()
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bulletsIni = pygame.sprite.Group()
lasers = pygame.sprite.Group()
all_sprites.add(player)




for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)




# Game loop
i=0
pup = 3
contador = Settings.vidas
bs = 0
cooldown = 0
running = True
while running:
    i+=1

    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot(pup)
            if event.key == pygame.K_m:
                player.laser()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_m:
                mobs.add(lasers)



    # Update
    all_sprites.update()


    if bs == 29:
        bs=0
    else:
        bs+=1

    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    if i % 120 == 0:
        for j in range(15):
            mob_img = pygame.image.load((meteor_list1[random.randrange(0, 5)])).convert()
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)


    hits = pygame.sprite.spritecollide(player, bulletsIni, True)
    if cooldown != 0:
        cooldown-=1

    if hits:
        if cooldown == 0:
            if pup > 1:
                pup-=1
            print(contador)
            if contador == 0:
                running = False
            contador -= 1
            cooldown = 120


    hits = pygame.sprite.spritecollide(player, mobs, True)
    if hits:
        if cooldown == 0:
            if pup > 1:
                pup -= 1
            print(contador)
            if contador == 0:
                running = False
            contador -= 1
            cooldown = 120

    hits = pygame.sprite.groupcollide(mobs, lasers, True, False)
    #if i % 1800 == 0:
     ##      mob_img = pygame.image.load((meteor_list[random.randrange(0, 5)])).convert()
       #     m = Mob()
        #    all_sprites.add(m)




    if i % 300 == 0:
        for j in range(3):

            m = Inimigos()

            all_sprites.add(m)
            mobs.add(m)


    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()