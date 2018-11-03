import pyxel
import argparse
from random import randint

parser = argparse.ArgumentParser(
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description="""Travelling through stars!""",
	epilog="""Argument rules:
	1) boardsize format -> 160x160 (2 integers with an x)
	2) boardsize <= 255
	""")

parser.add_argument('--startstars', type=int, nargs='?',help='Number of cells at start!')
parser.add_argument('--boardsize',  type=str, nargs='?',help='Size of the board!')
args = parser.parse_args()

class Star(object):
	def __init__(self, x, y, color):
		self._x = x
		self._y = y
		self._is_alive = True
		self._color = color

	def __str__(self):
		return f"Star(x = {self._x}, y = {self._y}, color = {self._color})"

	@property
	def is_alive(self):
		return self._is_alive

	@is_alive.setter
	def is_alive(self, value):
		self._is_alive = value
	

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, value):
		self._x = value
	
	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, value):
		self._y = value

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, value):
		self._color = value

class GoL(object):
	def __init__(self, starnum):
		self.x = x 
		self.y = y
		self.starnum = starnum
		self.stars = [Star(randint(int(self.x / 2)-20,int(self.x / 2)+40),randint(int(self.y / 2)-40,int(self.y / 2)+20),7) for i in range(self.starnum)]

		pyxel.init(self.x, self.y, caption = "Starry sky!", fps = 10)
		pyxel.run(self.update, self.draw)

	def kill_star(self):
		pass

	def draw_star(self, star):
		pyxel.line(star.x - 2, star.y, star.x + 2, star.y, star.color)
		pyxel.line(star.x, star.y - 2, star.x, star.y + 2, star.color)
		pyxel.line(star.x - 2, star.y - 2, star.x + 2, star.y + 2, star.color)
		pyxel.line(star.x - 2, star.y + 2, star.x + 2, star.y - 2, star.color)
		
	def update(self):
		if randint(1,100) in range(25):
			self.stars.append(Star(randint(int(self.x / 2)-20,int(self.x / 2)+40),randint(int(self.y / 2)-40,int(self.y / 2)+20),7))

		for star in self.stars:
			if not star.is_alive:
				self.stars.remove(star)
				continue

			if star.x < 10 or star.x > self.x - 10 or star.y < 10 or star.y > self.y - 10:
				star.is_alive = False
				star.color = 1
				continue

			if star.x > int(self.x / 2) and star.y > int(self.y / 2):
				if randint(1,10) % 2 == 0:
					star.x +=1
				else:
					star.y +=1

			elif star.x > int(self.x / 2) and star.y < int(self.y / 2):
				if randint(1,10) % 2 == 0:
					star.x +=1
				else:
					star.y -=1
			elif star.x < int(self.x / 2) and star.y > int(self.y / 2):
				if randint(1,10) % 2 == 0:
					star.x -=1
				else:
					star.y +=1
			else:
				if randint(1,10) % 2 == 0:
					star.x -=1
				else:
					star.y -=1

		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

	
	def draw(self):
		pyxel.cls(0)
		for star in self.stars:
			self.draw_star(star)




if args.boardsize == None or args.startstars == None:
	parser.print_help()
	raise SystemExit
else:
	print("Read aim fire!")
	if args.startstars < 7:
		print('You must specify a minimum of 7 cells at start!')
		raise SystemExit

	if not 'x' in args.boardsize:
		print('The boardsize needs <x> as a separator!')
		raise SystemExit

	try:
		x = int(args.boardsize.split('x')[0])
	except:
		print('Could not get width from boardsize!')
		raise SystemExit

	try:
		y = int(args.boardsize.split('x')[1])
	except:
		print('Could not get height from boardsize!')
		raise SystemExit

	if x > 255 or y > 255:
		print('The maximum size is 255x255!')
		raise SystemExit

	print(f'Starting game with {args.startstars} and width: {x} and height: {y}')

	GoL(args.startstars)