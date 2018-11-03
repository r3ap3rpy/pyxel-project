import pyxel
import random
from random import randint

class App(object):
	def __init__(self, x, y, caption, fps):
		print(f"App(x = {x}, y = {y}, caption = {caption}, fps = {fps})")
		pyxel.init(x,y, caption = caption, fps = fps)
		pyxel.run(self.update, self.draw)

	def draw_pixel(self, x, y, color):
		pyxel.pix(x,y,color)

	def draw_line(self, x,y, color):
		pyxel.line(x,y,x+10,y,color)

	def draw_rect(self, x, y, color):
		pyxel.rect(x,y,x+10,y+10,color)

	def draw_circle(self, x, y, r, color):
		pyxel.circ(x,y,r,color)

	def draw_text(self, x, y, message, color):
		pyxel.text(x, y, message, color)

	def update(self):
		pass

	def draw(self):
		FG = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
		BG = 16 % FG
		pyxel.cls(BG)
		self.draw_pixel(30,10,FG)
		self.draw_line(30,30,FG)
		self.draw_rect(30,50,FG)
		self.draw_circle(30,100,15,FG)
		self.draw_text(30,130,'Pyxel is awesome!',FG)


App(160,160,"Moving pixel", 5)