from _ast import Set

import pygame
import random

from CoreGame import Settings

WIDTH = Settings.WITDH    # Largura
HEIGHT = Settings.HEIGHT  # ALTURA
FPS = 60



# define cores
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


meteors = []
meteor_list1 =['meteorBrown_big1.png','meteorBrown_med1.png',
              'meteorBrown_med1.png','meteorBrown_med3.png',
              'meteorBrown_small1.png','meteorBrown_small2.png',
              'meteorBrown_tiny1.png']



inimigo_img = pygame.image.load((Settings.inimigoslist[Settings.currentlevel])).convert()
boss_img = pygame.image.load((Settings.bosslist[Settings.currentlevel])).convert()


img_dir = ((__file__), "Laser.png")
tiroIni_img = pygame.image.load(("Laser.png")).convert()

img_dir = ((__file__), "laser2.png")
tiro_img = pygame.image.load(("laser2.png")).convert()

mob_img = pygame.image.load((meteor_list1[random.randrange(0,5)])).convert()

background = pygame.image.load(Settings.backimg[Settings.currentlevel])



shoot_sound = pygame.mixer.Sound('lasersound.wav')
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(snd))
pygame.mixer.music.load(Settings.ostlist[Settings.currentlevel])
pygame.mixer.music.set_volume(0.5)

background_rect = background.get_rect()


#carregar pro Player
player_img = pygame.image.load(Settings.NAVIMG).convert()



spawnini = Settings.INILOCAL

for img in meteor_list1:
    meteors.append(pygame.image.load((img)).convert())


#Explosoes

explosion_anim = {}
explosion_anim['grande'] = []
explosion_anim['pequena'] = []
explosion_anim['player'] = []

for i in range(9):
    expi = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(expi).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['grande'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['pequena'].append(img_sm)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)

powerup_images = {}
powerup_images['shield'] = pygame.image.load('shield_gold.png').convert()
powerup_images['gun'] = pygame.image.load('bolt_gold.png').convert()


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
            shoot_sound.play()

        elif powerup == 2:
            bullet = Bullet(self.rect.centerx - 10, self.rect.top, 0)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet1 = Bullet(self.rect.centerx + 10, self.rect.top, 0)
            all_sprites.add(bullet1)
            bullets.add(bullet1)
            shoot_sound.play()

        elif powerup >= 3:
            bullet = Bullet(self.rect.centerx - 20, self.rect.top, 1)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet1 = Bullet(self.rect.centerx, self.rect.top, 0)
            all_sprites.add(bullet1)
            bullets.add(bullet1)
            bullet3 = Bullet(self.rect.centerx + 20, self.rect.top, 2)
            all_sprites.add(bullet3)
            bullets.add(bullet3)
            shoot_sound.play()



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
        self.radius = int(self.rect.width * .85 / 2)
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
        self.radius = int(self.rect.width * .20 / 2)
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

        if self.i % Settings.frequencia_tiros_inimigos[Settings.currentlevel] == 0:
            for j in range(20):
                self.shoot()

    def shoot(self):
        bullet4 = BulletIni(self.rect.centerx, self.rect.bottom , 0)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)



class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150, 150))
        self.image = boss_img
        self.image = pygame.transform.scale(boss_img, (150, 150))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .20 / 2)
        self.image.set_colorkey(BLACK)
        r = random.randrange(0,2)
        self.rect.x = 1
        self.rect.y = 2
        self.speedy = 0.5
        if r == 1:
            self.speedx = 1
        else:
            self.speedx = -1


        self.i = 0


    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 30 or self.rect.left < -45 or self.rect.right > WIDTH + 40:
            self.speedx *= -1
        elif self.rect.left < 0:
            self.speedx *= -1




        self.i +=1

        if self.i % Settings.frequencia_tiros_inimigos[Settings.currentlevel] == 0:
            for j in range(20):
                self.shoot()

    def shoot(self):
        bullet4 = BulletIni(self.rect.centerx, self.rect.bottom , 0)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
        bullet4 = BulletIni(self.rect.centerx - 20, self.rect.bottom, -1)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
        bullet4 = BulletIni(self.rect.centerx, self.rect.bottom, 0)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
        bullet4 = BulletIni(self.rect.centerx + 20, self.rect.bottom, -2)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
        bullet4 = BulletIni(self.rect.centerx + 40, self.rect.bottom, -4)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
        bullet4 = BulletIni(self.rect.centerx + 60, self.rect.bottom, -8)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
        bullet4 = BulletIni(self.rect.centerx + 80, self.rect.bottom, -10)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
        bullet4 = BulletIni(self.rect.centerx + 100, self.rect.bottom, -12)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
       # shootboss_sound.play()

class PoweShield(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = ('shield')
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the bottom of the screen
        if self.rect.top > HEIGHT:
            self.kill()

class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = ('gun')
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the bottom of the screen
        if self.rect.top > HEIGHT:
           self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center



font_name = pygame.font.match_font('Chandas')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / Settings.vidas) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
def newinim():
    ini = Inimigos()
    all_sprites.add(ini)
    inimigos.add(ini)

def newboss():
    bos = Boss()
    all_sprites.add(bos)
    bosses.add(bos)






mobs = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
bosses = pygame.sprite.Group()
player = Player()


all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bulletsIni = pygame.sprite.Group()
powerups = pygame.sprite.Group()
lasers = pygame.sprite.Group()
all_sprites.add(player)
shieldpowerups = pygame.sprite.Group()





pontos = 0
pygame.mixer.music.play(loops=-1)

# Game loop
game_over = True
i=0
pup = 1
contador = Settings.vidas
bs = 0
cooldown = 0
running = True
while running:
    i+=1
    #if game_over:
        #show_go_screen()
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

#PROGRESSAO DE INIMIGOS E NO FIM ENDBOSS

    if i % 300 == 0:
        for j in range(1):

            newboss()

    if i % 600 == 0:
        for j in range(Settings.quantidade_inimigos[Settings.currentlevel]):

            newinim()

    if i % 800 == 0:
        for j in range(Settings.quantidade_inimigos[Settings.currentlevel]):
            newinim()

    if i % 1200 == 0:
        for j in range(Settings.quantidade_inimigos[Settings.currentlevel]):
            newinim()

    if i % 1600 == 0:
        for j in range(Settings.quantidade_inimigos[Settings.currentlevel]):
            newinim()


    # Update
    all_sprites.update()


    if bs == 29:
        bs=0
    else:
        bs+=1

    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        pontos += 100 - hit.radius
        random.choice(expl_sounds).play()
        mob_img = pygame.image.load((meteor_list1[random.randrange(0, 5)])).convert()
        expl = Explosion(hit.rect.center, 'grande')
        all_sprites.add(expl)
        if random.randint(1, 30)  == Settings.prob_de_dropar_shield:  # Integer from 1 to 10
            sh = PoweShield(hit.rect.center)
            all_sprites.add(sh)
            shieldpowerups.add(sh)


    hits = pygame.sprite.spritecollide(player, bulletsIni, True)
    if cooldown != 0:
        cooldown-=1

    if hits:
        if cooldown == 0:
            expl = Explosion(player.rect.center,'pequena')
            all_sprites.add(expl)
            print(contador)
            if contador == 0:
                running = False
            contador -= 1
            cooldown = 120


    hits = pygame.sprite.spritecollide(player, mobs, True)
    if hits:
        if cooldown == 0:
            expl = Explosion(player.rect.center,'pequena')
            all_sprites.add(expl)
            print(contador)
            if contador == 0:
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.kill()

            # if the player died and the explosion has finished playing
            if contador == 0 and not death_explosion.alive():
                running = False
            contador -= 1
            cooldown = 60


    hits = pygame.sprite.groupcollide(inimigos, bullets, True, True)
    for hit in hits:
        pontos += 500 - hit.radius
        random.choice(expl_sounds).play()
        expl = Explosion(hit.rect.center, 'grande')
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)


    hits = pygame.sprite.groupcollide(mobs, lasers, True, False)


    hits = pygame.sprite.spritecollide(player, powerups, True)
    if hits:
        pup +=1

    hits = pygame.sprite.spritecollide(player, shieldpowerups, True)
    if hits:
        contador +=1





    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    draw_text(screen, str(pontos), 20, WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, contador)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit() 