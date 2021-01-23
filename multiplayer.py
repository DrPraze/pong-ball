import pygame

class Main:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((900, 650))
		pygame.display.set_caption("Simple Pong Ball Multiplayer")
		self.font = pygame.font.SysFont('Helvetica', 35)
		self.draw()

	def draw(self):
		global WHITE
		WHITE = (255, 255, 255)
		pygame.draw.rect(self.screen, WHITE, (0, 80, 900, 570), 20)
		pygame.draw.line(self.screen, WHITE, (450, 80), (450, 650), 5)

	def run(self):
		width, height = 10, 100
		x, y, x1, y1 = 50, 300, 850, 300
		xvel = yvel = 3
		posx, posy = 300, 250 
		score1 = score2 = 0

		while True:
			posx += xvel
			posy += yvel
			
			if posx<21:
				xvel = abs(xvel)
				score1+=1
			if posy<100:
				yvel = abs(yvel)
			if posx>880:
				xvel = -abs(xvel)
				score2 +=1
			if posy>630:
				yvel = -abs(yvel)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()
			key = pygame.key.get_pressed()
			if key[pygame.K_w] and y>100:
				y-=3
			if key[pygame.K_s] and y<530:
				y+=3
			if key[pygame.K_UP] and y1>100:
				y1-=3
			if key[pygame.K_DOWN] and y1<530:
				y1+=3

			if (posy > y) and (posy<y+100) and (posx>x) and (posx<x+10):
				xvel = abs(xvel)
				yvel = -abs(yvel)
			if (posy > y1) and (posy<y1+100) and (posx>x1) and (posx<x1+10):
				xvel = -abs(xvel)
				yvel = -abs(yvel)

			self.screen.fill((0,0,0))
			self.draw()
			self.screen.blit(self.font.render(f'SCORES; {score1}:{score2}', True, WHITE), (70, 16))
			pygame.draw.rect(self.screen, WHITE, (x, y, width, height))
			pygame.draw.rect(self.screen, WHITE, (x1, y1, width, height))
			pygame.draw.circle(self.screen, WHITE, (posx, posy), 20)
			pygame.display.update()

if __name__=='__main__':
	Main().run()
