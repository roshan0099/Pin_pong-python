import pygame
pygame.init()
class game:
	def __init__(self):
		self.movement_x = 100
		self.movement_y = 493
		self.rect = pygame.Rect(self.movement_x,self.movement_y,150,5)
		self.ball = pygame.Rect(self.movement_x/2,self.movement_y/2,15,15)
		self.move_speed = 0
		self.ball_speed_x = 5
		self.ball_speed_y = 5
		self.count = 0
		self.pause = False

	def moves(self,event):
		self.event = event
		if self.event.type == pygame.KEYDOWN:
			if self.event.key == pygame.K_RIGHT:
				self.move_speed = 10
			elif self.event.key == pygame.K_LEFT:
				self.move_speed = -10
			# elif self.event.key == pygame.K_SPACE :
			# 	self.pause = not self.pause	
		
		if self.event.type == pygame.KEYUP:		
			if self.event.key == pygame.K_RIGHT or self.event.key == pygame.K_LEFT :
				self.move_speed = 0

	def moves_player(self):
		self.rect.x += self.move_speed
		if self.rect.left <= 0 :
		 	self.rect.left = 5
		if self.rect.right >= 800 :
			self.rect.right = 795				
		#print(self.rect.x)

	def game_over(self) :
		pass
		# if self.ball.bottom == self.rect.top:	
		# 	print("hey")


	def moves_ball(self):
		self.ball.x += self.ball_speed_x
		self.ball.y += self.ball_speed_y
		if self.ball.top <=0 : #or self.ball.bottom >= 500 :
			self.ball_speed_y *= -1
		elif self.ball.bottom >= self.rect.top :
			if self.ball.colliderect(self.rect) :
				self.ball_speed_y *= -1 
				print("true ")
				self.count +=1
		if self.ball.bottom >= 500 :
			self.ball.center = (800/2,500/2)
			self.ball_speed_x *= -1 
			self.pause = True

		if self.ball.left <=0 or self.ball.right >=800 :
			self.ball_speed_x *= -1
		#if self.ball.bottom - self.rect.top <= 0 :
	
# def time_req():
# 	global temp 
# 	while True :
# 		temp +=1 


clock = pygame.time.Clock()
screen_x,screen_y = 800,500
screen = pygame.display.set_mode((screen_x,screen_y))


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

start = True 
board = game()
font = pygame.font.Font("freesansbold.ttf",30)


startTime = time.time()
# image = font.render('score : ' + str(temp), True, BLUE)
temp =0
while(start) :

	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			start = False

		board.moves(event)
	if board.pause == False:
		board.game_over() 		
		board.moves_player()
		board.moves_ball()
		board.game_over()

		screen.fill(BLACK)
		image = font.render('score : ' + str(board.count), True, BLUE)
		screen.blit(image,(20, 20))

		pygame.draw.rect(screen,RED,board.rect)
		pygame.draw.ellipse(screen,BLUE,board.ball)

		pygame.display.update()		
		clock.tick(60)
pygame.quit()	
