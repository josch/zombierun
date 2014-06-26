import pygame
import random
from math import sqrt

def main():
    pygame.init()

    w, h = 640,480
    screen = pygame.display.set_mode([w,h])
    screen.fill([255,255,255])

    mainloop = True
    x1, y1 = w/2+10, h/2
    x2, y2 = w/2-10, h/2
    fps = 60

    Clock = pygame.time.Clock()

    zx = list()
    zy = list()
    zs = list()
    m = 0 # countdown to next zombie
    n = 0 # number of zombies

    myFont = pygame.font.SysFont("None", 30)

    p1 = 0
    p2 = 0

    while mainloop:
        tickFPS = Clock.tick(fps)
        pygame.display.set_caption("Press Esc to quit. FPS: %.2f" % (Clock.get_fps()))
        screen.fill((255,255,255))
        screen.blit(myFont.render("%d"%n, 0, (0,0,0)), (5,5))
        screen.blit(myFont.render("%d"%p1, 0, (0,0,255)), (50,5))
        screen.blit(myFont.render("%d"%p2, 0, (255,0,0)), (100,5))
        p1 = 0
        p2 = 0
        keys = pygame.key.get_pressed()

        # update player 1
        if keys[pygame.K_UP] and y1 > 0:       y1 -= 1
        if keys[pygame.K_DOWN] and y1 < h-10:  y1 += 1
        if keys[pygame.K_LEFT] and x1 > 0:     x1 -= 1
        if keys[pygame.K_RIGHT] and x1 < w-10: x1 += 1
        screen.fill((0,0,255), pygame.Rect(x1,y1,10,10))

        # update player 2
        if keys[pygame.K_v] and y2 > 0:    y2 -= 1
        if keys[pygame.K_i] and y2 < h-10: y2 += 1
        if keys[pygame.K_u] and x2 > 0:    x2 -= 1
        if keys[pygame.K_a] and x2 < w-10: x2 += 1
        screen.fill((255,0,0), pygame.Rect(x2,y2,10,10))

        # decide whether to add new zombies
        m += 1
        if m > fps*2:
            n += 1
            while True:
                x = random.randrange(w)
                y = random.randrange(h)
                if sqrt((x-x1)**2 + (y-y1)**2) > 40 and sqrt((x-x2)**2 + (y-y2)**2) > 40:
                    zx.append(x)
                    zy.append(y)
                    break
            zs.append(random.uniform(0.15,0.65))
            m = 0

        # draw zombies
        for i in range(n):
            screen.fill((0,0,0), pygame.Rect(zx[i],zy[i],5,5))
        # check if any zombies collide
        for i in range(n):
            if x1<zx[i]+4 and x1+10>zx[i] and y1<zy[i]+4 and y1+10>zy[i]:
                mainloop = False
            if x2<zx[i]+4 and x2+10>zx[i] and y2<zy[i]+4 and y2+10>zy[i]:
                mainloop = False
        # update zombie pos
        for i in range(n):
            # determine closest player
            if (zx[i]-x1)*(zx[i]-x1)+(zy[i]-y1)*(zy[i]-y1) > (zx[i]-x2)*(zx[i]-x2)+(zy[i]-y2)*(zy[i]-y2):
                p2 += 1
                x = x2
                y = y2
            else:
                p1 += 1
                x = x1
                y = y1
            if x>zx[i]: zx[i]+=zs[i]
            else:       zx[i]-=zs[i]
            if y>zy[i]: zy[i]+=zs[i]
            else:       zy[i]-=zs[i]

        # get keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    mainloop = False
        pygame.display.flip()
    pygame.time.wait(2000)
    print n
    pygame.quit()

if __name__ == "__main__":
    main()
