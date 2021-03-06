print("\n\n\n")

import sys

import pygame
import random

print("ITS EGG TIME :)")

pygame.init()

fps = 73
fpsClock = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("eggEater")

bgc = (0, 0, 50)


def hilo(a, b, c):
    if c < b: b, c = c, b
    if b < a: a, b = b, a
    if c < b: b, c = c, b
    return a + c


def complement(r, g, b):
    k = hilo(r, g, b)
    return tuple(k - u for u in (r, g, b))


class Egg:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 25, 25)
        self.rect.x = random.randint(25, width - 25)
        self.rect.y = random.randint(25, height - 25)

    def update(self):
        pygame.draw.rect(screen, complement(bgc[0], bgc[1], bgc[2]), self.rect)


class Player:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

        pygame.draw.rect(screen, complement(bgc[0], bgc[1], bgc[2]), self.rect)


player = Player()
eggs = [Egg(), Egg(), Egg(), Egg(), Egg()]

spawn_egg = pygame.USEREVENT
pygame.time.set_timer(spawn_egg, 1000)

score = 0

# Game loop.
running = True
while running:
    screen.fill(bgc)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_egg:
            bgc = (random.randint(0, 254), random.randint(0, 254), random.randint(0, 254))

    # Update.

    player.update()
    for egg in eggs:
        egg.update()
        if player.rect.colliderect(egg.rect):
            eggs.remove(egg)
            eggs.append(Egg())
            score += 1
            print("NICE! score:", score)

    # Draw.

    if bgc[0] == 255:
        bgc = (random.randint(0, 254), bgc[1], bgc[2])

    bgc = (bgc[0] + 1, bgc[1], bgc[2])

    if bgc[1] == 255:
        bgc = (bgc[0], random.randint(0, 254), bgc[2])

    bgc = (bgc[0], bgc[1] + 1, bgc[2])

    if bgc[2] == 255:
        bgc = (bgc[0], bgc[1], random.randint(0, 254))

    bgc = (bgc[0], bgc[1], bgc[2] + 1)

    pygame.display.flip()
    fpsClock.tick(fps)
pygame.quit()
