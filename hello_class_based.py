import pyxel

class App(object):
	def __init__(self, x, y, caption, fps):
		print(f"App(x = {x}, y = {y}, caption = {caption}, fps = {fps})")
		self.pix_x = int(x / 2) - 50
		self.pix_y = int(y / 2)
		pyxel.init(x,y, caption = caption, fps = fps)
		pyxel.run(self.update, self.draw)

	def update(self):
		self.pix_x += 1
		print('Im updating')

	def draw(self):
		pyxel.cls(0)
		pyxel.pix(self.pix_x, self.pix_y, 11)
		print('Im drawing')

App(160,160,"Moving pixel", 5)