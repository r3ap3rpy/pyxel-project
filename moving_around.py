import pyxel
import random
from random import randint

class App(object):
	def __init__(self, x, y, caption, fps):
		print(f"App(x = {x}, y = {y}, caption = {caption}, fps = {fps})")
		self.x = int(x / 2)
		self.y = int(y / 2)
		pyxel.init(x,y, caption = caption, fps = fps)
		pyxel.run(self.update, self.draw)

	def draw_rect(self, x, y, color):
		pyxel.rect(x,y,x+10,y+10,color)


	def update(self):
		if pyxel.btnp(pyxel.KEY_UP):
			self.y = (self.y - 1) % 256 
		if pyxel.btnp(pyxel.KEY_DOWN):
			self.y = (self.y + 1) % 256
		if pyxel.btnp(pyxel.KEY_LEFT):
			self.x = (self.x - 1) % 256
		if pyxel.btnp(pyxel.KEY_RIGHT):
			self.x = (self.x + 1) % 256
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

	def draw(self):
		pyxel.cls(0)
		self.draw_rect(self.x, self.y, 11)




App(160,160,"Moving pixel", 30)