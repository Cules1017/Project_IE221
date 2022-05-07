
import pygame, sys, threading

pygame.init()

screen = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("Loading Bar!")

FONT = pygame.font.SysFont("Roboto", 100)


CLOCK = pygame.time.Clock()


WORK = 10000000


LOADING_BG = pygame.image.load("asset/loading/Loading Bar Background.png")
LOADING_BG_RECT = LOADING_BG.get_rect(center=(640, 360))


loading_bar = pygame.image.load("asset/loading/Loading Bar.png")
loading_bar_rect = loading_bar.get_rect(midleft=(200, 300))
loading_finished = False
loading_progress = 0
loading_bar_width = 4

def doWork():
	
	global loading_finished, loading_progress

	for i in range(WORK):
		math_equation = 523687 / 789456 * 89456
		loading_progress = i 

	loading_finished = True


finished = FONT.render("Done!", True, "white")
finished_rect = finished.get_rect(center=(640, 360))

# Thread
threading.Thread(target=doWork).start()

# Game loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill("#ffffff")

	

	loading_bar_width = loading_progress / WORK * 720

	loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 150))
	loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))

	screen.blit(LOADING_BG, LOADING_BG_RECT)
	screen.blit(loading_bar, loading_bar_rect)

	pygame.display.update()
	CLOCK.tick(10)