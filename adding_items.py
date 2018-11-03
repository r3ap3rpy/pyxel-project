import pyxel
import random
from random import randint

class Star(object):
	def __init__(self,x,y):
		self._x = x
		self._y = y
		self._is_alive = True
		self._color = 7

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	@property
	def is_alive(self):
		return self._is_alive
	
	@property
	def is_alive(self):
		return self._is_alive

	@is_alive.setter
	def is_alive(self,value):
		self._is_alive = value
	
	@property
	def color(self):
		return self._color

	@color.setter
	def color(self,value):
		self._color = value	
	
class Pixel(object):
	def __init__(self,x,y):
		self._x = x
		self._y = y
		self._is_alive = True
		self._color = 8

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	@property
	def is_alive(self):
		return self._is_alive

	@is_alive.setter
	def is_alive(self,value):
		self._is_alive = value
	
	@property
	def color(self):
		return self._color

	@color.setter
	def color(self,value):
		self._color = value

class App(object):
	def __init__(self, x, y, caption, fps):
		print(f"App(x = {x}, y = {y}, caption = {caption}, fps = {fps})")
		self._startstars = 20
		self._startpixels = 60
		self.x = int(x / 2)
		self.y = int(y / 2)
		self.stars = [Star(random.choice([randint(10,int(x / 2)-20),randint(int(x / 2)+20,x-10)]),random.choice([randint(10,int(y / 2)-20),randint(int(y / 2)+20,y-10)])) for i in range(self._startstars)]
		self.pixels = [Pixel(random.choice([randint(10,int(x / 2)-20),randint(int(x / 2)+20,x-10)]),random.choice([randint(10,int(y / 2)-20),randint(int(y / 2)+20,y-10)])) for i in range(self._startpixels)]
		pyxel.init(x,y, caption = caption, fps = fps)
		pyxel.run(self.update, self.draw)

	def draw_rect(self, x, y, color):
		pyxel.rect(x,y,x+10,y+10,color)

	def draw_pix(self,pixel):
		pyxel.pix(pixel.x, pixel.y, pixel.color)
	
	def draw_star(self, star):
		pyxel.line(star.x - 2, star.y, star.x + 2, star.y, star.color)
		pyxel.line(star.x, star.y - 2, star.x, star.y + 2, star.color)
		pyxel.line(star.x - 2, star.y - 2, star.x + 2, star.y + 2, star.color)
		pyxel.line(star.x - 2, star.y + 2, star.x + 2, star.y - 2, star.color)

	def update(self):
		if pyxel.btnp(pyxel.KEY_UP):
			self.y = (self.y - 1) % (pyxel.height - 10)
		if pyxel.btnp(pyxel.KEY_DOWN):
			self.y = (self.y + 1) % (pyxel.height - 10)
		if pyxel.btnp(pyxel.KEY_LEFT):
			self.x = (self.x - 1) % (pyxel.width - 10)
		if pyxel.btnp(pyxel.KEY_RIGHT):
			self.x = (self.x + 1) % (pyxel.width - 10)
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

	def draw(self):
		pyxel.cls(0)
		self.draw_rect(self.x, self.y, 11)
		for star in self.stars:
			self.draw_star(star)

		for pixel in self.pixels:
			self.draw_pix(pixel)




App(160,160,"Stars", 30)