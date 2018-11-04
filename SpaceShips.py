import pyxel
import random
import os

class Heart(object):
	def __init__(self, x, y):
		self._x = x
		self._y = y
		self.heal = random.randrange(20,50)
		self.color = 11

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self,value):
		self._x = value

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self,value):
		self._y = value

class Enemy(object):
	def __init__(self, x, y):
		self._x = x
		self._y = y
		self.color = 2

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self,value):
		self._x = value

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self,value):
		self._y = value


class Ship(object):
	def __init__(self, x, y):
		self._x = x 
		self._y = y
		self.color = 11
		self._life = 100
		self._score = 0

	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self, value):
		self._score += 1
	@property
	def x(self):
		return self._x

	@x.setter
	def x(self,value):
		self._x = value

	@property
	def life(self):
		return self._life

	@life.setter
	def life(self,value):
		self._life = value

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self,value):
		self._y = value

class Projectile(object):
	def __init__(self, x, y, affiliation):
		self._x = x
		self._y = y		
		if affiliation == 'ship':
			self.color = 8
		else:
			self.color = 7	
		self._affiliation = affiliation

	@property
	def affiliation(self):
		return self._affiliation

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self,value):
		self._x = value

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self,value):
		self._y = value


class WarShipz(object):
	def __init__(self):
		pyxel.init(255,255,caption = "Warshipz",fps = 20)
		self.warship = Ship(120,240)
		self.maxenemies = 20
		self.enemies = []	
		self.hearts = []	
		self.in_game = True
		if os.path.isfile('highscore'):
			with open('highscore') as hs:
				self.highscore = int(hs.read())
		else:
			self.highscore = 0
		for i in range(self.maxenemies):
			self.enemies.append(Enemy(random.randrange(0,pyxel.width),20))

		self.projectiles = []
		pyxel.sound(0).set("e3e3c3f1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr","p","6","vffn fnff vffs vfnn",25,)
		pyxel.sound(1).set("r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ","s","6","nnff vfff vvvv vfff svff vfff vvvv svnn",25,)
		pyxel.sound(2).set("c1g1c1g1 c1g1c1g1 b0g1b0g1 b0g1b0g1" "a0e1a0e1 a0e1a0e1 g0d1g0d1 g0d1g0d1","t","7","n",25,)
		pyxel.sound(3).set("f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1" "f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1","t","7","n",25,)
		pyxel.sound(4).set("f0ra4r f0ra4r f0ra4r f0f0a4r", "n", "6622 6622 6622 6422", "f", 25)
		self.play_music()
		pyxel.run(self.update, self.draw)

	def play_music(self):
		pyxel.play(0, [0, 1], loop=True)
		pyxel.play(1, [2, 3], loop=True)
		pyxel.play(2, 4, loop=True)

	def draw_projectile(self, projectile):
		pyxel.pix(projectile.x, projectile.y, projectile.color)

	def draw_highscore(self, highscore):
		pyxel.text(0,10,"Last highscore: {}".format(highscore),9)

	def draw_score(self,score):
		pyxel.text(0,18,"Current score: {}".format(score),9)

	def draw_heart(self, heart):
		pyxel.circ(heart.x-2,heart.y,2,heart.color)
		pyxel.circ(heart.x+2,heart.y,2,heart.color)
		pyxel.line(heart.x,heart.y+5,heart.x,heart.y,heart.color)
		pyxel.line(heart.x,heart.y+5,heart.x+1,heart.y,heart.color)
		pyxel.line(heart.x,heart.y+5,heart.x-1,heart.y,heart.color)
		pyxel.line(heart.x,heart.y+5,heart.x-2,heart.y,heart.color)
		pyxel.line(heart.x,heart.y+5,heart.x+2,heart.y,heart.color)
		pyxel.line(heart.x,heart.y+5,heart.x-3,heart.y,heart.color)
		pyxel.line(heart.x,heart.y+5,heart.x+3,heart.y,heart.color)
		pyxel.line(heart.x,heart.y+5,heart.x-4,heart.y,heart.color)
		pyxel.line(heart.x,heart.y+5,heart.x+4,heart.y,heart.color)
		pyxel.line(heart.x,heart.y+5,heart.x-5,heart.y,heart.color)
		pyxel.line(heart.x,heart.y+5,heart.x+5,heart.y,heart.color)

	def draw_life(self, life):
		if life in range(80,101):
			color = 11
		elif life in range(50,80):
			color = 10
		elif life in range(30,50):
			color = 9
		else:
			color = 8
		pyxel.text(0,2,"Life remaining: {}".format(life),color)

	def draw_enemy(self, enemy):
		pyxel.pix(enemy.x, enemy.y+1, enemy.color)
		pyxel.pix(enemy.x, enemy.y+2, enemy.color)
		pyxel.pix(enemy.x, enemy.y, enemy.color)
		pyxel.pix(enemy.x+1, enemy.y, enemy.color)
		pyxel.pix(enemy.x-1, enemy.y, enemy.color)
		pyxel.pix(enemy.x+2, enemy.y, enemy.color)
		pyxel.pix(enemy.x-2, enemy.y, enemy.color)
		pyxel.pix(enemy.x+1, enemy.y-1, enemy.color)
		pyxel.pix(enemy.x-1, enemy.y-1, enemy.color)
		pyxel.pix(enemy.x+2, enemy.y-1, enemy.color)
		pyxel.pix(enemy.x-2, enemy.y-1, enemy.color)		


	def draw_ship(self, warship):
		pyxel.pix(warship.x,warship.y-5,warship.color)
		pyxel.pix(warship.x,warship.y-6,warship.color)
		pyxel.pix(warship.x-1,warship.y-6,warship.color)
		pyxel.pix(warship.x+1,warship.y-6,warship.color)
		pyxel.circ(warship.x,warship.y,5,warship.color)
		pyxel.pix(warship.x+6,warship.y,warship.color)
		pyxel.pix(warship.x-6,warship.y,warship.color)
		pyxel.pix(warship.x+6,warship.y+1,warship.color)
		pyxel.pix(warship.x-6,warship.y+1,warship.color)
		pyxel.pix(warship.x+6,warship.y+2,warship.color)
		pyxel.pix(warship.x-6,warship.y+2,warship.color)
		pyxel.pix(warship.x+7,warship.y,warship.color)
		pyxel.pix(warship.x-7,warship.y,warship.color)
		pyxel.pix(warship.x+7,warship.y+1,warship.color)
		pyxel.pix(warship.x-7,warship.y+1,warship.color)
		pyxel.pix(warship.x+7,warship.y+2,warship.color)
		pyxel.pix(warship.x-7,warship.y+2,warship.color)
		pyxel.pix(warship.x+8,warship.y,warship.color)
		pyxel.pix(warship.x-8,warship.y,warship.color)
		pyxel.pix(warship.x+8,warship.y+1,warship.color)
		pyxel.pix(warship.x-8,warship.y+1,warship.color)
		pyxel.pix(warship.x+8,warship.y+2,warship.color)
		pyxel.pix(warship.x-8,warship.y+2,warship.color)
		pyxel.pix(warship.x+8,warship.y,warship.color)
		pyxel.pix(warship.x-8,warship.y,warship.color)
		pyxel.pix(warship.x+8,warship.y+3,warship.color)
		pyxel.pix(warship.x-8,warship.y+3,warship.color)
		pyxel.pix(warship.x+8,warship.y+4,warship.color)
		pyxel.pix(warship.x-8,warship.y+4,warship.color)
		pyxel.pix(warship.x+8,warship.y,warship.color)
		pyxel.pix(warship.x-8,warship.y,warship.color)
		pyxel.pix(warship.x+8,warship.y+5,warship.color)
		pyxel.pix(warship.x-8,warship.y+5,warship.color)
		pyxel.pix(warship.x+8,warship.y+6,warship.color)
		pyxel.pix(warship.x-8,warship.y+6,warship.color)

	def update(self):
		if self.in_game:
			if random.randint(1,10000) in range(50):
				self.hearts.append(Heart(random.randrange(20,pyxel.width-20),20))

			if len(self.enemies) < self.maxenemies:
				self.enemies.append(Enemy(random.randrange(0,pyxel.width),20))

			for heart in self.hearts:
				if random.randrange(1,100) in range(25):
					heart.x = heart.x + 1 % pyxel.width
				elif random.randrange(1,100) in range(25):
					heart.x = heart.x - 1 % pyxel.width
				elif random.randrange(1,100) in range(50):
					heart.y = heart.y + 5

				if (heart.x - 1 or heart.x-2 or heart.x -3 or heart.x or heart.x + 1 or heart.x+2 or heart.x +3) in [self.warship.x+8,self.warship.x-8,self.warship.x-1,self.warship.x-2,self.warship.x-3,self.warship.x-4,self.warship.x-5,self.warship.x-6,self.warship.x-7,self.warship.x, self.warship.x+1,self.warship.x+2,self.warship.x+3,self.warship.x+4,self.warship.x+5,self.warship.x+6,self.warship.x+7] and heart.y in [self.warship.y+1,self.warship.y+2,self.warship.y, self.warship.y-1,self.warship.y-2,self.warship.y-3,self.warship.y-4]:
					self.warship.life = (self.warship.life + heart.heal)
					if self.warship.life > 100:
						self.warship.life = 100
					self.hearts.remove(heart)

				if heart.y > 250:
					self.hearts.remove(heart)

			for projectile in self.projectiles:
				if projectile.y <= 0:
					self.projectiles.remove(projectile)
				if projectile.affiliation == "ship":
					projectile.y -= 2
				elif projectile.affiliation == "enemy":
					projectile.y += 2

				if projectile.y > 250:
					self.projectiles.remove(projectile)

			for enemy in self.enemies:
				if enemy.y >= 230:
					self.warship.life -= 2
					self.enemies.remove(enemy)

				if random.randrange(1,100) in range(2):
					self.projectiles.append(Projectile(enemy.x,enemy.y, 'enemy'))
				if random.randrange(1,100) in range(25):
					enemy.x = enemy.x + 1 % pyxel.width
				elif random.randrange(1,100) in range(25):
					enemy.x = enemy.x - 1 % pyxel.width
				elif random.randrange(1,100) in range(50):
					enemy.y = enemy.y + 2

			for projectile in [ _ for _ in self.projectiles if _.affiliation == 'ship']:
				for enemy in self.enemies:
					if projectile.x in [enemy.x, enemy.x + 1, enemy.x - 1, enemy.x + 2, enemy.x -2] and projectile.y in [enemy.y, enemy.y + 1,enemy.y+2,enemy.y -1 ]:
						self.enemies.remove(enemy)
						self.warship.score += 1
						try:
							self.projectiles.remove(projectile)
						except:
							pass

			for projectile in [ _ for _ in self.projectiles if _.affiliation != 'ship']:
				if projectile.x in [self.warship.x+8,self.warship.x-8,self.warship.x-1,self.warship.x-2,self.warship.x-3,self.warship.x-4,self.warship.x-5,self.warship.x-6,self.warship.x-7,self.warship.x, self.warship.x+1,self.warship.x+2,self.warship.x+3,self.warship.x+4,self.warship.x+5,self.warship.x+6,self.warship.x+7] and projectile.y in [self.warship.y+1,self.warship.y+2,self.warship.y, self.warship.y-1,self.warship.y-2,self.warship.y-3,self.warship.y-4]:				
					self.warship.life -= 2
					self.projectiles.remove(projectile)
					if self.warship.life <= 0:
						self.in_game = False
						if self.warship.score > self.highscore:
							with open('highscore','w') as hs:
								hs.write(str(self.warship.score))



			if pyxel.btn(pyxel.KEY_LEFT):
				if self.warship.x> 8:
					self.warship.x = (self.warship.x - 2)

			if pyxel.btn(pyxel.KEY_RIGHT):
				if self.warship.x < pyxel.width - 10:
					self.warship.x = (self.warship.x + 2)

			if pyxel.btnp(pyxel.KEY_LEFT_CONTROL):
				self.projectiles.append(Projectile(self.warship.x,self.warship.y - 8,"ship"))
		else:
			if pyxel.btnp(pyxel.KEY_Q):
				pyxel.quit()

	def draw(self):
		if self.in_game:
			pyxel.cls(0)
			self.draw_ship(self.warship)
			self.draw_life(self.warship.life)
			self.draw_score(self.warship.score)
			self.draw_highscore(self.highscore)
			for projectile in self.projectiles:
				self.draw_projectile(projectile)

			for enemy in self.enemies:
				self.draw_enemy(enemy)
			for heart in self.hearts:
				self.draw_heart(heart)
		else:
			pyxel.cls(0)
			pyxel.text(100,100,"Game Over! Press Q to quit!",8)
					

WarShipz()