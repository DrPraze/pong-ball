import sys
import pygame
from time import sleep
from random import randint

class game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 500))
        pygame.display.set_caption("PONG BALL")
        self.font = pygame.font.SysFont('Helvetica', 35)
        self.draw()

    def draw(self):
        global WHITE, BLACK
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        pygame.draw.rect(self.screen, WHITE, (0, 250, 600, 2))
        pygame.draw.rect(self.screen, WHITE, (500, 0, 2, 500))
        self.screen.blit(self.font.render(b'SCORE:', True, WHITE), (500, 40))
        place = 10
        for i in range(2):
            pygame.draw.rect(self.screen, WHITE, (0, place, 500, 15))
            place += 460


    def run(self):
        score = 0
        x = 250
        y = 440
        x1 = 300
        y1 = 40
        vel = 3
        width = 100
        height = 10
        xvel  = 3
        yvel = 3
        running = True
        posx = 300
        posy = 250
        ball = pygame.draw.circle(self.screen, WHITE, (posx, posy), 20)
        scoreA = 0
        scoreB = 0
        
        while running:
            posx += xvel
            posy += yvel

            if posx<20:
                xvel = abs(xvel)
            if posy<50:
                yvel = abs(yvel)
                #-#scoreB+=1 #the AI doesn't need scoresit is UNBEATABLE, lol 
            if posx>500:
                xvel = -abs(xvel)
            if posy>480:
                yvel = -abs(yvel)
                scoreA += 1

            if posx > x1 and x1<500-width:
                x1 += vel
            if posx < x1 and x1>0:
                x1 -= vel
                
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT] and x<500-width:
                x+= vel
            if key[pygame.K_LEFT] and x>0:
                x-=vel

            if (posy > y) and (posy<y+10) and (posx>x) and (posx<x+100):
                xvel = -abs(xvel)
                yvel = -abs(yvel)

            if (posy > y1) and (posy<y1+10) and (posx>x1) and (posx<x1+100):
                xvel = -abs(xvel)
                yvel = -abs(yvel)

            self.screen.fill(BLACK)
            self.draw()
            self.screen.blit(self.font.render(f'{scoreA}', True, WHITE), (570, 176))
            self.screen.blit(self.font.render(f'{scoreB}', True, WHITE), (570, 256))
            ball = pygame.draw.circle(self.screen, WHITE, (posx, posy), 20)
            AI = pygame.draw.rect(self.screen, WHITE, (x1, y1, 100, 10))
            player = pygame.draw.rect(self.screen, WHITE, (x, y, width, height))
            pygame.display.update()
        pygame.quit()
if __name__=='__main__':
    AI = game()
    sleep(4)
    AI.run()
